
import sys 

n = int(sys.argv[1])
"""
class Kmer:

    def __init__(self):
        self.l1 = ['A', 'C', 'G', 'T']
        self.l2 = ['A', 'C', 'G', 'T']
        self.ltmp = []

    def mer(self,l1,l2,n):
        if n == 1:
            return self.l2
        else:
            for s1 in self.l1:
                for s2 in l2:
                    self.ltmp.append(s1+s2)
            return mer(l1,self.ltmp,n-1)

a=Kmer()
print(a.mer(l1,l2,3))
"""

"""
def mer(n: int) -> int:
    lmer = ['','','','']
    if n == 0:
        lmer = ['','','','']
    else:
        for i in range(0,len()):
            for j in ['A','T','G','C']:
                lmer.append(j+lmer(n-1)[i])
    return lemr
  
print(mer(n))    




def mer(n):
    l1 = ['A','G','T','C']
    lmer = []
    if n > 1:
        for i in l1:
            for j in mer(n-1) :
                lmer.append(l1[i] + mer(n-1)[j])
                print(lmer)
    elif n == 1:
        lmer = ['A','G','T','C']
    return lmer


 
def mer(l2,n):
    l1 = ['A','G','T','C']
    if n == 1:
        return l2
    else:
        for s1 in l1:
            for s2 in l2:
                ltmp.append(s1+s2)
        return mer(ltmp,n-1)

"""

# 강사님 풀이

def mer(l1,l2,n):
    if n == 1:
        return l2
 
    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)
    return mer(l1, ltmp, n-1)


l1 = ['A','G','T','C']
l2 = ['A','G','T','C']

print(mer(l1,l2,n))

                  











