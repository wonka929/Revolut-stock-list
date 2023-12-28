import re
import os

with open("list.txt", "a") as ff:
    regex = re.compile(r"[A-Z]{2}\s")
    regex1 = re.compile(r"[A-Z]{3}\s")
    regex2 = re.compile(r"[A-Z]{4}\s")
    regex3 = re.compile(r"[A-Z]{5}\s")
    regex4 = re.compile(r"[A-Z]{2}\n")
    regex5 = re.compile(r"[A-Z]{3}\n")
    regex6 = re.compile(r"[A-Z]{4}\n")
    regex7 = re.compile(r"[A-Z]{5}\n")

    regexs = [regex, regex1, regex2, regex3, regex4, regex5, regex6, regex7]

    with open("output.txt") as f:
        for line in f:
            for regex in regexs:
                result = regex.findall(line)
                if len(result) > 0:
                    ff.write(str(result[0]) + "\n")

    ff.close()

lines_seen = set()  # holds lines already seen
outfile = open("list_final.csv", "w")
outfile.write(r"Name;Ticker" + "\n")
for line in open("list.txt", "r"):
    if line not in lines_seen:  # not a duplicate
        outfile.write(";" + line)
        lines_seen.add(line)

outfile.close()
