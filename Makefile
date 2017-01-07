SHELL=zsh

clean:
	@rm -frv *.class(N) *~(N) *.exe(N) __pycache__

sizes:
	@./size.py 2017-*.(java|cs)

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
