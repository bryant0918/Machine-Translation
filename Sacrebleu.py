# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:02:18 2022

@author: Bryant McArthur
"""

from sacrebleu.metrics import BLEU, CHRF, TER


bleu = BLEU()



def get_bleu(referencefile, translatedfile):
    with open(referencefile, 'r', encoding = 'utf-8') as rfile:
        refs = rfile.readlines()
        refs = [refs]
        
        with open(translatedfile, 'r', encoding = 'utf-8') as tfile:
            sys = tfile.readlines()
            sys = sys
            
            #print(bleu.corpus_score(sys, refs))
            
            
    return bleu.corpus_score(sys,refs)
            
            
if __name__ == "__main__":
# =============================================================================
#     
#     OpenNMT = get_bleu("OpenNMT/nottoy-enpl/src-test.txt", "OpenNMT/pred_40000.txt")
#     print(OpenNMT)
#     
#     tags = get_bleu()
# =============================================================================
# =============================================================================
#     #Check Czech
#     tags = get_bleu("Final Project/Es-Cz Model/src-test.txt2.txt", "Final Project/Cz_OUT.txt")
#     print("Czech", tags)
#     
#     #Check Polish
#     tags = get_bleu("Final Project/Pl-Es Model/tgt-test.txt2.txt", "Final Project/Pl_OUT.txt")
#     print("Polish", tags)
#     
#     #Check Spanish
#     tags = get_bleu("Final Project/Es-Cz Model/tgt-test.txt2.txt", "Final Project/Es_OUT.txt")
#     print("Spanish", tags)
# =============================================================================
    
    

    