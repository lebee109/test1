"""
import sys

f=sys.argv[1]

with open(f,'r') as handle:
    for line in handle:
        if line.startsith(">"):
            continue
        for i in line
"""

# 강사님
import sys
"""
class FASTA:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.count = {}
        self.length = 0

    def count_base(self):
        with open(self.file_name,'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line = line.strip()                
                for s in line:
                    if s in self.count:
                        self.count[s] +=1
                    else:
                        self.count[s] = 1

    def get_length(self):       # 길이구하기
        for k,v in self.count.items():
           self.length += v
    
    def __len__(self):     # 파이썬 내장함수말고 클래스 안 함수 호출
        self.get_length()
        return self.length
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
    file_name = sys.argv[1]
    t = FASTA(file_name)    # f 넣어야 오류 안남
    t.count_base()
    print(t.count)
   # t.get_length()
   # print(t.length)
    print(len(t))
"""

class FASTQ:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0

    def count_read_num(self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1 
                elif cnt % 4 == 1:
                    seq = line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [fasta]")
    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_read_num()
    print(t.read_num)
   
