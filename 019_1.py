import sys

if len(sys.argv) != 2:
    print(f"#uasge: python {sys.argv[0]} [num]")
    sys.exit()

try:
    num = int(sys.argv[1])
    print(10/num)     # num이 0 일때 오류날수있어서 예외처리
except ValueError:
    print("input not valid")
    sys.exit()                     # 멈추게 하는 것
except ZeroDivisionError:
    print("0으로 못나눔")
    sys.exit()                     # 멈추게 하는 것


