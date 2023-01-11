# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:57:14 2022

@author: Bryant McArthur
"""
from translate.storage.tmx import tmxfile

def clean(infile, outfile="infile.txt"):
    """Clean a TMX file up to Dr. Richardson's standards"""
    
    with open(infile,'rb') as file:
        tmx_file = tmxfile(file,'en','pl')
        
    for node in tmx_file.unit_iter():
        print(node.source, node.target)
        


