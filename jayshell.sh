#!/bin/bash

## Since "jshell" takes a ludicrous 9-18 seconds to start up, we can
## use this script to get the same computation by manually wrapping
## the source in a java interface, and running javac. This gives the
## same semantics, but about 98% faster.

NAME=javatmp_$$
printf "interface $NAME {
  static void printf(String format, Object... args) { System.out.printf(format, args); };
  static void println(String s) { System.out.println(s); }
  static void main(String[]a) { %s }
}" "$(<$1)" > $NAME.java

javac $NAME.java
java $NAME

rm -f $NAME.java $NAME.class
