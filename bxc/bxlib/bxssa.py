from .bxcfg import *

class SSA:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ssa = None
        self.version_counter = {}
        
    def add_phi_functions(self):
        pass
    
    def _liveness_analysis(self):
        live_in = {block_label: self._get_use(block) for block_label, block in self.cfg.cfg.items()}
        live_out = {block_label: set() for block_label in self.cfg.cfg.keys()}

        changed = True
        while changed:
            changed = False
            for block_label, block in self.cfg.cfg.items():
                old_live_in = live_in[block_label].copy()

                # Calculate live_out for the block using live_in of successors
                live_out[block_label] = set()
                if block.jump and block.jump[0] != 'ret':  # Ensure we handle 'ret' correctly
                    live_out[block_label].update(live_in.get(block.jump[1], set()))
                for _, (_, target) in block.cjumps:
                    live_out[block_label].update(live_in.get(target, set()))

                # Calculate live_in by union of live_out of the block and use - def of the block
                live_in[block_label] = live_out[block_label].union(self._get_use(block) - self._get_def(block))

                # Check if there are any changes to the live_in set
                if live_in[block_label] != old_live_in:
                    changed = True

        return live_in

    def _get_use(self, block) -> set:
        # Collect the use-set of the block
        use_set = set()
        for instruction in block.body:
            # Assuming arguments are a list of variables and constants, we only want the variables
            use_set.update(arg for arg in instruction.arguments if isinstance(arg, str) and arg.startswith('%'))
        return use_set

    def _get_def(self, block) -> set:
        # Collect the def-set of the block
        def_set = set()
        for instruction in block.body:
            # Assuming result is a variable name, not a constant or label
            if instruction.result and isinstance(instruction.result, str) and instruction.result.startswith('%'):
                def_set.add(instruction.result)
        return def_set
        
    def _is_use_instruction(self, instruction):
        # Implement logic to determine if an instruction uses a variable
        pass
        
if __name__ == "__main__":
    # Create the CFGNode for L0
    cfg_node0 = CFGNode()
    cfg_node0.label = "L0"
    cfg_node0.body = [TAC("const", [0], "%0"),
                    TAC("const", [1], "%1"),
                    TAC("const", [1], "%2")]
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
    cfg_node2.body = [TAC("sub", ["%n", "%2"], "%n"),
                    TAC("add", ["%0", "%1"], "%3"),
                    TAC("copy", ["%1"], "%0"),
                    TAC("copy", ["%3"], "%1")]
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
    print(ssa._liveness_analysis())
        
    
    
    

       

