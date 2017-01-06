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

max_err = 0

for i, ref in enumerate(refs if len(refs) >= len(vals) else vals):
    val = vals[i]
    diff = ref - val
    if diff == 0.0:
        desc = 0.0
    else:
        desc = diff / ref * 100.0
    max_err = max(max_err, abs(desc))
    print("%d: %12.4f vs ref %12.4f: diff %12.4f (%8.4f%% error)" % (2016 + i, val, ref, diff, desc))

print("-"*80)
max_err_level = 0.1
if len(refs) != len(vals):
    print("Wrong number of values (%d actual vs %d expected)" % (len(vals), len(refs)))
else:
    print("Correct number of values")
print("max error: %.4f%%" % max_err)
print("error level: %.2f%%" % (abs(max_err / max_err_level) * 100))
print("-"*80)
