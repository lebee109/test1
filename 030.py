"""
seq1="AGTTTATGA"

for i in range(0,len(seq1)-1):
    if seq1[i]+seq1[i+1] == "TT":
        print(i)
"""
# 강사님 풀이
import sys

seq1=sys.argv[1]

for i in range(0,len(seq1),1):
   if seq1[i:i+2]=="TT":             # i+2인거 주의
       print(i)
