"""
# 내풀이   - 답나옴
with open("070.vcf",'r') as handle:
    cnt = 0
    for line in handle:
        if line.startswith('#'):
            continue
        else:
            cnt += 1
    print(cnt)
"""

# 강사님 풀이
cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        cnt+=1
print(cnt)
