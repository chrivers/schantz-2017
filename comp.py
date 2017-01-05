#!/usr/bin/env python3

import sys
import fileinput

REFERENCE = "santas-pension-projection.txt"

def parse(fd):
    vals = []
    for line in fd:
        year, amount = line.rstrip().split("\t")
        vals.append(float(amount))
    return vals

refs = parse(open(REFERENCE))
vals = parse(fileinput.input())

if len(refs) != len(vals):
    print("Wrong number of values (%d actual vs %d expected)" % (len(vals), len(refs)))
#    sys.exit(1)

for i, ref in enumerate(refs):
    val = vals[i]
    diff = ref - val
    if diff == 0.0:
        desc = 0.0
    else:
        desc = diff / ref * 100.0
    print("%d: %12.4f vs ref %12.4f: diff %12.4f (%8.4f%% error)" % (2016 + i, val, ref, diff, desc))
