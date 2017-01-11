SHELL=zsh

clean:
	@rm -frv *.class(N) *~(N) *.exe(N) __pycache__ 2017-09.gc2 2017-*.txt(N)

A.class:
	@javac 2017-01.java
B.class:
	@javac 2017-02.java
C.class:
	@javac 2017-03.java
D.class:
	@javac 2017-04.java
E.class:
	@javac 2017-05.java
F.class:
	@javac 2017-06.java
2017-07.exe:
	@mcs 2017-07.cs
2017-09.gc2:
	@cd ./gs2 && ./gs2c.py < ../2017-09.gs2 > ../2017-09.gc2

compile01: A.class
compile02: B.class
compile03: C.class
compile04: D.class
compile05: E.class
compile06: F.class
compile07: 2017-07.exe
compile08:
compile09: 2017-09.gc2
compile10:
compile11:
compiles: compile01 compile02 compile03 compile04 compile05 compile06 compile07 compile08 compile09 compile10 compile11

run01: compile01
	@java A > 2017-01.txt
run02: compile02
	@java B > 2017-02.txt
run03: compile03
	@java C > 2017-03.txt
run04: compile04
	@java D > 2017-04.txt
run05: compile05
	@java E > 2017-05.txt
run06: compile06
	@java F > 2017-06.txt
run07: compile07
	@./2017-07.exe > 2017-07.txt
run08: compile08
	@csharp ./2017-08.cs > 2017-08.txt
run09: compile09
	@cd gs2 && ./gs2.py ../2017-09.gc2 > ../2017-09.txt
run10: compile10
	@./2017-10.py > 2017-10.txt
run11: compile11
	@bsh ./2017-11.java > 2017-11.txt

comp01:
	@./comp.py 2017-01.txt
comp02:
	@./comp.py 2017-02.txt
comp03:
	@./comp.py 2017-03.txt
comp04:
	@./comp.py 2017-04.txt
comp05:
	@./comp.py 2017-05.txt
comp06:
	@./comp.py 2017-06.txt
comp07:
	@./comp.py 2017-07.txt
comp08:
	@./comp.py 2017-08.txt
comp09:
	@./comp.py 2017-09.txt
comp10:
	@./comp.py 2017-10.txt
comp11:
	@./comp.py 2017-11.txt

size01:
	@./size.py 2017-01.java
size02:
	@./size.py 2017-02.java
size03:
	@./size.py 2017-03.java
size04:
	@./size.py 2017-04.java
size05:
	@./size.py 2017-05.java
size06:
	@./size.py 2017-06.java
size07:
	@./size.py 2017-07.cs
size08:
	@./size.py 2017-08.cs
size09:
	@./size.py 2017-09.gc2
size10:
	@./size.py 2017-10.py
size11:
	@./size.py 2017-11.java
sizes: compile09
	@./size.py 2017-*.(java|cs|gc2|py)

check01: compile01 run01 comp01 size01
check02: compile02 run02 comp02 size02
check03: compile03 run03 comp03 size03
check04: compile04 run04 comp04 size04
check05: compile05 run05 comp05 size05
check06: compile06 run06 comp06 size06
check07: compile07 run07 comp07 size07
check08: compile08 run08 comp08 size08
check09: compile09 run09 comp09 size09
check10: compile10 run10 comp10 size10
check11: compile11 run11 comp11 size11
