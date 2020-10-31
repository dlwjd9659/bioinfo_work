import sys

class Parser:
    def __init__(self, file_name):
        self.filename = file_name
        self.line_cnt = 0
    def parse(self, data_type):
        if data_type.lower() == "fastq":
            cnt = 0
            with open(self.filename, 'r') as handle:
                for line in handle:
                    if cnt % 4 == 0:
                        self.line_cnt += 1
                    elif cnt % 4 == 1:
                        pass
                    elif cnt % 4 == 3:
                        pass
                    cnt += 1
        
        elif data_type.lower() == "fasta":
            pass

file_name = sys.argv[1]
parser = Parser(file_name)
parser.parse("fastq")
print(parser.line_cnt)
