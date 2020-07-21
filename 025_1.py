#슬라이싱
seq1="ATGTTATAG"
"""
for i in (0,len(seq1),3):
    print(i,seq1[i:i+3])
"""

for i in range(0,len(seq1),3):
    print(i,seq1[i]) #인덱싱
    print(i,i+3,seq1[i:i+3])  
