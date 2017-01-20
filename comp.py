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

def color(text, color, reset_color=Style.RESET_ALL):
    return "%s%s%s" % (color, text, reset_color)

def color_result(text, cond, ok_color=Style.BRIGHT + Fore.GREEN, fail_color=Style.BRIGHT + Fore.RED, reset_color=Style.RESET_ALL):
    return color(text, ok_color if cond else fail_color, reset_color)

def check(res):
    return color_result("OK" if res else "FAIL", res)

refs = parse(open(REFERENCE))
comp = parse(fileinput.input())

max_err = 0

wrong_years = 0
max_err_level = 0.1

def clamp(_min, x, _max):
    return max(_min, min(x, _max))

def error_bar(value, max_value, ok_color=Style.BRIGHT + Fore.GREEN, fail_color=Style.BRIGHT + Fore.RED, reset_color=Style.RESET_ALL, width=10):
    pct = value / max_value

    color = ok_color if abs(value) <= abs(max_value) else fail_color
    return "|%s%10s%s|%s%10s%s|%s%-10s%s|%s%-10s%s|" % (
        color, "X" * int(-clamp(-1, pct + 1, 0) * width), reset_color,
        color, "*" * int(-clamp(-1, pct,     0) * width), reset_color,
        color, "*" * int( clamp( 0, pct,     1) * width), reset_color,
        color, "X" * int( clamp( 0, pct - 1, 1) * width), reset_color,
    )

for i, ref in enumerate(zip(refs, comp)):
    ref_year, ref_val = ref[0]
    cmp_year, cmp_val = ref[1]
    diff = cmp_val - ref_val
    if ref_year != cmp_year:
        wrong_years += 1
    err = diff / (ref_val or 1) * 100.0

    max_err = max(max_err, abs(err))
    bar = error_bar(err, max_err_level)
    print(
        "%d: %12.4f vs ref %12.4f: diff %12.4f (%s error) %s" %
        (
            2016 + i,
            cmp_val,
            ref_val,
            diff,
            color_result("%8.3f%%" % (err / max_err_level * 100.0), abs(err) < max_err_level),
            bar
        )
    )

print("-"*80)
print("Number of incorrect years [%d] [%s]" % (wrong_years, check(wrong_years == 0)))
print("Number of values [%d == %d] [%s]" % (len(comp), len(refs), check(len(comp) == len(refs))))
print("max error: %.4f%%" % max_err)
print("error level: %.2f%% [%s]" % (abs(max_err / max_err_level) * 100, check(abs(max_err) < max_err_level)))
print("-"*80)
