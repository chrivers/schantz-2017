#!/usr/bin/python
#encoding=utf-8
q = []
reduce(
    lambda x, y: q.append("20%d	%s" % (16+y,x)) or x + ord(u"Ἕ䈯䘐"[(y>12)+(y>18)]) + x/118,
    range(55),
    0
)
print "\n".join(q)
