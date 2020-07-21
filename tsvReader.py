 
import sys           ###안되서 내가 붙임
# 강사님 풀이

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")     # 딕셔너리로 묶여나옴   row 값
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("#uasge: python {sys.argv[0]} [txt]")

file_name=sys.argv[1]
print(read_tsv(file_name))           ###안되서 내가 붙임










