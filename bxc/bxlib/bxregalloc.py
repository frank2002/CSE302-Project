import copy
import time

from .bxcfg import *
from .union_find import UnionFind
from .bxssa import SSA


CONDITIONAL_JUMP_OPCODES = ["jz", "jnz", "jlt", "jle", "jgt", "jge"]

REGISTER_MAP = (
    "%%rax",
    "%%rcx",
    "%%rdx",
    "%%rsi",
    "%%rdi",
    "%%r8",
    "%%r9",
    "%%r10",
    "%%rbx",
    "%%r12",
    "%%r13",
    "%%r14",
    "%%r15",
    "%%r11",
    "%%rbp",
    "%%rsp",
)

REGISTER_PREORDERED = ("%%rax", "%%rdi", "%%rsi", "%%rdx", "%%rcx", "%%r8", "%%r9")

#################
# Inference Graph
#################


class InterferenceGraph:
    def __init__(self, name=None, arguments=None):
        self.graph = {}
        self.color = {}
        self.name = name
        self.arguments = arguments
        self.ret = None

        # print(self.arguments)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()

    def add_edge(self, node1, node2):
        if node1 == node2:
            return
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def remove_node(self, node):
        # Remove the node and all edges associated with it
        for neighbor in self.graph[node]:
            self.graph[neighbor].remove(node)
        del self.graph[node]

    def get_neighbors(self, node):
        return self.graph[node] if node in self.graph else set()

    def has_edge(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]

    def build(self, cfg, var_ignore=None):
        livein, liveout, all_instructions, instr_dict = liveness_analysis(cfg)
        # get all variables from cfg

        variables = set()
        for block_label, block in cfg.cfg.items():
            variables.update(get_block_variables(block))

        # print(variables)

        variables = variables - var_ignore if var_ignore else variables

        for var in variables:
            if var_ignore and var in var_ignore:
                continue
            self.add_node(var)

        for instr in all_instructions:
            if isinstance(instr_dict[instr], TAC):
                if instr_dict[instr].opcode == "copy":
                    for var1 in liveout[instr]:
                        if var_ignore and var1 in var_ignore:
                            continue
                        use = _get_use(instr_dict[instr])
                        def_set = _get_def(instr_dict[instr])
                        for var2 in use | def_set:
                            if var_ignore and var2 in var_ignore:
                                continue
                            if var1 != var2:
                                self.add_edge(var1, var2)
                else:
                    for var1 in liveout[instr]:
                        if var_ignore and var1 in var_ignore:
                            continue
                        def_set = _get_def(instr_dict[instr])
                        for var2 in def_set:
                            if var_ignore and var2 in var_ignore:
                                continue
                            if var1 != var2:
                                self.add_edge(var1, var2)
            elif isinstance(instr_dict[instr], tuple):
                if instr_dict[instr][0] == "ret":
                    self.ret = instr_dict[instr][1][0]
                for var1 in liveout[instr]:
                    var2s = set(
                        var
                        for var in instr_dict[instr][1]
                        if isinstance(var, str) and var.startswith("%")
                    )
                    for var2 in var2s:
                        if var1 != var2:
                            self.add_edge(var1, var2)
        return variables

    def max_cardinality_search(self) -> list:
        interference_graph = self.graph
        # Create a mapping weight and initialize it to 0 for all vertices
        weight = {v: 0 for v in interference_graph}
        # Copy of the vertex set
        W = set(interference_graph)
        # Resulting simplicial elimination ordering
        seo = []

        while W:
            # Pick the node with the maximum weight
            v_i = max(W, key=lambda w: weight[w])
            seo.append(v_i)
            # Update the weight of the neighbors of the picked node
            for neighbor in interference_graph[v_i]:
                if neighbor in W:
                    weight[neighbor] += 1
            # Remove the picked node from the set W
            W.remove(v_i)
        return seo

    def greedy_coloring(self, seo):
        interference_graph = self.graph

        reserved_register_colors = {
            "%%rax": 1,
            "%%rdi": 2,
            "%%rsi": 3,
            "%%rdx": 4,
            "%%rcx": 5,
            "%%r8": 6,
            "%%r9": 7,
        }

        precolored = {"input": self.arguments, "output": [self.ret]}
        # Initialize coloring with precolored nodes based on reserved registers
        coloring = {node: 0 for node in interference_graph}

        # Assign precolored input temporaries to their corresponding registers
        for index, var in enumerate(precolored["input"]):
            coloring[var] = index + 2

        # Assign precolored output temporary to the "%%rax" register
        for var in precolored["output"]:
            coloring[var] = 1

        # Iterate through nodes in the order given by the SEO
        for node in seo:
            if node in precolored["input"] or node in precolored["output"]:
                continue
            if coloring[node] == 0:  # Only color uncolored nodes
                used_colors = set(
                    coloring[neighbor] for neighbor in interference_graph[node]
                )
                # Find the smallest color not used by neighbors
                color = 1
                while color in used_colors:
                    color += 1
                # Assign the color to the current node
                coloring[node] = color
            else:
                # If the node is precolored but used as a neighbor, ensure it keeps its color
                for neighbor in interference_graph[node]:
                    if coloring[neighbor] == coloring[node]:
                        coloring[neighbor] = coloring[node]

        return coloring

    def __str__(self):
        return str(self.graph)


