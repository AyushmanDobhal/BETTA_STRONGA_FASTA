 #!/usr/bin/env python3



import sys
#import re
import matplotlib.pyplot as plt

#import numpy as np
fasta_file=sys.argv[1]

def parse_fasta(fasta_file):
    sequence={}
    seq_name= ""
    header= None
    length = 0
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith(">"):
                if header is not none:
                    print(header,length)
                    length = 0
                header=line[1:]
            else:
                lenght += len(line)
    if length:
        print(header, length)

def len_histo(fasta_input):
    lengths=list()
    for header in fasta_input:
      lengths.append(len(),length:)    
