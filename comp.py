#!/usr/bin/env python3

import sys
import fileinput
from colorama import init as colorama_init, Fore, Back, Style
colorama_init()

REFERENCE = "santas-pension-projection.txt"

def parse(fd):
    vals = []
    for line in fd:
        year, amount = line.rstrip().split("\t")
        vals.append((float(year), float(amount)))
    return vals

def check(res):
    if res:
        return "%sOK%s" % (Style.BRIGHT + Fore.GREEN, Style.RESET_ALL)
    else:
        return "%sFAIL%s" % (Style.BRIGHT + Fore.RED, Style.RESET_ALL)

refs = parse(open(REFERENCE))
comp = parse(fileinput.input())

max_err = 0

for i, ref in enumerate(zip(refs, comp)):
    ref_year, ref_val = ref[0]
    cmp_year, cmp_val = ref[1]
    diff = ref_val - cmp_val
    if diff == 0.0:
        desc = 0.0
    else:
        desc = diff / ref_val * 100.0
    max_err = max(max_err, abs(desc))
    print("%d: %12.4f vs ref %12.4f: diff %12.4f (%8.4f%% error)" % (2016 + i, cmp_val, ref_val, diff, desc))

print("-"*80)
max_err_level = 0.1
print("Number of values [%d == %d] [%s]" % (len(comp), len(refs), check(len(comp) == len(refs))))
print("max error: %.4f%%" % max_err)
print("error level: %.2f%%" % (abs(max_err / max_err_level) * 100))
print("-"*80)
