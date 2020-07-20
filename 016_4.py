# 파일 입력하기

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit() 
# 2줄이 아니면 오류여서 sys 나가게함
# 0 : 파일명  1: 파일내용

f  = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip(): # ACGTACGTAAAA
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)

total = 0
for k,v in d.items():   # base 개수 세기, k는 keys,v는 values
    total += v
print(total)    

#출력을 print로 안하고 하이라이트로

with open("result.txt",'w') as handle: #handle은 변수같이 생각하기
    handle.write(f"A: {d['A']}\n")  # 'A' 대신 "A"이면 안됨
    handle.write(f"C: {d['C']}\n") 
    handle.write(f"G: {d['G']}\n") 
    handle.write(f"T: {d['T']}\n")
   
