"""
import sys

f = sys.argv[1]

with open(f, 'r') as handle:
    cnt = 0
    for line in handle:
        if cnt%3 == 0:
            chro =




"""
# 강사님

total = 0

with open("077.bed",'r') as handle:
    for line in handle:
        splitted = line.strip().split("\t")
        start = int(splitted[1])
        end = int(splitted[2])
        total += end - start

print(total)