#################
# Register Allocation
#################


def allocation(ssa, name, arguments):
    graph = InterferenceGraph(name, arguments)
    variable_used = graph.build(ssa)

    alloc = {}
    seo = graph.max_cardinality_search()
    reg_map = {reg: REGISTER_MAP.index(reg) for reg in REGISTER_MAP}

    def col_2_reg(col):
        return REGISTER_MAP[col - 1]

    def reg_2_col(reg):
        return reg_map[reg] + 1

    color_map = graph.greedy_coloring(seo)
    num_color = len(reverse_dict(color_map))
    var_ignore = set()
    while num_color > 13:
        # we randomly pick here (not optimal)

        for var in variable_used:
            if var not in graph.arguments and var not in graph.ret:
                var_ignore.add(var)
                break

        graph = InterferenceGraph(name, arguments)
        variable_used = graph.build(ssa, var_ignore)
        seo = graph.max_cardinality_search()
        color_map = graph.greedy_coloring(seo)

        num_color = len(reverse_dict(color_map))

    for node, color in color_map.items():
        alloc[node] = col_2_reg(color)

    offset = -8
    for var in var_ignore:
        alloc[var] = offset
        offset -= 8

    stack_size = -offset - 8

    return alloc, stack_size


#################
# Live Variables
#################


