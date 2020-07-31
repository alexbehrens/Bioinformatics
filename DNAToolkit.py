import collections
from collections import Counter
from structures import *

def start_seq(logo):
    print(logo)
    print('...')
    print(' ')
    print('Begin DNA Sequencing')
    print(' ')
    print('...')
    print(' ')

def validateSeq(dna_seq):
    #validates no upper and only nuc in seq
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    # Counts Nucs
    tmpFreqDict = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    #dna => rna transcription
    return seq.replace('T', 'U')

def reverse_comlement(seq):
    #doc string not working?
    """swapping adenine with thymine and guanine with cytosine, reversing newly generated string"""
    #return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    #pythonic approach
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

def gc_content(seq):
    '''GC Content in a DNA/RNA Sequence'''
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subsec(seq, k=0):
    '''GC Content in a DNA/RNA subsequence length k, k = 0n by default, outputs percentage for each section '''
    res = []
    for i in range (0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    '''Translates a DNA sequence into an aminoacid sequence'''
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    '''provides the frequency of each codon encoding a given aminoacid in a dna sequence'''
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i +3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return (freqDict)

def gen_reading_frames(seq):
    '''Generate the six reading frames of a DNA Sequence'''
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_comlement(seq), 0))
    frames.append(translate_seq(reverse_comlement(seq), 1))
    frames.append(translate_seq(reverse_comlement(seq), 2))
    return frames
    #didnt fully understand this
