from DNAToolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(500)])
#random DNA string



DNAStr = validateSeq(randDNAStr)

print(start_seq(dna_logo))
print(f'[1] + Sequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Reverse Complement: \n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_comlement(DNAStr))} 5'\n")
print(f"[5] + GC Content: {gc_content(DNAStr)}% \n")
print(f"[6] GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=25)}\n")
print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 15)}\n')
print(f'[8] + Codon Frequency (L): {codon_usage(DNAStr, "L")}\n')
print('[9] + Reading Frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)


