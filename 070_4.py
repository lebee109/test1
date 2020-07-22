"""
with open("070.vcf",'r') as handle:
    dic={'SNP':0,'Del':0,'Ins':0}
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        ref = splitted[3]
        alt = splitted[4]
        li_alt = splitted[4].split(',')
        for i in range(0,len(li_alt)):
            if len(ref) == len(li_alt[i]):
                dic['SNP'] += 1
            elif len(ref) <  len(li_alt[i]):
                dic['Ins'] += 1
            if len(ref) > len(li_alt[i]):
                dic['Del'] += 1

for k,v in dic.items():
   print(k,v)
"""
import pandas as pd
from matplotlib import pyplot as plt

# 강사님
dic={'snp':0,'ins':0,'del':0}   # 초기화
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        splitted = line.strip().split("\t")
        ref = splitted[3]
        alts = splitted[4].split(',')
        li_alt = splitted[4].split(',')
        for alt in alts:
            if len(ref) == len(alt): #snp
                dic['snp'] += 1
            elif len(ref) >  len(alt): #del
                dic['del'] += 1       
            elif len(ref) < len(alt):   # ins
                dic['Del'] += 1
            else:
                raise    # 방어적 코딩 ( 오류나지 않고 멈춤)


print(dic)
df = pd.DataFrame([dic])    # 테이블형태로 출력
print(df)
df.plot.bar()
plt.savefig("v.png")    # 그림으로

















