"""
pivo = []

n=int(input())
for i in range(0,n):
    if i == 0:
        pivo.append(0)
    elif i == 1:
        pivo.append(1)
    else:
        pivo.append(pivo[-2]+pivo[-1])

print(pivo)


"""
#강사님 피보나치
import sys

def fib(n: int)-> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)   # return에 함수 있는게 재귀

n = int(sys.argv[1])

print(fib(n))

# (base) [root@centos6 test1]# python pivo.py 10
#  55

