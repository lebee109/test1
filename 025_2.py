"""
#뒤집기
seq1="ATGTTATAG"

print(seq1)
print(seq1[::-1])
"""
"""
#상보적
seq1="ATGTTATAG"

d={'A':'T','T':'a','C':'G','G':'c'}

for i in range(0,len(seq1)):
   chseq1= seq1.replace(seq1[i],d[seq1[i]])

chseq1.upper()

print(chseq1)
"""

# 아이디어1
import sys

def comp1(seq: str) -> str:
    comp =""
    for s in seq:
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "T":
            comp += "A"
        elif s == "G":
            comp += "C"
    return comp

# 아이디어 2
import sys

def comp2(seq: str)-> str:
    d_comp = {"A":"T","T":"A","C":"G","G":"C"}
    comp = ""
    for s in seq:
        comp +=d_comp[s]
    return comp
#-----------------------------------------------

if __name__ == "__main__":    #  import시에는 실행 안됨
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()
seq1 = sys.argv[1]
c1=comp1(seq1)
c2=comp2(seq1)
print(seq1)
print(c1)
print(c2)


