import collections
from structures import *

Nucleotides = ['A', 'C', 'G', 'T']
DNA_ReverseComplement =  {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

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
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
