#! /usr/bin/env python3

# --------------------------------------------------------------------
# Requires Python3 >= 3.10

# --------------------------------------------------------------------
import argparse
import os
import subprocess as sp
import sys

from bxlib.bxast import *
from bxlib.bxerrors import Reporter, DefaultReporter
from bxlib.bxparser import Parser
from bxlib.bxmm import MM
from bxlib.bxtychecker import check as tycheck
from bxlib.bxasmgen import AsmGen
from bxlib.bxtac import *
from bxlib.bxcfg import tac2cfg, cfg2tac, uce, jthreading
from bxlib.bxssa import SSA
from bxlib.bxregalloc import *

# ====================================================================
# Parse command line arguments


def parse_args():
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))

    parser.add_argument("input", help="input file (.bx)")

    parser.add_argument(
        "-t",
        "--TAC",
        action="store_true",
        default=False,
        help="Save the TAC code",
    )
    aout = parser.parse_args()

    if os.path.splitext(aout.input)[1].lower() != ".bx":
        parser.error("input filename must end with the .bx extension")

    return aout


# ====================================================================
# Main entry point


def _main():
    args = parse_args()

    try:
        with open(args.input, "r") as stream:
            prgm = stream.read()

    except IOError as e:
        print(f"cannot read input file {args.input}: {e}")
        exit(1)

    reporter = DefaultReporter(source=prgm)
    prgm = Parser(reporter=reporter).parse(prgm)

    if prgm is None:
        exit(1)

    if not tycheck(prgm, reporter=reporter):
        exit(1)

    tac = MM.mm(prgm)

    new_tac = []

    for decl in tac:
        match decl:
            case TACProc(tac=ptac):
                # We here do TAC -> CFG -> JTHREADING -> UCE -> TAC
                # Other CFG-based optimizations should be inserted here
                # cfg = tac2cfg(ptac)
                cfg = uce(jthreading(tac2cfg(ptac)))
                if detect_param_call_cfg(cfg):
                    print("param call detected")
                    decl.tac = cfg2tac(cfg)
                    # print(f"tac: {decl.tac}")
                    continue
                dict_print(cfg.cfg, "Original CFG\n")
                ssa = SSA(cfg, decl.name, decl.arguments)
                ssa.transform()
                print("\n\n\n\n\n")
                dict_print(ssa.ssa.cfg, "AFTER SSA\n")
                print("\n\n\n\n\n")
                alloc_record, stack_size = allocation(
                    ssa.ssa, decl.name, decl.arguments
                )
                cfg = ssa.destruct()
                dict_print(cfg.cfg, "AFTER SSA DESTRUCT\n")

                decl.alloc = alloc_record
                decl.stack_size = stack_size
                decl.tac = cfg2tac(cfg)
                decl.is_alloc = True
                new_tac.append(decl)
                print(f"stack_size: {decl.stack_size}")
                print(f"alloc: {decl.alloc}")
                print(f"proc @{decl.name}({', '.join(decl.arguments)}):")

    abk = AsmGen.get_backend("x64-linux")
    asm = abk.lower(tac)

    basename = os.path.splitext(args.input)[0]
    basename = os.path.basename(basename)

    try:
        with open(f"{basename}.s", "w") as stream:
            stream.write(asm)

        if args.TAC:
            with open(f"{basename}.tac", "w") as stream:
                stream.write(new_tac.__repr__())

    except IOError as e:
        print(f"cannot write outpout file {args.output}: {e}")
        exit(1)

    bxruntime = os.path.join(os.path.dirname(__file__), "bxlib", "bxruntime.c")

    sp.call(["gcc", "-g", "-c", "-o", f"{basename}.o", f"{basename}.s"])
    sp.call(["gcc", "-g", "-o", f"{basename}.exe", bxruntime, f"{basename}.o"])


# --------------------------------------------------------------------
if __name__ == "__main__":
    _main()
