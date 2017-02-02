#!/usr/bin/python
#encoding=utf-8
Z=0
print reduce(lambda q,y:(q[0]+"20%d	%s\n"%(16+y,q[1]),q[1]+ord(u"Ἕ䈯䘐"[(y>12)+(y>18)])+q[1]/118),range(55),("",0))[0],
