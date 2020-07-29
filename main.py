from DNAToolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])
#random DNA string



DNAStr = validateSeq(randDNAStr)
print(f'[1] + Sequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_comlement(DNAStr))} 5'\n")
