#!/usr/bin/env python
X = 0
for Y in range(16, 71):
    print "20%d\t%s" % (Y, X)
    X += ((1000 * ((Y > 34)+1)) + 7900) * (Y > 28)
    X += 7900
    X += X / 118