def liveness_analysis(cfg: CFG):
    # Initialize livein for every instruction in every block
    livein = {}
    liveout = {}
    all_instructions = []
    instr_dict = {}
    for block_label, block in cfg.cfg.items():
        line_counter = 0

        for var, phi in block.phi_functions.items():
            index = (block_label, line_counter)

            instr = TAC("phi", phi, var)
            livein[index] = _get_use(instr)
            all_instructions.append(index)
            instr_dict[index] = instr
            line_counter += 1

        for i, instr in enumerate(block.body):
            index = (block_label, line_counter)
            livein[index] = _get_use(instr)
            all_instructions.append(index)
            instr_dict[index] = instr
            line_counter += 1

        for i, instr in enumerate(block.cjumps):
            use_list = [
                arg for arg in instr[1] if isinstance(arg, str) and arg.startswith("%")
            ]
            index = (block_label, line_counter)
            livein[index] = set(use_list)
            all_instructions.append(index)
            instr_dict[index] = instr
            line_counter += 1

        if block.jump:
            index = (block_label, line_counter)
            if block.jump[0] == "ret" and block.jump[1] and len(block.jump[1]) == 0:
                livein[index] = set([block.jump[1][0]])
            else:
                livein[index] = set()
            all_instructions.append(index)
            instr_dict[index] = block.jump

    # print(all_instructions)
    # dict_print(instr_dict, "instr_dict")

    # Step 2: Iteratively update livein sets
    changed = True
    while changed:
        changed = False
        livein_copy = livein.copy()
        for index1, instr1 in enumerate(reversed(all_instructions)):
            successors = get_successors(cfg, instr1, instr_dict, all_instructions)

            for instr2 in successors:
                livein[instr1] = livein[instr1] | (
                    livein[instr2] - _get_def(instr_dict[instr1])
                )

            if livein[instr1] != livein_copy[instr1]:
                changed = True

        # Step 3: Compute liveout sets
    for index1, instr1 in enumerate(reversed(all_instructions)):
        successors = get_successors(cfg, instr1, instr_dict, all_instructions)
        if not successors or len(successors) == 0:
            liveout[instr1] = set()
            continue
        for instr2 in successors:
            if instr1 in liveout:
                liveout[instr1] = liveout[instr1] | (livein[instr2])
            else:
                liveout[instr1] = livein[instr2]

    return livein, liveout, all_instructions, instr_dict


def get_successors(cfg, instruction_index, instr_dict, all_instructions):
    def last_index(lst, element):
        for item in reversed(lst):
            if item[0] == element:
                return item[1]
        return None

    block_label, instr_index = instruction_index
    successors = []

    current_block = cfg.cfg[block_label]

    if (
        isinstance(instr_dict[instruction_index], TAC)
        and instr_dict[instruction_index].opcode == "phi"
    ):
        successors.append((block_label, instr_index + 1))

    elif isinstance(instr_dict[instruction_index], TAC):
        successors.append((block_label, instr_index + 1))

    elif instr_index == last_index(all_instructions, block_label):
        if current_block.jump[0] == "jmp":
            next_label = current_block.jump[1]
            successors.append((next_label, 0))

        elif current_block.jump[0] == "ret":
            pass

    elif (
        isinstance(instr_dict[instruction_index], tuple)
        and instr_dict[instruction_index][0] in CONDITIONAL_JUMP_OPCODES
    ):
        successors.append((block_label, instr_index + 1))
        next_label = instr_dict[(block_label, instr_index)][1][1]
        successors.append((next_label, 0))

    return successors


def _get_use(instr):
    # Assuming 'instr' is a TAC object and arguments are a list of used variables
    if isinstance(instr, TAC) and instr.opcode == "phi":
        return set([arg[1] for arg in instr.arguments if isinstance(arg, tuple)])
    else:
        return set(
            arg
            for arg in instr.arguments
            if isinstance(arg, str) and arg.startswith("%")
        )


def _get_def(instr):
    # Assuming 'instr' is a TAC object and result is the defined variable
    if (
        isinstance(instr, TAC)
        and instr.result
        and isinstance(instr.result, str)
        and instr.result.startswith("%")
    ):
        return {instr.result}
    return set()


#################
# Helper Functions
#################


def detect_param_call_cfg(cfg: CFG) -> bool:
    for block_label, block in cfg.cfg.items():
        if detect_param_call(block):
            return True
    return False


def detect_param_call(cfg: CFGNode) -> bool:
    for instr in cfg.body:
        if instr.opcode == "param":
            return True
        if instr.opcode == "call":
            return True
    return False


def get_block_variables(block: CFGNode) -> set:
    variables = set()
    for var, phi in block.phi_functions.items():
        variables.add(var)
    for instr in block.body:
        if (
            instr.result
            and isinstance(instr.result, str)
            and instr.result.startswith("%")
        ):
            variables.add(instr.result)
        for arg in instr.arguments:
            if isinstance(arg, str) and arg.startswith("%"):
                variables.add(arg)
    for instr in block.cjumps:
        for arg in instr[1]:
            if isinstance(arg, str) and arg.startswith("%"):
                variables.add(arg)
    if block.jump:
        if (
            block.jump[0] == "ret"
            and block.jump[1]
            and len(block.jump[1]) == 0
            and isinstance(block.jump[1][0], str)
            and block.jump[0][1].startswith("%")
        ):
            variables.add(block.jump[1][0])
    return variables


