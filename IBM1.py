# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:37:33 2022

@author: Bryant McArthur
"""

import math
import numpy
import matplotlib.pyplot as plt
    
    
def probability_e_f(e, f, t, epsilon=1):
    l_e = len(e)
    l_f = len(f)
    p_e_f = 1
    
    for ew in e: # iterate over english words ew in english sentence e
        inner_sum = 0
        for fw in f: # iterate over foreign words fw in foreign sentence f
            inner_sum += t[(ew, fw)]
        p_e_f = inner_sum * p_e_f
    
    p_e_f = p_e_f * epsilon / (l_f**l_e)
    
    return p_e_f 


def perplexity(sentence_pairs, t, epsilon=1, debug_output=False):
    pp = 0
    
    for sp in sentence_pairs:
        prob = probability_e_f(sp[1], sp[0], t)
        if debug_output:
            """
            print('english sentence:', sp[1], 'foreign sentence:', sp[0])
            print(prob)
            print()
            """
        pp += math.log(prob, 2) # log base 2
        
    pp = 2.0**(-pp)
    return pp


# Get sentence pairs for toy experiment

sentence_pairs = [ 
    [ ['das', 'Haus'], ['the', 'house'] ], 
    [ ['das', 'Buch'], ['the', 'book'] ], 
    [ ['ein', 'Buch'], ['a', 'book'] ]
]


sentence_pairs = [
    [ ['la', 'maison'],     ['the', 'house'] ],
    [ ['la', 'fleur'],      ['the', 'flower']],
    [ ['la','maison','bleu'],['the','blue','house']],
    [ ['la','fleur','bleu'],['the','blue','flower']],
    [ ['pomme','bleu'],     ['blue','apple']]
]

"""
print('No. of sentences in translation memory: ', len(sentence_pairs))
print('Content: ', sentence_pairs)
"""

# Extract foreign and english vocabularies
foreign_words = []
english_words = []

for sp in sentence_pairs:
    for ew in sp[1]: 
        english_words.append(ew)
    for fw in sp[0]: 
        foreign_words.append(fw)
        
english_words = sorted(list(set(english_words)), key=lambda s: s.lower()) 
foreign_words = sorted(list(set(foreign_words)), key=lambda s: s.lower())
"""
print('English vocab: ', english_words)
print('Foreign vocab: ', foreign_words)
"""
english_vocab_size = len(english_words)
foreign_vocab_size = len(foreign_words)
"""
print('english_vocab_size: ', english_vocab_size)
print('foreign_vocab_size: ', foreign_vocab_size)
"""


# Routine to uniformly initialize word translation probabilities in t hash

def init_prob(t, init_val, english_words, foreign_words):
    for fw in foreign_words:
        for ew in english_words:
            tup = (ew, fw) # tuple required because dict key cannot be list
            t[tup] = init_val
            
# Main routine
num_iterations = 2
perplex = []
debug_output = True
s_total = {}

# Initialize probabilities uniformly
t = {}
init_val = 1.0 / foreign_vocab_size
init_prob(t, init_val, english_words, foreign_words)
#print(t)

if debug_output:
    print('Hash initialized')
    print('No. of foreign/english pairs: ', len(t))
    print('Content: ', t)
    print('**************')
    print()

# Loop while not converged
for iter in range(num_iterations):
    print()
    print(iter)
    # Calculate perplexity
    pp = perplexity(sentence_pairs, t, 1, True)
    print(pp)
    print('**************')
    perplex.append(pp)

    # Initialize
    count = {}
    total = {}
    
    
    for fw in foreign_words:
        total[fw] = 0.0
        for ew in english_words:
            count[(ew,fw)] = 0.0
            
    for sp in sentence_pairs:

        # Compute normalization
        for ew in sp[1]:
            #print("Normalization word",ew)
            s_total[ew] = 0.0
            for fw in sp[0]:
                s_total[ew] += t[(ew, fw)]
        
        # Collect counts
        for ew in sp[1]:
            #print("English word",ew)
            for fw in sp[0]:
                count[(ew, fw)] += t[(ew, fw)] / s_total[ew]
                total[fw] += t[(ew, fw)] / s_total[ew]
                
    
    
    # Estimate probabilities
    for fw in foreign_words:
        for ew in english_words:
            t[(ew, fw)] = count[(ew, fw)] / total[fw]

    
    if debug_output:
        [print(key,':',value) for key, value in t.items()]
        
        