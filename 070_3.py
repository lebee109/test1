
# 내풀이  14개 나와야 되는데 15개 나옴 => ALT도 나와서
cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
           header = line.strip().split("\t")
           alt_idx = header.index("ALT")

        splitted = line.strip().split("\t")
        alt = splitted[4]
        ltmp = splitted[4].split(',')
        cnt += len(ltmp)
print(cnt)
"""
# 강사님
cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        alts = splitted[4].split(',')   # , 없는 애들도 그냥 리스트로 나옴(쓰기전 확인 하기)
        for alt in alts:
            cnt += 1
print(cnt)
"""












