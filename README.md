# Schantz Challenge 2017

Like last year, Schantz A/S is holding a code golf competition. This
repository contains my research notes, failed attempts, experiments,
as well as the 2 programs that won first place in each of the 2
categories.

Challenge: Write the shortest possible program that outputs the yearly
reserves for Santa’s pension until he has enough to retire and buy the
island of Kiatak (> 1.000.000 DKK).

The exact rules are described in the [LinkedIn
announcement](https://www.linkedin.com/pulse/schantz-new-years-coding-challenge-2017-espen-højsgaard).

There are 2 categories:

 - Category 1: Only C# and Java are allowed

 - Category 2: Anything goes, except languages invented for this challenge.

## Give it to me straight, doc!

Ok, ok. I get it, you want to cut to the chase. The 2 winning entries are:

 - Category 1: [2017-19.cs](2017-19.cs) (66 characeters)
 - Category 2: [2017-17.gs2s](2017-17.gs2s) (assembles to `2017-17.gs2`) (33 characeters)

## Tools of the trade

### Checking

Checking the validity of the work is important. To this end, I made an
improved validation tool, that not only validates correctness, but
also displays deviation from the reference solution.

To run a check on a solution, run `make checkXX`, for example `make
check17` or `make check19` to check the winning entries.

### Size calculation

Type `make size` to see an overview of all sizes, like so:

```
2017-08.cs     :    153 total,     77 whitespace,     76 non-whitespace:     78 characters (minified)
2017-09.gs2    :     39 total,      0 whitespace,     39 non-whitespace:     39 bytes (binary)
...
2017-16.gs2    :     39 total,      0 whitespace,     39 non-whitespace:     39 bytes (binary)
2017-17.gs2    :     33 total,      0 whitespace,     33 non-whitespace:     33 bytes (binary)
2017-18.java   :    101 total,     37 whitespace,     64 non-whitespace:     65 characters (minified)
2017-19.cs     :     81 total,     17 whitespace,     64 non-whitespace:     66 characters (minified)
2017-20.jshell :     97 total,     16 whitespace,     81 non-whitespace:     83 characters (minified)
2017-21.py     :     89 total,      0 whitespace,     89 non-whitespace:     89 chars (raw text)
...
```

Type `make checkXX` to see the size of a specific entry.
