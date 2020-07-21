l=[3,1,1,2,0,0,2,3,3]
"""
for i in l[,,]:
    if l[i]>l[i+1]

print(ma,mi)
"""

#강사님 풀이
max(l)
min(l)



max_val = l[0]  #초기화
min_val = l[0]

for elem in l:
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(f"max: {max_val}")
print(f"min: {min_val}")
