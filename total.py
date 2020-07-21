import sys
import json

def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

#json 쓰기
def to_json(l: list, file_name: str) -> None:
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4)   # 4는 4칸의 space 의미 python json document 참고

#json 읽기
def read_json(file_name: str) -> list:
    with open(file_name,'r') as handle:
        l = json.load(handle)   #리스트 형태 넣으면 리스트 형태로 나옴
    return l    



if __name__ == "__main__":              #import 시에는 안돌아감
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    #txt = read_txt(file_name)
    #print(txt)
    #ret = read_csv(file_name)    # csv 파일 넣기
    ret = read_tsv(file_name)     # tsv파일 넣기
    to_json(ret,"result.json")
