#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("usage: %s <file>" % sys.argv[0])
    sys.exit(1)

text = open(filename).read().strip()
line = text.replace("\n", "")
line = re.sub("(?<=\w)[ ]+(?=\w)", "!", line)
#line = re.sub("(?<!\w)[ ]+(?!\w)", "", line)
line = line.replace(" ", "").replace("!", " ")
sys.stdout.write(line)

#print("%s: %6d total, %6d whitespace, %6d non-whitespace (%6d estimated real)" % (filename, len(text), len(text)-len(text2), len(text2), len(text2) + 6))
