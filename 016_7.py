import sys
import gzip

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]}) [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with gzip.open (f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        print(type(line.strip()))
        sys.exit()    # 한줄만 보려고
