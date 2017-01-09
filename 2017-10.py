#!/usr/bin/env python
X = 0
for Y in range(16, 71):
    print "20%d\t%s" % (Y, X)
    if Y > 28:
        X += (Y / 35 * 1024) + 8864
    X += 7904
    X += X / 118

