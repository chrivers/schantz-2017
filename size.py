#!/usr/bin/env python3
import sys
import minify

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
    text = open(filename,errors='surrogateescape').read()
    extension = filename.split(".")[-1]
    if extension in ("cs", "java", "groovy"):
        text = text.strip()
        text2 = strip_whitespace(text)
        mindesc = "%6d characters (minified)" % len(minify.minify(text))
    else:
        text2 = text
        mindesc = "%6d bytes (binary)" % len(text)
    print("%-15s: %6d total, %6d whitespace, %6d non-whitespace: %s" % (filename, len(text), len(text)-len(text2), len(text2), mindesc))
