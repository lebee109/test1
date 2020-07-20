def mySum(n1: int, n2: int) -> None:
    print(f"{n1}+{n2}={n1+n2}")

res1 = mySum(2,3)
res2 = mySum(5,7)
res3 = mySum(10,15)

print("----")

print(res1)
print(res2)
print(res3)


def mySum(n1: int, n2: int) -> int:    #int가 들어가고 int가 나온다고 알려줌(안써도 무방)
    print(f"{n1}+{n2}={n1+n2}")
    return n1+n2

res1 = mySum(2,3)
res2 = mySum(5,7)
res3 = mySum(10,15)

print("----")

print(res1)
print(res2)
print(res3)

