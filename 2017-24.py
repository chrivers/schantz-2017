#!/usr/bin/python
#encoding=utf-8
def foo(q, y):
    return (q[0] + "20%d	%s\n" % (16+y,q[1])), q[1] + ord(u"Ἕ䈯䘐"[(y>12)+(y>18)]) + q[1]/118

print reduce(
    foo,
    range(55),
    ("", 0)
)[0],
