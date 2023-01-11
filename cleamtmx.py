# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:57:14 2022

@author: Bryant McArthur
"""
from translate.storage.tmx import tmxfile

def clean(infile, outfile="infile.txt"):
    """Clean a TMX file up to Dr. Richardson's standards"""
    
    with open(infile,'r',encoding='utf-8') as file:
        sentences = file.read().split('\n')  # read the training set from the file filename
        unique_words = set()
            
        

clean("14 166 - Polish - FamilyHistory - Recent.tmx.txt")
