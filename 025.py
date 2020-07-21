seq1 = "ATGTTATAG"
"""
for i in seq1(,,3):
    print(seq1[i])
"""

for i in range(0,len(seq1),3):
   # print(i)   # 0,3,6
    print(i,seq1[i])
