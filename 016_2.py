import sys

f = sys.argv[1]

with open(f,'r') as handle:
    for line in handle:
        a =0
        t =0
        g =0
        c =0
        for i in range(len(line)):
            if line[i] == A:
                a += 1
            elif line[i] == T:
                t += 1
            elif line[i] == G:
                g += 1
            else:
                c +=1
