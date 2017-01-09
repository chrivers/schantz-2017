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

def color_result(text, cond, ok_color=Style.BRIGHT + Fore.GREEN, fail_color=Style.BRIGHT + Fore.RED, reset_color=Style.RESET_ALL):
    return "%s%s%s" % (ok_color if cond else fail_color, text, reset_color)

def check(res):
    return color_result("OK" if res else "FAIL", res)

refs = parse(open(REFERENCE))
comp = parse(fileinput.input())

max_err = 0

wrong_years = 0
max_err_level = 0.1

for i, ref in enumerate(zip(refs, comp)):
    ref_year, ref_val = ref[0]
    cmp_year, cmp_val = ref[1]
    diff = ref_val - cmp_val
    if ref_year != cmp_year:
        wrong_years += 1
    if diff == 0.0:
        desc = 0.0
    else:
        desc = diff / ref_val * 100.0
    max_err = max(max_err, abs(desc))
    if abs(desc) < max_err_level:
        num_good = abs(desc) / max_err_level * 10
        num_bad  = 0
    else:
        num_good = 10
        num_bad = (abs(desc) - max_err_level) / max_err_level * 10
    bar = color_result("*" * int(num_good), True) + color_result("*" * int(num_bad), False)
    print("%d: %12.4f vs ref %12.4f: diff %12.4f (%s error)%s" % (2016 + i, cmp_val, ref_val, diff, color_result("%8.4f%%" % -desc, abs(desc) < max_err_level), bar))

print("-"*80)
print("Number of incorrect years [%d] [%s]" % (wrong_years, check(wrong_years == 0)))
print("Number of values [%d == %d] [%s]" % (len(comp), len(refs), check(len(comp) == len(refs))))
print("max error: %.4f%%" % max_err)
print("error level: %.2f%% [%s]" % (abs(max_err / max_err_level) * 100, check(abs(max_err) < max_err_level)))
print("-"*80)
