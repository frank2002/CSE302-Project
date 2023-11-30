from .bxcfg import *

class SSA:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ssa = self._ssa()
        self.version_counter = {}
    
    def _ssa(self):
        ssa = {}
        for block in self.cfg.cfg.values():
            for tac in block.body:
                if tac[0] == 'phi':
                    ssa[tac[1]] = tac[2]
        return ssa
    

       

