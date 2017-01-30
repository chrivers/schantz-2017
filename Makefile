SHELL=zsh

clean:
	@rm -frv *.class(N) *~(N) *.exe(N) __pycache__ 2017-*.txt(N) 2017-22

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
2017-09.gs2: 2017-09.gs2s
	@cd ./gs2 && ./gs2c.py < ../2017-09.gs2s > ../2017-09.gs2
2017-16.gs2: 2017-16.gs2s
	@cd ./gs2 && ./gs2c.py < ../2017-16.gs2s > ../2017-16.gs2
2017-17.gs2: 2017-17.gs2s
	@cd ./gs2 && ./gs2c.py < ../2017-17.gs2s > ../2017-17.gs2
2017-22: 2017-22.rs
	@rustc 2017-22.rs -o 2017-22

compile01: A.class
compile02: B.class
compile03: C.class
compile04: D.class
compile05: E.class
compile06: F.class
compile07: 2017-07.exe
compile08:
compile09: 2017-09.gs2
compile10:
compile11:
compile12:
compile13:
compile14:
compile15:
compile16: 2017-16.gs2
compile17: 2017-17.gs2
compile18:
compile19:
compile20:
compile21:
compile22: 2017-22
compile23:
compile: compile01 compile02 compile03 compile04 compile05 compile06 compile07 compile08 compile09 compile10 compile11 compile12 compile13 compile14 compile15 compile16 compile17 compile18 compile19 compile20 compile21 compile22 compile23

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
	@cd gs2 && ./gs2.py ../2017-09.gs2 > ../2017-09.txt
run10: compile10
	@./2017-10.py > 2017-10.txt
run11: compile11
	@bsh ./2017-11.java > 2017-11.txt
run12: compile12
	@groovy ./2017-12.groovy > 2017-12.txt
run13: compile13
	@groovy ./2017-13.groovy > 2017-13.txt
run14: compile14
	@groovy ./2017-14.groovy > 2017-14.txt
run15: compile15
	@groovy ./2017-15.groovy > 2017-15.txt
run16: compile16
	@cd gs2 && ./gs2.py ../2017-16.gs2 > ../2017-16.txt
run17: compile17
	@cd gs2 && ./gs2.py ../2017-17.gs2 > ../2017-17.txt
run18: compile18
	@bsh ./2017-18.java > 2017-18.txt
run19: compile19
	@csharp ./2017-19.cs > 2017-19.txt
run20: compile20
	@./jayshell.sh ./2017-20.jshell > 2017-20.txt
run21: compile21
	@python3 2017-21.py > 2017-21.txt
run22: compile22
	@./2017-22 > 2017-22.txt
run23: compile23
	@./jayshell.sh ./2017-23.jshell > 2017-23.txt
run: run01 run02 run03 run04 run05 run06 run07 run08 run09 run10 run11 run12 run13 run14 run15 run16 run17 run18 run19 run20 run21 run22 run23

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
comp12:
	@./comp.py 2017-12.txt
comp13:
	@./comp.py 2017-13.txt
comp14:
	@./comp.py 2017-14.txt
comp15:
	@./comp.py 2017-15.txt
comp16:
	@./comp.py 2017-16.txt
comp17:
	@./comp.py 2017-17.txt
comp18:
	@./comp.py 2017-18.txt
comp19:
	@./comp.py 2017-19.txt
comp20:
	@./comp.py 2017-20.txt
comp21:
	@./comp.py 2017-21.txt
comp22:
	@./comp.py 2017-22.txt
comp23:
	@./comp.py 2017-23.txt
comp: comp01 comp02 comp03 comp04 comp05 comp06 comp07 comp08 comp09 comp10 comp11 comp12 comp13 comp14 comp15 comp16 comp17 comp18 comp19 comp20 comp21 comp22 comp23

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
	@./size.py 2017-09.gs2
size10:
	@./size.py 2017-10.py
size11:
	@./size.py 2017-11.java
size12:
	@./size.py 2017-12.groovy
size13:
	@./size.py 2017-13.groovy
size14:
	@./size.py 2017-14.groovy
size15:
	@./size.py 2017-15.groovy
size16:
	@./size.py 2017-16.gs2
size17:
	@./size.py 2017-17.gs2
size18:
	@./size.py 2017-18.java
size19:
	@./size.py 2017-19.cs
size20:
	@./size.py 2017-20.jshell
size21:
	@./size.py 2017-21.py
size22:
	@./size.py 2017-22.rs
size23:
	@./size.py 2017-23.jshell
size: compile09 compile16 compile17
	@./size.py 2017-*.(java|cs|gs2|py|groovy|jshell)

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
check12: compile12 run12 comp12 size12
check13: compile13 run13 comp13 size13
check14: compile14 run14 comp14 size14
check15: compile15 run15 comp15 size15
check16: compile16 run16 comp16 size16
check17: compile17 run17 comp17 size17
check18: compile18 run18 comp18 size18
check19: compile19 run19 comp19 size19
check20: compile20 run20 comp20 size20
check21: compile21 run21 comp21 size21
check22: compile22 run22 comp22 size22
check23: compile23 run23 comp23 size23
