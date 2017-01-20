#!/usr/bin/env python

import sys
def log(x, *args):
    sys.stderr.write(x % args)
    sys.stderr.write("\n")

X = 0
for Y in range(16, 71):
    print "20%d\t%s" % (Y, X)
    c = cmp((Y - 29) / 6, 0) + 1
    A = 1000 * c
    log("%4d: c %d | A %4d", Y + 2000, c, A)
    X += A
    X += 7900 * (cmp(c, 0)+1)
    X += X / 118
