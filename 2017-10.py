#!/usr/bin/env python

import sys
def log(x, *args):
    sys.stderr.write(x % args)
    sys.stderr.write("\n")

#  7893 -  7907
# 16766 - 16835
# 17773 - 17822

D = [(13, 7900), (6, 16800), (36, 17800)]

Y = 2016
X = 0
for c, v in D:
    for _ in range(c):
        print "%d\t%s" % (Y, X)
        Y += 1
        X += v
        X += X / 118
