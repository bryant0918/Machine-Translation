# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:04:09 2022

@author: Bryant McArthur
"""

import html
import re
        
def clean_lines(file):
    """Go by line to hopefully not completely delete lines"""
    #Read in the text
    with open(file, 'r', encoding = 'utf-8') as myfile:
        lines = myfile.readlines()
        
    with open("hyphen.txt", 'r', encoding = 'utf-8') as data:
        characters = data.read()
        hyphen1 = characters[0]
        hyphen2 = characters[1]
        others = characters[2:]
        
    with open("nonbreakingspace.txt", 'r', encoding = 'utf-8') as data:
        nbs = data.read()
        
        cleaned = []
        print(len(lines))
        for text in lines:
            #Get rid of HTML characters
            newtext = html.unescape(text)
            text = html.unescape(newtext)
            
            """Using Regex"""
            #For weird % issues
            text = re.sub(r"(%\S\s|\s%\s|%.*%|%\S)", "", text)
            
            #Get rid of dumb Hyphens and make them dashes
            text = text.replace(hyphen1, "-")
            text = text.replace(hyphen2, "-")
            
            #For random characters I don't want anywhere
            text = text.replace(others,"")
            #text = text.replace(nbs," ")
            
            #For weird characters at the beginning of the line
            rando = re.compile(r"(^[,#)*-.\s\\\/]\s?)", re.MULTILINE)
            text = rando.sub(r"", text)
            beg = re.compile(r"^\W+",re.MULTILINE)
            text = beg.sub(r"",text)
            numbers = re.compile(r"^[\d\s]*")
            text = numbers.sub(r"", text)
            
            #Get rid of all nonword characters at the end of the line
            end = re.compile(r"\W+$", re.MULTILINE)
            text = end.sub(r"",text)
            numbers = re.compile(r"[\s\d\W]*$")
            text = numbers.sub(r"", text)
            
            #All extra space at the beginning and end of the line
            space = re.compile(r"^\s+", re.MULTILINE)
            space2 = re.compile(r"\s+$", re.MULTILINE)
            text = space.sub(r"", text)
            text = space2.sub(r"", text)
            
            #Ignore Case
            #text = text.casefold()
            
            cleaned.append(text+"\n")
            
            
        print(len(cleaned))
        
        
    with open(file+"Cln.txt",'w', encoding = 'utf-8') as myfile:
        myfile.writelines(cleaned)
    

#clean_random("test.txt")
#print("cleaned")

def complete(eng1, eng2, tgt1, tgt2):
    """
    Sorts and only keeps sentences that are in both
    Start in file1 and run through file 2
    if x in file2 < y in file 1 go to x2
    if x in file2 == y in file1 keep
    if x in file2 > y in file1 stop and go to y2
    At the same time it makes a set to get rid of duplicates
    It also just deletes the sentence if > 3 words or < 100 words
    """
    
    #Open and read text files into list of sentences and sort
    with open(eng1, 'r', encoding = 'utf-8') as file1:
        en1 = file1.readlines()
        
    with open(eng2, 'r', encoding = 'utf-8') as file2:
        en2 = file2.readlines()
    
    with open(tgt1, 'r', encoding = 'utf-8') as file3:
        tg1 = file3.readlines()
        
    with open(tgt2, 'r', encoding = 'utf-8') as file4:
        tg2 = file4.readlines()
        
    #Zip together the corresponding src and tgt texts
    eng_tgt1 = {x:y for (x,y) in zip(en1,tg1)}
    eng_tgt2 = {x:y for (x,y) in zip(en2,tg2)}
    
    
    eng_tgt1 = dict(sorted(eng_tgt1.items()))
    eng_tgt2 = dict(sorted(eng_tgt2.items()))
    
    en1 = list(eng_tgt1.keys())
    en2 = list(eng_tgt2.keys())
    
    new_en_tg1 = {}
    new_en_tg2 = {}
    
    i,j = 0,0
    while (i < len(en1)) and (j < len(en2)):
        #Get rid of random newline characters
        line1 = en1[i].replace("\n", "")
        line2 = en2[j].replace("\n", "")
        if en1[i] < en2[j]: 
            i += 1
        elif en1[i] == en2[j]:
            if 3 <= len(en1[i].split()) <= 100:
                #Make dictionary mapping of complete sentences
                new_en_tg1[en1[i]] = eng_tgt1[en1[i]]
                new_en_tg2[en2[j]] = eng_tgt2[en2[j]]
            i += 1
            j += 1
        else:
            j += 1
    
    english = list(new_en_tg1.keys())
    polish = list(new_en_tg2.values())
    czech = list(new_en_tg1.values())
    
    print(len(english))
    print(len(polish), len(czech))
    
    #Open and write text files
    with open(eng1+"out.txt", 'w', encoding = 'utf-8') as file1:
        en1 = file1.writelines(english)
        
    with open(eng2+"out.txt", 'w', encoding = 'utf-8') as file2:
        en2 = file2.writelines(english)
        
    with open(tgt1+"out.txt", 'w', encoding = 'utf-8') as file3:
        tg1 = file3.writelines(czech)
        
    with open(tgt2+"out.txt", 'w', encoding = 'utf-8') as file4:
        tg2 = file4.writelines(polish)
    
    
if __name__ == "__main__":
# =============================================================================
#     #Clean czech and english with case
#     print("Cleaning")
#     clean_lines("CZ_ENG.txt")
#     clean_lines("CZECH.txt")
#     clean_lines("Cz_ENG.txtCln.txt")
#     clean_lines("CZECH.txtCln.txt")
# =============================================================================
    
# =============================================================================
#     #Complete with itself so it finishes cleaning
#     complete("CZ_ENG.txtCln.txtCln.txt", "CZ_ENG.txtCln.txtCln.txt", "CZECH.txtCln.txtCln.txt", "CZECH.txtCln.txtCln.txt")
#     
# =============================================================================
    #Clean again
    #clean_lines("CZECH.txtCln.txtCln.txtout.txt")
    #clean_lines("CZ_ENG.txtCln.txtCln.txtout.txt")
# =============================================================================
#     #Clean
#     print("cleaning")
#     clean_lines("CZECH.txt")
#     print("cleaning")
#     clean_lines("POLISH.txt")
#     clean_lines("CZ_ENG.txt")
#     clean_lines("PL_ENG.txt")
#     clean_lines("English2M.txt")
#     print("halfway done cleaning")
#     clean_lines("Spanish2M.txt")
#     print("cleaned")
# =============================================================================
    
# =============================================================================
#     #Complete
#     print("Completing Czech and Polish")
#     complete("CZ_ENG.txtclean.txt", "PL_ENG.txtclean.txt", "CZECH.txtclean.txt", "POLISH.txtclean.txt")    
#     print("now completing Spanish and Polish again")
#     complete("English2M.txtclean.txt", "PL_ENG.txtclean.txtout.txt", "Spanish2M.txtclean.txt", "POLISH.txtclean.txtout.txt")
#     print("now completing Spanish and Czech again")
#     complete("English2M.txtclean.txtout.txt", "CZ_ENG.txtclean.txtout.txt", "Spanish2M.txtclean.txtout.txt", "CZECH.txtclean.txtout.txt")
# =============================================================================
    
# =============================================================================
#     #Clean a second time
#     print("cleaning")
#     clean_lines("CZECH.txtclean.txtout.txtout.txt")
#     print("cleaning")
#     clean_lines("POLISH.txtclean.txtout.txtout.txt")
#     clean_lines("English2M.txtclean.txtout.txtout.txt")
#     print("halfway done cleaning")
#     clean_lines("Spanish2M.txtclean.txtout.txtout.txt")
#     print("cleaned")
# =============================================================================
    
# =============================================================================
#     clean_lines("CZ_ENG.txtclean.txtout.txtout.txt")
#     clean_lines("PL_ENG.txtclean.txtout.txtout.txt")
# =============================================================================
    
# =============================================================================
#     
#     #Open and read text files into list of sentences and sort
#     with open("English2M.txtclean.txtout.txtout.txtclean.txt", 'r', encoding = 'utf-8') as file1:
#         en1 = file1.readlines()
#         
#     with open("POLISH.txtclean.txtout.txtout.txtclean.txt", 'r', encoding = 'utf-8') as file2:
#         en2 = file2.readlines()
#     
#     with open("CZECH.txtclean.txtout.txtout.txtclean.txt", 'r', encoding = 'utf-8') as file3:
#         tg1 = file3.readlines()
#         
#     with open("Spanish2M.txtclean.txtout.txtout.txtclean.txt", 'r', encoding = 'utf-8') as file4:
#         tg2 = file4.readlines()
#         
#     with open("fullcorpus.txt", 'w', encoding = "utf-8") as f:
#         f.writelines(en1[:-34] + en2[:-35] + tg1[:-35] + tg2[:-35])
#     
# =============================================================================
