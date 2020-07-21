import sys
import gzip

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]}) [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with gzip.open (f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
    d={}
    for i in len(f):
        if f[i] in d.keys():
            d(f[i])

