#!/usr/bin/python
import sys,random,re

amino = {'A': {1.0: 'GCC', 0.6: 'GCU', 0.1: 'GCG', 0.33: 'GCA'}, 'C': {1.0: 'UGC', 0.46: 'UGU'}, 'E': {0.42: 'GAA', 1.0: 'GAG'}, 'D': {1.0: 'GAC', 0.46: 'GAU'}, 'G': {1.0: 'GGC', 0.66: 'GGG', 0.16: 'GGU', 0.41: 'GGA'}, 'F': {1.0: 'UUC', 0.46: 'UUU'}, 'I': {0.17: 'AUA', 1.0: 'AUC', 0.53: 'AUU'}, 'H': {0.42: 'CAU', 1.0: 'CAC'}, 'K': {0.43: 'AAA', 1.0: 'AAG'}, 'M': {1.0: 'AUG'}, 'L': {0.27: 'CUU', 0.4: 'UUG', 1.0: 'CUG', 0.14: 'UUA', 0.6: 'CUC', 0.06: 'CUA'}, 'N': {1.0: 'AAC', 0.47: 'AAU'}, 'Q': {0.27: 'CAA', 1.0: 'CAG'}, 'P': {0.68: 'CCU', 1.0: 'CCC', 0.11: 'CCG', 0.39: 'CCA'}, 'S': {0.54: 'UCU', 0.76: 'UCC', 0.05: 'UCG', 0.2: 'UCA', 1.0: 'AGC', 0.35: 'AGU'}, 'R': {0.79: 'AGG', 0.58: 'CGG', 0.38: 'CGC', 0.2: 'CGA', 1.0: 'AGA', 0.08: 'CGU'}, 'T': {1.0: 'ACC', 0.11: 'ACG', 0.36: 'ACU', 0.64: 'ACA'}, 'W': {1.0: 'UGG'}, 'V': {0.54: 'GUC', 0.3: 'GUU', 0.12: 'GUA', 1.0: 'GUG'}, 'Y': {1.0: 'UAU', 0.56: 'UAC'}}
#amino = {'A': {1.0: 'GCC', 0.6: 'GCU', 0.1: 'GCG', 0.33: 'GCA'}, 'C': {1.0: 'UGC', 0.46: 'UGU'}, 'E': {0.42: 'GAA', 1.0: 'GAG'}, 'D': {1.0: 'GAC', 0.46: 'GAU'}, 'G': {1.0: 'GGC', 0.66: 'GGG', 0.16: 'GGU', 0.41: 'GGA'}, 'F': {1.0: 'UUC', 0.46: 'UUU'}, 'I': {0.17: 'AUA', 1.0: 'AUC', 0.53: 'AUU'}, 'H': {0.42: 'CAU', 1.0: 'CAC'}, 'K': {0.43: 'AAA', 1.0: 'AAG'}, 'M': {1.0: 'AUG'}, 'L': {0.27: 'CUU', 0.4: 'UUG', 1.0: 'CUG', 0.14: 'UUA', 0.6: 'CUC', 0.06: 'CUA'}, 'N': {1.0: 'AAC', 0.47: 'AAU'}, 'Q': {0.27: 'CAA', 1.0: 'CAG'}, 'P': {0.68: 'CCU', 1.0: 'CCC', 0.11: 'CCG', 0.39: 'CCA'}, 'S': {0.54: 'UCU', 0.76: 'UCC', 0.05: 'UCG', 0.2: 'UCA', 1.0: 'AGC', 0.35: 'AGU'}, 'R': {0.79: 'AGG', 0.58: 'CGG', 0.38: 'CGC', 0.2: 'CGA', 1.0: 'AGA', 0.08: 'CGU'}, 'T': {1.0: 'ACC', 0.11: 'ACG', 0.36: 'ACU', 0.64: 'ACA'}, 'W': {1.0: 'UGG'}, 'V': {0.54: 'GUC', 0.3: 'GUU', 0.12: 'GUA', 1.0: 'GUG'}, 'Y': {1.0: 'UAU', 0.56: 'UAC'}}

seq = raw_input('Input the amino acid sequence\n>> ')
genome = ''
seq_list = list(seq)
rand_list = []
for char in seq_list:
    #generate random number(0<rand<1)
    rand = random.random()
    rand_list.append(rand)
#    print rand
    cumlo = sorted(amino[char].keys())

    comp = 0 #number in cumlo
    while comp < len(cumlo):        
        if rand < cumlo[0]: # compare values
#            print amino[char][cumlo[0]]
            genome = genome + amino[char][cumlo[0]]
            break
        elif rand > cumlo[comp] and rand < cumlo[comp+1]:
#            print amino[char][cumlo[comp+1]]
            genome = genome + amino[char][cumlo[comp+1]]
            break
        comp = comp + 1
print genome

summ = 0
for 
print 

