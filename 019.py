import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [txt]")
    sys.exit()

f = sys.argv[1]

try:
    with open(f,'r') as handle:
        read = handle.readlines() # list로 반환

except FileNotFoundError:            # 없는 파일일 경우
    print(f"{f} not found.. please check..")
    sys.exit()

print(read)
