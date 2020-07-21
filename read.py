"""
# 016참고
import sys

f=sys.argv[1]

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue   
        print(line.strip(),end='')
print()
"""
import sys

#강사님
def read_txt(file_name: str)-> str:
    ret = ""
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"):    #헤더 없애기
                continue
            ret += line.strip()
    return ret

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#uasge: python {sys.argv[0]} [txt]")
    
    file_name = sys.argv[1]
    txt = read_txt(file_name)
    print(txt)    # => return ret가 프린트됨


