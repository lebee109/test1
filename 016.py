"""
FI = open("read_sample.txt",'r')

FI_read = FI.read()
print(FI_read)
FI.close()

FI = readline
"""


with open("read_sample.txt",'r') as handle:
    for line in handle:
        if line.startswith(">"):         #header 안나오게
            continue
        print(line.strip())    # 열리고 끝나면 알아서 닫힘
                                # strip없으면 엔터로 줄 바뀜(비교해보기)


# header 안나오게 하기

