#!/usr/bin/env python

import sys
def log(x, *args):
    sys.stderr.write(x % args)
    sys.stderr.write("\n")

X = 0
for Y in range(16, 71):
    print "20%d\t%s" % (Y, X)
    ycmp1 = int(Y > 34)
    ycmp2 = int(Y > 28)
    A = 1000 * (ycmp2 + ycmp1)
    log("%4d: ycmp1=%d ycmp2=%d, A=%d", Y + 2000, ycmp1, ycmp2, A)
    X += A + 7900 * (ycmp2+1)
    X += X / 118
