# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:29:26 2022

@author: Bryant McArthur
"""

import os

def getxlines(infile, training, test, validation, vector):
    """Get the training, test, and validation text files from a large given text file"""
    
    x,y,z = vector[0],vector[1],vector[2]
    
    
    with open(infile, 'r', encoding = 'utf-8') as myfile:
        data = myfile.readlines()
        
        trn = data[:x]
        tst = data[x+1:x+1+y]
        val = data[x+1+y+1:x+2+y+z]
        
        with open(training, 'w', encoding='utf-8') as outfile1:
            for line in trn:
                outfile1.write(line)
        
            with open(test, 'w', encoding='utf-8') as outfile2:
                for line in tst:
                    outfile2.write(line)
         
                with open(validation, 'w', encoding='utf-8') as outfile3:
                    for line in val:
                        outfile3.write(line)
        

if __name__ == "__main__":
    #getxlines("churchenglish.txt", 'src-train.txt', 'src-test.txt', 'src-val.txt', [50000,2500,2500])
    #getxlines("churchpolish.txt", 'tgt-train.txt', 'tgt-test.txt', 'tgt-val.txt', [50000,2500,2500])
    head -n 2 nottoy-enpl/src-train.txt
    pass