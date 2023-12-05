from .bxcfg import *


class SSA:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ssa = None
        self.all_instructions = []
        self.instr_dict = {}
        self.version_counter = 0

    def transform(self):
        self._add_phi_functions()
        self._update_phi_functions()
        self.ssa = self.cfg
        return self.ssa

    def null_choice_elimination(self):
        for block_label, block in self.cfg.cfg.items():
            phi_functions = block.phi_functions
            for variable, phi_function in phi_functions.items():
                version = variable.split(".")[1]
                is_same = True
                for block_label2, variable2 in phi_function:
                    version2 = variable2.split(".")[1]
                    if version != version2:
                        is_same = False
                        break
                if is_same:
                    phi_functions.pop(variable)

    def rename_elimination(self):
        pass

    def _get_new_variable(self, variable: str):
        self.version_counter += 1
        return f"{variable}.{self.version_counter}"

    def _add_phi_functions(self):
        # livein analysis

        block_liveness = self._liveness_analysis()

        # initialize phi functions
        for block_label, block in self.cfg.cfg.items():
            self.cfg.cfg[block_label].phi_functions = {}
            for variable in block_liveness[block_label]:
                self.cfg.cfg[block_label].phi_functions[variable] = []

        # add versions for defs
        for block_label, block in self.cfg.cfg.items():
            new_phi_functions = {}
            for variable, phi_functions in block.phi_functions.items():
                new_phi_functions[self._get_new_variable(variable)] = phi_functions

            self.cfg.cfg[block_label].phi_functions = new_phi_functions

            for instr in block.body:
                instr.result = self._get_new_variable(instr.result)

        # update all variable versions
        for block_label, block in self.cfg.cfg.items():
            for index, instr in enumerate(reversed(block.body)):
                old_variable = instr.arguments
                new_variable = []
                for variable in old_variable:
                    is_found = False

                    if isinstance(variable, str) and variable.startswith("%"):
                        for index2, instr2 in enumerate(reversed(block.body)):
                            if (
                                index2 > index
                                and variable == instr2.result.split(".")[0]
                            ):
                                new_variable.append(instr2.result)
                                is_found = True
                                break
                        if not is_found:
                            for key in block.phi_functions:
                                if variable == key.split(".")[0]:
                                    new_variable.append(key)
                                    break
                    else:
                        new_variable.append(variable)

                instr.arguments = new_variable

            for index, instr in enumerate(reversed(block.cjumps)):
                old_variable = instr[1]
                new_variable = []
                for variable in old_variable:
                    is_found = False
                    if isinstance(variable, str) and variable.startswith("%"):
                        for index2, instr2 in enumerate(reversed(block.body)):
                            if variable == instr2.result.split(".")[0]:
                                new_variable.append(instr2.result)
                                is_found = True
                                break
                        if not is_found:
                            for key in block.phi_functions:
                                if variable == key.split(".")[0]:
                                    new_variable.append(key)
                                    break
                    else:
                        new_variable.append(variable)

                self.cfg.cfg[block_label].cjumps[len(block.cjumps) - 1 - index] = (
                    instr[0],
                    new_variable,
                )

            if block.jump:
                if block.jump[0] == "ret":
                    is_found = False
                    variable = block.jump[1]
                    if isinstance(variable, str) and variable.startswith("%"):
                        for index2, instr2 in enumerate(reversed(block.body)):
                            if variable == instr2.result.split(".")[0]:
                                self.cfg.cfg[block_label].jump = ("ret", instr2.result)

                                is_found = True
                                break
                        if not is_found:
                            for key in block.phi_functions:
                                if variable == key.split(".")[0]:
                                    self.cfg.cfg[block_label].jump = (
                                        "ret",
                                        key,
                                    )
                                    break
                    else:
                        self.cfg.cfg[block_label].jump = ("ret", instr2.result)

    def _update_phi_functions(self):
        for block_label, block in self.cfg.cfg.items():
            predecessor_blocks = self._get_predecessor_blocks(block_label)

            for variable, phi_functions in block.phi_functions.items():
                for predecessor_block in predecessor_blocks:
                    defined_variables = self._get_block_defined_variables(
                        predecessor_block, variable
                    )
                    if defined_variables:
                        self.cfg.cfg[block_label].phi_functions[variable].append(
                            (predecessor_block, defined_variables[variable])
                        )

    def _get_predecessor_blocks(self, block_label):
        predecessor = []
        for block_label2, block in self.cfg.cfg.items():
            for instr in block.cjumps:
                if instr[1][1] == block_label:
                    predecessor.append(block_label2)
                    break
            if block.jump and block.jump[1] == block_label:
                predecessor.append(block_label2)
        return predecessor

    def _get_block_defined_variables(self, block_label, variable):
        block = self.cfg.cfg[block_label]
        defined_variables = {}
        variable_prefix = variable.split(".")[0]
        for key, _ in block.phi_functions.items():
            if key.startswith(variable_prefix):
                defined_variables[variable] = key

        for instr in block.body:
            if instr.result.startswith(variable_prefix):
                defined_variables[variable] = instr.result

        return defined_variables

    def _liveness_analysis(self):
        # Initialize livein for every instruction in every block
        livein = {}
        all_instructions = []
        instr_dict = {}
        for block_label, block in self.cfg.cfg.items():
            line_counter = 0
            for i, instr in enumerate(block.body):
                index = (block_label, i)
                livein[index] = self._get_use(instr)
                all_instructions.append(index)
                instr_dict[index] = instr
                line_counter += 1

            for i, instr in enumerate(block.cjumps):
                use_list = [
                    arg
                    for arg in instr[1]
                    if isinstance(arg, str) and arg.startswith("%")
                ]
                index = (block_label, i + line_counter)
                livein[index] = set(use_list)
                all_instructions.append(index)
                instr_dict[index] = instr
                line_counter += 1

            if block.jump:
                index = (block_label, line_counter)
                if block.jump[0] == "ret":
                    livein[index] = set([block.jump[1]])
                else:
                    livein[index] = set()
                all_instructions.append(index)
                instr_dict[index] = block.jump

        # Step 2: Iteratively update livein sets
        changed = True
        while changed:
            changed = False
            livein_copy = livein.copy()
            for index1, instr1 in enumerate(reversed(all_instructions)):
                successors = self.get_successors(instr1, instr_dict, all_instructions)

                for instr2 in successors:
                    livein[instr1] = livein[instr1] | (
                        livein[instr2] - self._get_def(instr_dict[instr1])
                    )

                if livein[instr1] != livein_copy[instr1]:
                    changed = True

        # return the first livein for each label
        block_liveness = {}
        for index, instr in enumerate(all_instructions):
            block_label = instr[0]
            if block_label not in block_liveness:
                block_liveness[block_label] = livein[instr]

        self.all_instructions = all_instructions
        self.instr_dict = instr_dict
        return block_liveness

    def get_successors(self, instruction_index, instr_dict, all_instructions):
        def last_index(lst, element):
            for item in reversed(lst):
                if item[0] == element:
                    return item[1]
            return None

        block_label, instr_index = instruction_index
        successors = []

        current_block = self.cfg.cfg[block_label]

        if instr_index < len(current_block.body):
            successors.append((block_label, instr_index + 1))

        elif instr_index == last_index(all_instructions, block_label):
            if current_block.jump[0] == "jmp":
                next_label = current_block.jump[1]
                successors.append((next_label, 0))

            elif current_block.jump[0] == "ret":
                pass
        elif instr_index > len(current_block.body) - 1 and instr_index < last_index(
            all_instructions, block_label
        ):
            successors.append((block_label, instr_index + 1))
            next_label = instr_dict[(block_label, instr_index)][1][1]
            successors.append((next_label, 0))

        return successors

    def _get_use(self, instr):
        # Assuming 'instr' is a TAC object and arguments are a list of used variables
        return set(
            arg
            for arg in instr.arguments
            if isinstance(arg, str) and arg.startswith("%")
        )

    def _get_def(self, instr):
        # Assuming 'instr' is a TAC object and result is the defined variable
        if (
            isinstance(instr, TAC)
            and instr.result
            and isinstance(instr.result, str)
            and instr.result.startswith("%")
        ):
            return {instr.result}
        return set()


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
    cfg_node3.jump = ("ret", "%0")
    cfg_node3.cjumps = []

    # Create the CFG with all nodes
    fib_cfg = CFG(
        "L0", {"L0": cfg_node0, "L1": cfg_node1, "L2": cfg_node2, "L3": cfg_node3}
    )

    ssa = SSA(fib_cfg)
    print(ssa.transform().cfg)
