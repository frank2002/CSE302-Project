import copy
import time

from .bxcfg import *
from .union_find import UnionFind


class SSA:
    def __init__(self, cfg, name: str = None, arguments: list[str] = None):
        self.cfg = cfg
        self.ssa = None
        self.all_instructions = []
        self.instr_dict = {}
        self.version_counter = 0
        self.name = name
        self.arguments = arguments

    def transform(self):
        self._add_phi_functions()
        self._update_phi_functions()

        print(f"before elimination, {self.cfg.cfg}")

        is_changed = True
        uf = UnionFind()
        while is_changed:
            is_changed = False

            changed1 = self.null_choice_elimination()
            changed2 = self.rename_elimination(uf)
            # print(f"after, {self.cfg.cfg}\n\n\n\n")

            is_changed = changed1 or changed2

        self.ssa = self.cfg
        return self.ssa

    def destruct(self) -> CFG:
        if not self.ssa:
            raise Exception("SSA has not been built yet")

        # Adding COPY instructions to end of blocks

        cfg = copy.deepcopy(self.ssa)

        for block_label, block in cfg.cfg.items():
            for variable, phi_functions in block.phi_functions.items():
                for phi_function in phi_functions:
                    if phi_function[0] == "@":
                        variable2 = phi_function.split(".")[1]
                        self.ssa.cfg[block_label].body.insert(
                            0, TAC("copy", [variable2], variable)
                        )
                        continue

                    block_label2, variable2 = phi_function

                    self.ssa.cfg[block_label2].body.append(
                        TAC("copy", [variable2], variable)
                    )
                self.ssa.cfg[block_label].phi_functions.pop(variable)

        return self.ssa

    def null_choice_elimination(self) -> bool:
        is_changed = False
        for block_label, block in self.cfg.cfg.items():
            phi_functions = block.phi_functions
            new_phi_functions = phi_functions.copy()
            for variable, phi_function in phi_functions.items():
                if len(phi_function) == 1 and phi_function[0][0] == "@":
                    continue
                version = variable.split(".")[1]
                is_same = True
                for block_label2, variable2 in phi_function:
                    # print(f"variable2: {variable2}")
                    if "." not in variable2:
                        version2 = 0
                    else:
                        version2 = variable2.split(".")[1]
                    if version != version2:
                        is_same = False
                        break
                if is_same:
                    new_phi_functions.pop(variable)
                    is_changed = True
                    # print(f"eliminate: {variable} : {phi_function}")
            self.cfg.cfg[block_label].phi_functions = new_phi_functions

        return is_changed

    def rename_elimination(self, uf) -> bool:
        # uf = UnionFind()
        is_changed = False

        for block_label, block in self.cfg.cfg.items():
            new_phi_functions = block.phi_functions.copy()
            for variable, phi_function in block.phi_functions.items():
                v = None
                is_qualified = True
                if len(phi_function) == 1 and phi_function[0][0] == "@":
                    new_variable = phi_function[0].split(".")[1]
                    # print(f"new_variable: {(block_label, new_variable), variable}")
                    uf.union((block_label, new_variable), variable)
                    # print(f"new_phi_functions: {new_phi_functions}")
                    new_phi_functions.pop(variable)
                    is_changed = True

                elif len(phi_function) == 1:
                    # print(
                    #     f" Union {phi_function[0][0]} {phi_function[0][1]} <- {variable}"
                    # )
                    uf.union(
                        (phi_function[0][0], phi_function[0][1]),
                        variable,
                    )
                    is_changed = True
                    new_phi_functions.pop(variable)
                else:
                    for block_label2, variable2 in phi_function:
                        if variable2 == variable:
                            continue
                        elif not v:
                            v = variable2
                        else:
                            if v != variable2:
                                is_qualified = False
                                break
                    if is_qualified:
                        uf.union((block_label2, v), variable)
                        # print(f" Union {block_label2} {v} <- {variable}")
                        new_phi_functions.pop(variable)
                        is_changed = True

            self.cfg.cfg[block_label].phi_functions = new_phi_functions

        for block_label, block in self.cfg.cfg.items():
            for instr in block.body:
                # print(f"instr: {instr}")
                new_arguments = []
                for argument in instr.arguments:
                    # print(f"argument: {argument}")
                    if isinstance(argument, str) and argument.startswith("%"):
                        temp = uf.find(argument)
                        # print(f" find({ argument} -> {temp})")
                        if len(temp) == 2 and isinstance(temp, tuple):
                            new_arguments.append(uf.find(argument)[1])
                        else:
                            new_arguments.append(argument)
                    else:
                        new_arguments.append(argument)
                if instr.arguments != new_arguments:
                    is_changed = True

                # print(f"old: {instr.arguments} -> new: {new_arguments}")
                instr.arguments = new_arguments

                # if isinstance(instr.result, str) and instr.result.startswith("%"):
                #     tmp = uf.find(instr.result)[1]

                #     if instr.result != tmp:
                #         is_changed = True
                #     instr.result = tmp

            for index, instr in enumerate(reversed(block.cjumps)):
                new_arguments = []
                for argument in instr[1]:
                    if isinstance(argument, str) and argument.startswith("%"):
                        temp = uf.find(argument)
                        if len(temp) == 2 and isinstance(temp, tuple):
                            new_arguments.append(temp[1])
                        else:
                            new_arguments.append(argument)
                    else:
                        new_arguments.append(argument)
                if instr[1] != new_arguments:
                    is_changed = True
                self.cfg.cfg[block_label].cjumps[len(block.cjumps) - 1 - index] = (
                    instr[0],
                    new_arguments,
                )

            if block.jump:
                if block.jump[0] == "ret" and block.jump[1] and len(block.jump[1]) == 1:
                    variable = block.jump[1][0]
                    if isinstance(variable, str) and variable.startswith("%"):
                        # print(f"find {(block_label, variable)} -> {uf.find( variable)}")
                        temp = uf.find(variable)
                        if (
                            len(temp) == 2
                            and temp[1] != variable
                            and isinstance(temp, tuple)
                        ):
                            is_changed = True
                            self.cfg.cfg[block_label].jump = (
                                "ret",
                                [temp[1]],
                            )
                        else:
                            self.cfg.cfg[block_label].jump = ("ret", [variable])
                    else:
                        self.cfg.cfg[block_label].jump = ("ret", [variable])

            # for variable, phi_function in block.phi_functions.copy().items():
            #     print(f"phi_function: {variable}:{phi_function}")
            #     if len(phi_function) == 1 and phi_function[0][0] == "@":
            #         continue
            #     if isinstance(variable, str) and variable.startswith("%"):
            #         print(f"old var: {variable} -> {uf.find(variable)}")
            #         new_variable = uf.find(variable)[1]
            #         if variable != new_variable:
            #             is_changed = True
            #             self.cfg.cfg[block_label].phi_functions[
            #                 new_variable
            #             ] = phi_function
            #             self.cfg.cfg[block_label].phi_functions.pop(variable)

            for variable, phi_function in block.phi_functions.items():
                new_phi_functions = []
                if len(phi_function) == 1 and phi_function[0][0] == "@":
                    continue
                for block_label2, variable2 in phi_function:
                    if isinstance(variable2, str) and variable2.startswith("%"):
                        # print(f"find {variable2} -> {uf.find(variable2)}")
                        temp = uf.find(variable2)
                        if len(temp) == 2 and isinstance(temp, tuple):
                            new_phi_functions.append(uf.find(variable2))
                        else:
                            new_phi_functions.append((block_label2, variable2))
                    else:
                        new_phi_functions.append((block_label2, variable2))
                if phi_function != new_phi_functions:
                    is_changed = True
                    # print(f"Change: {variable} : {phi_function} -> {new_phi_functions}")
                self.cfg.cfg[block_label].phi_functions[variable] = new_phi_functions

        return is_changed

    def _get_new_variable(self, variable: str):
        self.version_counter += 1
        return f"{variable}.{self.version_counter}"

    def _add_phi_functions(self):
        # livein analysis

        block_liveness = self._liveness_analysis()
        # print(f"block_liveness: {block_liveness}")

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
                if block.jump[0] == "ret" and block.jump[1] and len(block.jump[1]) == 1:
                    is_found = False
                    variable = block.jump[1][0]
                    if isinstance(variable, str) and variable.startswith("%"):
                        for index2, instr2 in enumerate(reversed(block.body)):
                            if variable == instr2.result.split(".")[0]:
                                self.cfg.cfg[block_label].jump = (
                                    "ret",
                                    [instr2.result],
                                )

                                is_found = True
                                break
                        if not is_found:
                            for key in block.phi_functions:
                                if variable == key.split(".")[0]:
                                    self.cfg.cfg[block_label].jump = (
                                        "ret",
                                        [key],
                                    )
                                    break
                    else:
                        self.cfg.cfg[block_label].jump = ("ret", [instr2.result])

    def _update_phi_functions(self):
        for block_label, block in self.cfg.cfg.items():
            predecessor_blocks = self._get_predecessor_blocks(block_label)

            if not predecessor_blocks:
                for variable, phi_functions in block.phi_functions.items():
                    # print(f"@{self.name}.{variable}")

                    self.cfg.cfg[block_label].phi_functions[variable].append(
                        f"@{self.name}.{variable.split('.')[0]}"
                    )

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
            if key.startswith(variable_prefix + "."):
                defined_variables[variable] = key

        for instr in block.body:
            if instr.result.startswith(variable_prefix + "."):
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
                if block.jump[0] == "ret" and block.jump[1] and len(block.jump[1]) == 1:
                    livein[index] = set([block.jump[1][0]])
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

            elif (
                current_block.jump[0] == "ret"
                and current_block.jump[1]
                and len(current_block.jump[1]) == 1
            ):
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
