"""
import sys

f = sys.argv[1]

class FASTQ:
    def __init__(self, file_name):
        self.rid = 0
        self.f = file_name
        self.base = ""
    
    def rid(self):
        with open(f,'r') as handle:
            for line in handle:
                if line.startswith('+'):
                    self.rid += 1
            print(self.rid)
    
    def count_base(self):
        with open(f,'r') as handle:
            for line in range(1,self.rid,4):
                self.base += line
    """        
