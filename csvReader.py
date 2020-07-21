"""
import sys

f = sys.argv[1]
l=[]
with open(f,'r') as handle:
    for line in handle:
        if line.startswith("#"):
            line.replace('#',"")
            inde=line.split(',')
            continue
        li=line.split(',')
        d={}
        for i in li:
            d[inde[i]]=li[i]
        l.append(d)

print(l)
       """ 
import sys           ###안되서 내가 붙임
# 강사님 풀이
f = sys.argv[1]        ###안되서 내가 붙임

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")     # 딕셔너리로 묶여나옴   row 값
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("#uasge: python {sys.argv[0]} [txt]")

print(read_csv(f))           ###안되서 내가 붙임










