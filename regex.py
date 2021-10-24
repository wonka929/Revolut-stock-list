import re
import os

with open("list.txt", "a") as ff:

    regex = re.compile(r'[A-Z]{4}')

    with open("output.txt") as f:
        for line in f:
            result = regex.findall(line)
            if len(result)>0:
                ff.write(str(result[0]) + '\n')

    regex1 = re.compile(r'^[A-Z]{3}\s')

    with open("output.txt") as f:
        for line in f:
            result = regex1.findall(line)
            if len(result)>0:
                ff.write(str(result[0]) + '\n')

    regex2 = re.compile(r'^[A-Z]{2}\s')

    with open("output.txt") as f:
        for line in f:
            result = regex2.findall(line)
            if len(result)>0:
                ff.write(str(result[0]) + '\n')
                print(result[0])

    regex3 = re.compile(r'^[A-Z]{1}\s')

    with open("output.txt") as f:
        for line in f:
            result = regex3.findall(line)
            if len(result)>0:
                ff.write(str(result[0]) + '\n')

    regex4 = re.compile(r'^[A-Z]{5}\s')

    with open("output.txt") as f:
        for line in f:
            result = regex4.findall(line)
            if len(result)>0:
                ff.write(str(result[0]) + '\n')

lines_seen = set() # holds lines already seen
outfile = open("list_final.csv", "w")
outfile.write(r'Name;Ticker' + '\n')
for line in open("list.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(';' + line)
        lines_seen.add(line)
        
outfile.close()
