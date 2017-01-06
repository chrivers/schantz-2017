SHELL=zsh

clean:
	@rm -fv *.class(N) *~(N)

check01:
	@javac 2017-01.java
	@./comp.py <(java A)
check02:
	@javac 2017-02.java
	@./comp.py <(java A)
check03:
	@javac 2017-03.java
	@./comp.py <(java A)
check04:
	@javac 2017-04.java
	@./comp.py <(java A)
check05:
	@javac 2017-05.java
	@./comp.py <(java A)
check06:
	@javac 2017-06.java
	@./comp.py <(java A)
	@./size.py 2017-06.java