def get_all_variables(cfg: CFG) -> set:
    variables = set()
    for block_label, block in cfg.cfg.items():
        for var, phi in block.phi_functions.items():
            variables.add(var)
        for instr in block.body:
            if (
                instr.result
                and isinstance(instr.result, str)
                and instr.result.startswith("%")
            ):
                variables.add(instr.result)
            for arg in instr.arguments:
                if isinstance(arg, str) and arg.startswith("%"):
                    variables.add(arg)
        for instr in block.cjumps:
            for arg in instr[1]:
                if isinstance(arg, str) and arg.startswith("%"):
                    variables.add(arg)
        if block.jump:
            if (
                block.jump[0] == "ret"
                and block.jump[1]
                and len(block.jump[1]) == 0
                and isinstance(block.jump[1][0], str)
            ):
                variables.add(block.jump[1][0])
    return variables


def dict_print(dict: dict, comment=None, sort=False) -> None:
    if sort:
        dict = dict(sorted(dict.items(), key=lambda item: (item[0][0], item[0][1])))
    if comment:
        print(comment)
    for key, value in dict.items():
        print(f"{key}: {value}")


def reverse_dict(dict: dict) -> dict:
    dic = {}
    for key, value in dict.items():
        dic.setdefault(value, []).append(key)
    return dic


if __name__ == "__main__":
    # Create the CFGNode for L0
    cfg_node0 = CFGNode()
    cfg_node0.label = "L0"
    cfg_node0.body = [
        TAC("const", [0], "%0"),
        TAC("const", [1], "%1"),
        TAC("const", [1], "%2"),
    ]
    cfg_node0.jump = ("jmp", "L1")
    cfg_node0.cjumps = []

    # Create the CFGNode for L1
    cfg_node1 = CFGNode()
    cfg_node1.label = "L1"
    cfg_node1.body = []
    cfg_node1.jump = ("jmp", "L2")
    cfg_node1.cjumps = [("jz", ["%n", "L3"])]

    # Create the CFGNode for L2
    cfg_node2 = CFGNode()
    cfg_node2.label = "L2"
    cfg_node2.body = [
        TAC("sub", ["%n", "%2"], "%n"),
        TAC("add", ["%0", "%1"], "%3"),
        TAC("copy", ["%1"], "%0"),
        TAC("copy", ["%3"], "%1"),
    ]
    cfg_node2.jump = ("jmp", "L1")
    cfg_node2.cjumps = []

    # Create the CFGNode for L3
    cfg_node3 = CFGNode()
    cfg_node3.label = "L3"
    cfg_node3.body = []
    cfg_node3.jump = ("ret", ["%0"])
    cfg_node3.cjumps = []

    # Create the CFG with all nodes
    fib_cfg = CFG(
        "L0", {"L0": cfg_node0, "L1": cfg_node1, "L2": cfg_node2, "L3": cfg_node3}
    )

    ssa = SSA(fib_cfg)
    ssa.transform()

    livein, liveout, all_instructions, instr_dict = liveness_analysis(ssa.ssa)

    sorted_livein = dict(
        sorted(livein.items(), key=lambda item: (item[0][0], item[0][1]))
    )
    sorted_liveout = dict(
        sorted(liveout.items(), key=lambda item: (item[0][0], item[0][1]))
    )

    # print("livein")
    # dict_print(sorted_livein)
    # print("liveout")
    # dict_print(sorted_liveout)

    graph = InterferenceGraph()
    graph.build(ssa.ssa)
    print(graph)
    print(graph.max_cardinality_search())
