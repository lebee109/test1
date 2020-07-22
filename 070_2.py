"""
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        if splitted[2].startswith("rs"):
            print(splitted[0],splitted[1],splitted[3],splitted[4],splitted[2])
"""


# 강사님 풀이
cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
           header = line.strip().split("\t")
           id_idx = header.index("ID")

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != ".":
            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")

















