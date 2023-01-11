# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:12:52 2022

@author: Bryant McArthur
"""

import numpy as np
import re
import json

def initialize(t, init_val, english_words, foreign_words):
    print("Initializing...")
    for fw in foreign_words:
        for ew in english_words:
            tup = (ew,fw)
            t[tup] = init_val
    return t

def get_word_dict(x):
    """from sentence pairs return set of english words
    and foreign words"""
    
    english_words = set()
    foreign_words = set()
    
    print("Getting word dictionary...")
    
    for i,sp in enumerate(x):
        for fw in sp[0]:
            foreign_words.add(fw)
        for ew in sp[1]:
            english_words.add(ew)
        
    
    return english_words, foreign_words
    
    

def IBM1(sentence_pairs, maxiters=15, p=True):
    """Return translation probability t(e|f)"""
    t, stotal = {},{}
    
    e,f = get_word_dict(sentence_pairs)
    n = len(e)
    init_val = 1/n
    
    #Initialize t uniformly
    t = initialize(t,init_val,e,f)
    
    #print(t[('Accordingly','Zgodnie')])

    for i in range(maxiters):
        print("iterating at i=",i)
        count,total = {},{}
        for fw in f:
            total[fw] = 0
            for ew in e:
                count[(ew,fw)] = 0
        
        
        for sp in sentence_pairs:
            
            # Compute Normalization
            for ew in sp[1]:
                stotal[ew] = 0.0
                for fw in sp[0]:
                    stotal[ew] += t[(ew, fw)]
            
            # Collect Counts
            for ew in sp[1]:
                for fw in sp[0]:
                    count[(ew,fw)] += t[(ew,fw)] / stotal[ew]
                    total[fw] += t[(ew,fw)] / stotal[ew]
        
        
        # Estimate Probabilities
        for fw in f:
            for ew in e:
                t[(ew,fw)] = count[(ew,fw)] / total[fw]
            
            
        
        if p:
            print("iteration: ",i)
            [print(key,':',value) for key, value in t.items()]     
            print("**********")
            print("***********")
            print()
            
        
        #Calculate convergence
        
        
        
        
        
    # Find the best translation
    pairs = []
    for fw in f:
        elem = e.pop()
        maxpair = (elem,fw)
        e.add(elem)
        for ew in e:
            if t[(ew,fw)] > t[maxpair]:
                maxpair = (ew,fw) 
            
        pairs.append(maxpair)   
        
        
    return t,pairs
        

def make_sentence_pairs(infile1,infile2,Truncate=True):
    
    with open(infile1,'r',encoding='utf-8') as myfile:
        english = myfile.read().split('\n')[0:50]
        
        english = np.array(english)
        
        with open(infile2, 'r',encoding='utf-8') as myfile:
            foreign = myfile.read().split('\n')[0:50]
            foreign = np.array(foreign)
            
            #sentence_pairs = np.array([[[fwords for fwords in forsent.split()], [ewords for engsent.split()] for forsent, engsent in foreign, english] ])
            
            ew,fw = [],[]
            print(len(english))
            if Truncate:
                for i in range(50):
                    for engsent in english:
                        engsent = re.sub(r'[^\w\s]', '', engsent)  #Remove punctionation
                        ewords = engsent.split()
                        ew.append(ewords)
                    for forsent in foreign:
                        forsent = re.sub(r'[^\w\s]', '', forsent)
                        fwords = forsent.split()
                        fw.append(fwords)
            else:
                for engsent in english:
                    engsent = re.sub(r'[^\w\s]', '', engsent)  #Remove punctionation
                    ewords = engsent.split()
                    ew.append(ewords)
                for forsent in foreign:
                    forsent = re.sub(r'[^\w\s]', '', forsent)
                    fwords = forsent.split()
                    fw.append(fwords)
                
            ew = np.array(ew,dtype=object)
            fw = np.array(fw,dtype=object)
            
            sp = np.vstack((fw, ew)).T
            
    print("Done")        
    return sp

if __name__ == "__main__":
    
    
    
    sentence_pairs = np.array([
    [['la', 'maison'],['the', 'house']], 
    [['la', 'fleur'],  ['the', 'flower']],
    [['la','maison','bleu'],['the','blue','house']],
    [['la','fleur','bleu'],['the','blue','flower']],
    [['pomme','bleu'],['blue','apple']]],dtype=object)
    
    print(sentence_pairs[0])
    print(sentence_pairs.shape)
    
    t,pairs = IBM1(sentence_pairs,3)
    print(pairs)
    
    """
    sentence_pairs2 = make_sentence_pairs("churchenglish.txt","churchpolish.txt")
    print(sentence_pairs2.shape)
    
    
    t,pairs = IBM1(sentence_pairs2,4,p=False)
    print(pairs)
    """
    #[print(key,':',value) for key, value in t.items()]
    
    #pairs = ('should', 'wydobędę'), ('the', 'wyczekiwaną')
    
    with open("pairs.txt",'w') as myfile:
        pairs = re.sub('\)', '\n', str(pairs))
        myfile.write(repr(pairs))
        
    pass
        
    

    

