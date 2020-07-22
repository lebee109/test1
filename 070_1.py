# PASS가 여섯번째 칼럼에 있음
# split으로 나눠서 6이 PASS면 카운트 올리기
"""
cnt=0

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        ltmp=line.split('\t')
       # print(ltmp[6])
        if ltmp[6] == 'PASS':
            cnt+=1

print(cnt)
"""
"""
# 강사님 풀이
# 리눅스 상에서 cat 070.vcf | grep "PASS" | wc -l 해도 되는데 6번째가 아닌곳에
#  PASS있으면 그거도 걸릴 수 있음

cnt = 0
with open("070.vcf".'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        if splitted[6] == "PASS":
            cnt += 1

print(cnt)
"""

# filter 가 몇번째인지 모를 수 있음 (#으로 시작하는 것만 갖고오기)


cnt = 0
with open("070.vcf".'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strop().split("\t")
            filt_idx= header.index("FILTER")

        splitted = line.strip().split("\t")
        if splitted[filt_idx] == "PASS":
            cnt += 1

print(cnt)

# 방어적 코딩(헤드 바꼈을 때 대비)

















