l=[3,1,1,2,0,0,2,3,3]
d={}

for i in range(0,len(l)):
    if l[i] in d.keys():
        d[l[i]] +=1
    else:
        d[l[i]] = 1

print(d)
"""
#강사님
for elem in l:
    if elem in d:
        d[elem] +=1
    else:
        d[elem] =1


print(d)



##순서 없는 것
1. 딕셔너리
   a
2. set
   {} 형태
   add로 추가


"""



