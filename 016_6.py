import sys

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]) [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with open (f,'r') as handle:
    for line in handle:
        print(line.strip())

