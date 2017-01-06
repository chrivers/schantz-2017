#!/usr/bin/env python3
import sys

def strip_whitespace(text):
    return text \
        .replace(" ", "") \
        .replace("\t", "") \
        .replace("\n", "") \
        .replace("\r", "") \
        .replace("\f", "") \
        .replace("\v", "")

if len(sys.argv) > 1:
    filenames = sys.argv[1:]
else:
    print("usage: %s <file>" % sys.argv[0])
    sys.exit(1)

for filename in filenames:
    text = open(filename).read().strip()
    text2 = strip_whitespace(text)

    print("%s: %6d total, %6d whitespace, %6d non-whitespace (%6d estimated real)" % (filename, len(text), len(text)-len(text2), len(text2), len(text2) + 5))
