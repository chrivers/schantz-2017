SHELL=zsh

clean:
	@rm -frv *.class(N) *~(N) *.exe(N) __pycache__

sizes:
	@./size.py 2017-*.(java|cs|gc2)

check01:
	@javac 2017-01.java
	@./comp.py <(java A)
	@./size.py 2017-01.java
check02:
	@javac 2017-02.java
	@./comp.py <(java A)
	@./size.py 2017-02.java
check03:
	@javac 2017-03.java
	@./comp.py <(java A)
	@./size.py 2017-03.java
check04:
	@javac 2017-04.java
	@./comp.py <(java A)
	@./size.py 2017-04.java
check05:
	@javac 2017-05.java
	@./comp.py <(java A)
	@./size.py 2017-05.java
check06:
	@javac 2017-06.java
	@./comp.py <(java A)
	@./size.py 2017-06.java
check07:
	@mcs 2017-07.cs
	@./comp.py <(./2017-07.exe)
	@./size.py 2017-07.cs
check08:
	@./comp.py <(csharp ./2017-08.cs)
	@./size.py 2017-08.cs
check09:
	@(cd ./gs2 && ./gs2c.py < ../2017-09.gs2 > ../2017-09.gc2)
	@./comp.py <(./gs2/gs2.py 2017-09.gc2)
	@./size.py 2017-09.gc2
