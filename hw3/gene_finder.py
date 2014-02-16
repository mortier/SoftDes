# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    # YOUR IMPLEMENTATION HERE
    sequence = '' 
    for i in range(len(dna)/3):
        L=dna[i*3:i*3+3]
        for a in range(len(aa)):
            if L in codons[a]:
                sequence = sequence + str(aa[a])
               
    return sequence 
                   

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """
        
    # YOUR IMPLEMENTATION HERE
    if coding_strand_to_AA("TTTCAAAACAATTGT") == 'FQNNC' and coding_strand_to_AA("TTTCAAAACAATTTT") == 'FQNNF' and coding_strand_to_AA("TTTCAAAACCAATGT") == 'FQNQC':
        return "good"
    else:
        return "bad"
        
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE
    reverse = ''
    for i in range(len(dna)):
        L = dna[i]
        if L == "A":
            reverse = reverse + "T"
        elif L == "T":
            reverse = reverse + "A"
        elif L == "G":
            reverse = reverse + "C"
        elif L == 'C':
            reverse = reverse + "G"   
    return reverse
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """
        
    # YOUR IMPLEMENTATION HERE    
    if get_reverse_complement('ATGCTACGGCAT')== 'TACGATGCCGTA':
        return "good"
    else:
        return "bad"
        
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE
    sequence = ''
    for i in range(len(dna)/3):
        L=dna[i*3:i*3+3]
        if L == "TAG" or L == 'TAA' or L == 'TGA':
            return sequence
        else:
            sequence = sequence + str(L)
    return sequence

def rest_of_ORF_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """
    if rest_of_ORF('ATGGCATTT')== "ATGGCATTT" and rest_of_ORF('ATGTAA')=='ATG' and rest_of_ORF('ATGTTTCGATAG')=='ATGTTTCGA':
       return "good"
    else:
       return "bad"
        
    # YOUR IMPLEMENTATION HERE
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    # YOUR IMPLEMENTATION HERE   
    dnasequence=[]     
    for i in range(len(dna)):
        if i % 3 == 0:
            codon = dna[i:i+3]
            dnasequence.append(codon) 
    a=0
    listoORF=[]
    while a < len(dnasequence):       
        if dnasequence[a] == "ATG":
            for b in range(a,len(dnasequence)):
                 if dnasequence[b]=="TAG" or dnasequence[b]=="TAA" or dnasequence[b]=="TGA":
                     listoORF.append(dnasequence[a:b])
                     a = b
                     break
        a += 1
    res=[]
    for x in range(len(listoORF)):
        res.append(collapse(listoORF[x]))
    return res
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """

    # YOUR IMPLEMENTATION HERE
    if find_all_ORFs_oneframe('ATGGAGTAGATGGAGTAG')== ['ATGGAG', 'ATGGAG'] and find_all_ORFs_oneframe('ATGGAGTAG')== ['ATGGAG']:
        return "good"
    else:
        return "bad"
    

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
    stuff = []
    for i in range(3):
        offset=i
        filler = find_all_ORFs_oneframe(dna[offset:])
        stuff += filler
    return stuff

    
def find_all_ORFs_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """
        
    # YOUR IMPLEMENTATION HERE
    if find_all_ORFs('ATGTTTTAATGTTTTAATGTTTTAA') == ['ATGTTT','ATGTTT',"ATGTTT"]:
        return "good"
    else:
        return "bad"

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
    strings=[]
    reverse = get_reverse_complement(dna)
    strings = (find_all_ORFs(dna))
    strings = strings + (find_all_ORFs(reverse))
    return strings

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """

    # YOUR IMPLEMENTATION HERE

    if find_all_ORFs_both_strands('ATGTTTTAATGTTTTAATGTTTTAATACAAAATTACAAAATTACAAAATT') == ['ATGTTT','ATGTTT',"ATGTTT",'ATGTTT','ATGTTT',"ATGTTT"]:
        return "good"
    else:
        return "bad"

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE
    allorfs=find_all_ORFs(dna)
    return [max(allorfs, key=len)]

def longest_ORF_unit_tests():
    """ Unit tests for the coding_strand_to_AA function. Iff all the stuff returns
    expected values the function returns the string 'good' if not, the string 
    'bad' """
    
    # YOUR IMPLEMENTATION HERE
    if longest_ORF('ATGTTTTAATGTTTTTTTAATGTTTTAATACAAAATTACAAAATTACAAAATT') == ['ATGTTTTTT']:
        return "good"
    else:
        return "bad"

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE
    absbest=[]
    from random import shuffle
    for i in range(num_trials):
        dna=list(dna)
        shuffle(dna)
        dna=collapse(dna)
        best=longest_ORF(dna)
        absbest=absbest + [best]
    return len(max(absbest,key=len))

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE
    ALLDAFUCKAS=find_all_ORFs_both_strands(dna)
    allprotines=[]    
    for i in range(len(ALLDAFUCKAS)):
        if len(ALLDAFUCKAS[i])>=threshold:
            protiens = coding_strand_to_AA(ALLDAFUCKAS[i])
            allprotines.append(protiens)
            print allprotines
    return allprotines
            