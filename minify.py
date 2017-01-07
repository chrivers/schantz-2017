#!/usr/bin/env python3
import sys
import re

def minify(text):
    line = text.replace("\n", "")
    line = re.sub("(?<=\w)[ ]+(?=\w)", "\x00", line)
    line = line.replace(" ", "").replace("\x00", " ")
    return line

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        text = open(filename).read().strip()
        line = minify(text)
        sys.stdout.write(line)
    else:
        print("usage: %s <file>" % sys.argv[0])
        sys.exit(1)
