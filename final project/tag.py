# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:35:18 2022

@author: Bryant McArthur
"""

import random
from sklearn.model_selection import train_test_split
import re

def tag(src_file, tgt_file, src_lang, tgt_lang):
    """
    Tag every sentence for MNMT Model src and tgt
    """
    
    #Define the Target Tags depending on the source language
    if src_lang == "Pl":
        tgt_tag = "<pl>"
    elif src_lang == "Cz":
        tgt_tag = "<cz>"
    elif src_lang == "Es":
        tgt_tag = "<es>"
    elif src_lang == "En":
        tgt_tag = "<en>"
    else:
        raise ValueError("language given not in domain")
        
    #Define the Source Tags dependig on the target language
    if tgt_lang == "Pl":
        src_tag = "<pl>"
    elif tgt_lang == "Cz":
        src_tag = "<cz>"
    elif tgt_lang == "Es":
        src_tag = "<es>"
    elif tgt_lang == "En":
        src_tag = "<en>"
    else:
        raise ValueError("language given not in domain")
        
    #Get rid of existing tags at the begining
    untag = re.compile(r"^<.*>\s", re.MULTILINE)
    
    #Open the Source text file
    with open(src_file, 'r', encoding = "utf-8") as myfile:
        src_text = myfile.readlines()
        
        #For every line add the tag at the front
        for i in range(len(src_text)):
            src_text[i] = untag.sub(r"", src_text[i])
            src_text[i] = src_tag +" "+ src_text[i]
            
    #Open the Target text file
    with open(tgt_file, 'r', encoding = "utf-8") as myfile:
        tgt_text = myfile.readlines()
        
        #For every line add the tag at the front
        for i in range(len(src_text)):
            tgt_text[i] = untag.sub(r"", tgt_text[i])
            tgt_text[i] = tgt_tag +" "+ tgt_text[i]
            
            
    with open(src_file, 'w', encoding = "utf-8") as outfile:
            outfile.writelines(src_text)
        
    with open(tgt_file, 'w', encoding = "utf-8") as outfile:
            outfile.writelines(tgt_text)
        
def tag1(src_file, lang):
    """
    Tag every sentence for MNMT Model src and tgt
    """
        
    #Define the Source Tags dependig on the target language
    if lang == "Pl":
        src_tag = "<2pl>"
    elif lang == "Cz":
        src_tag = "<2cz>"
    elif lang == "Es":
        src_tag = "<2es>"
    elif lang == "En":
        src_tag = "<2en>"
    else:
        raise ValueError("language given not in domain")
        
    #Get rid of existing tags at the begining
    untag = re.compile(r"^<.*>\s", re.MULTILINE)
    
    #Open the Source text file
    with open(src_file, 'r', encoding = "utf-8") as myfile:
        src_text = myfile.readlines()
        
        #For every line add the tag at the front
        for i in range(len(src_text)):
            src_text[i] = untag.sub(r"", src_text[i])
            src_text[i] = src_tag +" "+ src_text[i]
            
            
    with open(src_file+"tag.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(src_text)
            
    return src_text
        
        
            
def rmvtag(file):
    """Remove tags because apparently they decrease performance on OpenNMT"""
    
    #Get rid of existing tags at the begining
    untag = re.compile(r"^<.*>\s", re.MULTILINE)
    
    #Open the Source text file
    with open(file, 'r', encoding = "utf-8") as myfile:
        src_text = myfile.readlines()
        
        #For every line add the tag at the front
        for i in range(len(src_text)):
            src_text[i] = untag.sub(r"", src_text[i])
    
    with open(file, 'w', encoding = "utf-8") as outfile:
            outfile.writelines(src_text)

    return src_text

def split(file, src = True):
    """
    shuffle with random seed
    split
    write to correct Model folder
    """
    with open(file, 'r', encoding = "utf-8") as myfile:
        text = myfile.readlines()
    
    test = []
    train = []
    val = []
    
    #Split evenly
    for i in range(len(text)):
        if i % 10 == 0:
            test.append(text[i])
        elif i % 10 == 5:
            val.append(text[i])
        else:
            train.append(text[i])
    
    
    if src:
        with open("src-test.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(test)
        
        with open("src-train.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(train)
            
        with open("src-val.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(val)
            
        return test, val, train
        
    else:
        with open("tgt-test.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(test)
        
        with open("tgt-train.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(train)
            
        with open("tgt-val.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(val)
            
        return test, val, train
    

def split2(file, file2, file3, file4):
    """
    shuffle with random seed
    split
    write to correct Model folder
    """
    with open(file, 'r', encoding = "utf-8") as myfile:
        text = myfile.readlines()
        
    with open(file2, 'r', encoding = "utf-8") as myfile:
        text2 = myfile.readlines()
        
    with open(file3, 'r', encoding = "utf-8") as myfile:
        text3 = myfile.readlines()
        
    with open(file4, 'r', encoding = "utf-8") as myfile:
        text4 = myfile.readlines()
        
        
    lines = [(w,x,y,z) for (w,x,y,z) in zip(text,text2,text3,text4)]
   
    random.shuffle(lines)
    
    text = [line[0] for line in lines]
    text2= [line[1] for line in lines]
    text3= [line[2] for line in lines]
    text4= [line[3] for line in lines]
    
    
   
    test = text[:-6000]
    train = text[-6000:-3000]
    val = text[-3000:]
    
    test2 = text2[:-6000]
    train2 = text2[-6000:-3000]
    val2 = text2[-3000:]
    
    test3 = text3[:-6000]
    train3 = text3[-6000:-3000]
    val3 = text3[-3000:]
    
    test4 = text4[:-6000]
    train4 = text4[-6000:-3000]
    val4 = text4[-3000:]
    
    
    with open(file+"_test.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(test)
    
    with open(file+"_train.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(train)
        
    with open(file+"_val.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(val)
        
    with open(file2+"_test.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(test2)
    
    with open(file2+"_train.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(train2)
        
    with open(file2+"_val.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(val2)
        
    with open(file3+"_test.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(test3)
    
    with open(file3+"_train.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(train3)
        
    with open(file3+"_val.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(val3)
        
    with open(file4+"_test.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(test4)
    
    with open(file4+"_train.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(train4)
        
    with open(file4+"_val.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(val4)
        
    return test,test2,test3,test4,train,train2,train3,train4,val,val2,val3,val4
    
        
    
        
if __name__ == "__main__":
    
    split2("Multi Model/Sentencepiece built on/Good_Cz.txt", "Multi Model/Sentencepiece built on/Good_En.txt", "Multi Model/Sentencepiece built on/Good_Es.txt", "Multi Model/Sentencepiece built on/Good_Pl.txt")
    
    
# =============================================================================
#     
#     """Get Additional Validation/test data"""
#     with open("Multi Model/Method1-separate tokenizers/Tsrc-test.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         print(len(data))
#         pl = data[:3000]
#         cz = data[3000:6000]
#         es = data[6000:9000]
#         
#     print(pl[0])
#     print(pl[-1])
#     print(cz[0])
#     print(cz[-1])
#     print(es[0])
#     print(es[-1])
#     
#     print(len(pl))
#     print(len(cz))
#     print(len(es))
#         
#     untag = re.compile(r"^<.*>\s", re.MULTILINE)
#     
#     cz2es_tgt = []
#     cz2es_src = []
#     
#     #Untag and tag
#     for i in range(len(pl)):
#         #Untag Polish
#         pl[i] = untag.sub(r"", pl[i])
#         #Untag spanish
#         es[i] = untag.sub(r"", es[i])
#         cz2es_tgt.append(es[i])
#         es[i] = "<2pl> "+es[i]
#         #Untag Czech
#         cz[i] = untag.sub(r"", cz[i])
#         cz[i] = "<2es> "+cz[i]
#         cz2es_src.append(cz[i])
#         cz[i] = "<2pl> "+cz[i]
#         
#     cz2pl_src = cz
#     es2pl_src = es
#     es2pl_tgt = pl
#     cz2pl_tgt = pl
#         
#     with open("Multi Model/Method1-separate tokenizers/Additional/add_test_src.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(cz2es_src + es2pl_src + cz2pl_src)
#         
#     with open("Multi Model/Method1-separate tokenizers/Additional/add_test_tgt.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(cz2es_tgt + es2pl_tgt + cz2pl_tgt)
#     
# =============================================================================
# =============================================================================
#     """Get Additional training data"""
#     with open("Multi Model/Method1-separate tokenizers/Tsrc-train.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         print(len(data))
#         pl = data[:328783]
#         cz = data[328783:657566]
#         es = data[657566:986349]
#         
#     print(pl[0])
#     print(pl[-1])
#     print(cz[0])
#     print(cz[-1])
#     print(es[0])
#     print(es[-1])
#     
#     print(len(pl))
#     print(len(cz))
#     print(len(es))
#         
#     untag = re.compile(r"^<.*>\s", re.MULTILINE)
#     
#     cz2es_tgt = []
#     cz2es_src = []
#     
#     #Untag and tag
#     for i in range(len(pl)):
#         #Untag Polish
#         pl[i] = untag.sub(r"", pl[i])
#         #Untag spanish
#         es[i] = untag.sub(r"", es[i])
#         cz2es_tgt.append(es[i])
#         es[i] = "<2pl> "+es[i]
#         #Untag Czech
#         cz[i] = untag.sub(r"", cz[i])
#         cz[i] = "<2es> "+cz[i]
#         cz2es_src.append(cz[i])
#         cz[i] = "<2pl> "+cz[i]
#         
#     cz2pl_src = cz
#     es2pl_src = es
#     es2pl_tgt = pl
#     cz2pl_tgt = pl
#         
#     with open("Multi Model/Method1-separate tokenizers/Additional/add_train_src.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(cz2es_src + es2pl_src + cz2pl_src)
#         
#     with open("Multi Model/Method1-separate tokenizers/Additional/add_train_tgt.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(cz2es_tgt + es2pl_tgt + cz2pl_tgt)
# =============================================================================
    
# =============================================================================
#     tag1("Multi Model/En_tok_test.txt2.txt", "Pl")
#     tag1("Multi Model/Es_tok_test.txt2.txt", "Cz")
#     tag1("Multi Model/Pl_tok_test.txt2.txt", "Cz")
#     tag1("Multi Model/Pl_tok_test.txt2 - Copy.txt", "Es")
# =============================================================================
    
# =============================================================================
#     tag1("Pl_tok.txt", "En")
#     tag1("Cz_tok.txt", "En")
#     tag1("Es_tok.txt", "En")
#     tag1("En_tok.txt", "Pl")
#     
#     stst1,stst2,stst3,stst4, strn1,strn2,strn3,strn4, sval1,sval2,sval3,sval4, = split2("Pl_tok.txttag.txt","Cz_tok.txttag.txt","Es_tok.txttag.txt","En_tok.txttag.txt")
#     
#     ttst1 = rmvtag("En_tok.txttag.txt_test.txt")
#     tval1 = rmvtag("En_tok.txttag.txt_val.txt")
#     ttrn1 = rmvtag("En_tok.txttag.txt_train.txt")
#     
#     ttst2 = ttst1
#     tval2 = tval1
#     ttrn2 = ttrn1
#     
#     ttst3 = ttst1
#     tval3 = tval1
#     ttrn3 = ttrn1
#     
#     ttst4 = rmvtag("Pl_tok.txttag.txt_test.txt")
#     tval4 = rmvtag("Pl_tok.txttag.txt_val.txt")
#     ttrn4 = rmvtag("Pl_tok.txttag.txt_train.txt")
#     
#     stst5 = tag1("En_tok.txttag.txt_test.txt", "Cz")
#     sval5 = tag1("En_tok.txttag.txt_val.txt", "Cz")
#     strn5 = tag1("En_tok.txttag.txt_train.txt", "Cz")
#     
#     ttst5 = rmvtag("Cz_tok.txttag.txt_test.txt")
#     tval5 = rmvtag("Cz_tok.txttag.txt_val.txt")
#     ttrn5 = rmvtag("Cz_tok.txttag.txt_train.txt")
#     
#     stst6 = tag1("En_tok.txttag.txt_test.txt", "Es")
#     sval6 = tag1("En_tok.txttag.txt_val.txt", "Es")
#     strn6 = tag1("En_tok.txttag.txt_train.txt", "Es")
#     
#     ttst6 = rmvtag("Es_tok.txttag.txt_test.txt")
#     tval6 = rmvtag("Es_tok.txttag.txt_val.txt")
#     ttrn6 = rmvtag("Es_tok.txttag.txt_train.txt")
#     
#     #I mixed up the train and validate from the return but they're the same size
#     with open("Tsrc-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(stst1+stst2+stst3+stst4+stst5+stst6)
#         
#     with open("Tsrc-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(strn1+strn2+strn3+strn4+strn5+strn6)
#         
#     with open("Tsrc-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(sval1+sval2+sval3+sval4+sval5+sval6)
#         
#     with open("Ttgt-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttst1+ttst2+ttst3+ttst4+ttst5+ttst6)
#     
#     with open("Ttgt-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttrn1+ttrn2+ttrn3+ttrn4+ttrn5+ttrn6)
#         
#     with open("Ttgt-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(tval1+tval2+tval3+tval4+tval5+tval6)
#     
#     
# =============================================================================
# =============================================================================
#     """Create Complete Model tokenized txt files"""
#     #En-Pl
#     tag1("En_tok.txt", "Pl")
#     rmvtag("Pl_tok.txt")
#     stst1, sval1, strn1 = split("En_tok.txt", True)
#     ttst1, tval1, ttrn1 = split("Pl_tok.txt", False)
#     
#     #En-Cz
#     tag1("En_tok.txt", "Cz")
#     rmvtag("Cz_tok.txt")
#     stst2, sval2, strn2 = split("En_tok.txt", True)
#     ttst2, tval2, ttrn2 = split("Cz_tok.txt", False)
#     
#     #En-Es
#     tag1("En_tok.txt", "Es")
#     rmvtag("Es_tok.txt")
#     stst3, sval3, strn3 = split("En_tok.txt", True)
#     ttst3, tval3, ttrn3 = split("Es_tok.txt", False)
#     
#     #Pl-En
#     tag1("Pl_tok.txt", "En")
#     rmvtag("En_tok.txt")
#     ttst4, tval4, ttrn4 = split("En_tok.txt", False)
#     stst4, sval4, strn4 = split("Pl_tok.txt", True)
#     
#     #Cz-En
#     tag1("Cz_tok.txt", "En")
#     rmvtag("En_tok.txt")
#     ttst5, tval5, ttrn5 = split("En_tok.txt", False)
#     stst5, sval5, strn5 = split("Cz_tok.txt", True)
#     
#     #Es-En
#     tag1("Es_tok.txt", "En")
#     rmvtag("En_tok.txt")
#     ttst6, tval6, ttrn6 = split("En_tok.txt", False)
#     stst6, sval6, strn6 = split("Es_tok.txt", True)
# =============================================================================
    
    
# =============================================================================
#     #I mixed up the train and validate from the return but they're the same size
#     with open("Tsrc-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(stst1+stst2+stst3+stst4+stst5+stst6)
#         
#     with open("Tsrc-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(strn1+strn2+strn3+strn4+strn5+strn6)
#         
#     with open("Tsrc-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(sval1+sval2+sval3+sval4+sval5+sval6)
#         
#     with open("Ttgt-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttst1+ttst2+ttst3+ttst4+ttst5+ttst6)
#     
#     with open("Ttgt-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttrn1+ttrn2+ttrn3+ttrn4+ttrn5+ttrn6)
#         
#     with open("Ttgt-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(tval1+tval2+tval3+tval4+tval5+tval6)
#     
# =============================================================================
# =============================================================================
#     """Create Complete Model tokenized txt files"""
#     #En-Pl
#     tag1("En_tok.txt", "Pl")
#     rmvtag("Pl_tok.txt")
#     stst1, sval1, strn1 = split("En_tok.txt", True)
#     ttst1, tval1, ttrn1 = split("Pl_tok.txt", False)
#     
#     #En-Cz
#     tag1("CZ_ENG.txtclean.txtout.txtout.txt", "Cz")
#     rmvtag("CZECH.txtclean.txtout.txtout.txt")
#     stst2, sval2, strn2 = split("CZ_ENG.txtclean.txtout.txtout.txtMulti.txt", True)
#     ttst2, tval2, ttrn2 = split("CZECH.txtclean.txtout.txtout.txtMulti.txt", False)
#     
#     #En-Es
#     tag1("CZ_ENG.txtclean.txtout.txtout.txt", "Es")
#     rmvtag("Spanish2M.txtclean.txtout.txtout.txt")
#     stst3, sval3, strn3 = split("CZ_ENG.txtclean.txtout.txtout.txtMulti.txt", True)
#     ttst3, tval3, ttrn3 = split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", False)
#     
#     #Pl-En
#     tag1("POLISH.txtclean.txtout.txtout.txt", "En")
#     rmvtag("CZ_ENG.txtclean.txtout.txtout.txt")
#     ttst4, tval4, ttrn4 = split("CZ_ENG.txtclean.txtout.txtout.txtMulti.txt", False)
#     stst4, sval4, strn4 = split("POLISH.txtclean.txtout.txtout.txtMulti.txt", True)
#     
#     #Cz-En
#     tag1("CZECH.txtclean.txtout.txtout.txt", "En")
#     rmvtag("CZ_ENG.txtclean.txtout.txtout.txt")
#     ttst5, tval5, ttrn5 = split("CZ_ENG.txtclean.txtout.txtout.txtMulti.txt", False)
#     stst5, sval5, strn5 = split("CZECH.txtclean.txtout.txtout.txtMulti.txt", True)
#     
#     #Es-En
#     tag1("Spanish2M.txtclean.txtout.txtout.txt", "En")
#     rmvtag("CZ_ENG.txtclean.txtout.txtout.txt")
#     ttst6, tval6, ttrn6 = split("CZ_ENG.txtclean.txtout.txtout.txtMulti.txt", False)
#     stst6, sval6, strn6 = split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", True)
#     
#     
#     #I mixed up the train and validate from the return but they're the same size
#     with open("Csrc-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(stst1+stst2+stst3+stst4+stst5+stst6)
#         
#     with open("Csrc-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(strn1+strn2+strn3+strn4+strn5+strn6)
#         
#     with open("Csrc-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(sval1+sval2+sval3+sval4+sval5+sval6)
#         
#     with open("Ctgt-test.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttst1+ttst2+ttst3+ttst4+ttst5+ttst6)
#     
#     with open("Ctgt-train.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(ttrn1+ttrn2+ttrn3+ttrn4+ttrn5+ttrn6)
#         
#     with open("Ctgt-val.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(tval1+tval2+tval3+tval4+tval5+tval6)
#     
# =============================================================================
    
# =============================================================================
#     
#     #For En-Pl Model
#     tag("CZ_ENG.txtclean.txtout.txtout.txt", "POLISH.txtclean.txtout.txtout.txt", "En", "Pl")
#     split("CZ_ENG.txtclean.txtout.txtout.txt", True)
#     split("POLISH.txtclean.txtout.txtout.txt", False)
#     #For Es-Cz Model
#     #tag("Spanish2M.txtclean.txtout.txtout.txt", "CZECH.txtclean.txtout.txtout.txt", "Es", "Cz")
#     tag1("Spanish2M.txtclean.txtout.txtout.txt", "Cz")
#     rmvtag("CZECH.txtclean.txtout.txtout.txt")
#     split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", True)
#     split("CZECH.txtclean.txtout.txtout.txtMulti.txt", False)
#     
#     tag1("CZECH.txtclean.txtout.txtout.txt", "Es")
#     rmvtag("Spanish2M.txtclean.txtout.txtout.txt")
#     split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", False)
#     split("CZECH.txtclean.txtout.txtout.txtMulti.txt", True)
#     #For Pl-Cz Model
#     #tag("POLISH.txtclean.txtout.txtout.txt", "CZECH.txtclean.txtout.txtout.txt", "Pl", "Cz")
#     tag1("POLISH.txtclean.txtout.txtout.txt", "Cz")
#     rmvtag("CZECH.txtclean.txtout.txtout.txt")
#     split("POLISH.txtclean.txtout.txtout.txtMulti.txt", True)
#     split("CZECH.txtclean.txtout.txtout.txtMulti.txt", False)
#     
#     tag1("CZECH.txtclean.txtout.txtout.txt", "Pl")
#     rmvtag("POLISH.txtclean.txtout.txtout.txt")
#     split("POLISH.txtclean.txtout.txtout.txtMulti.txt", False)
#     split("CZECH.txtclean.txtout.txtout.txtMulti.txt", True)
#     
#     
#     #For Pl-Es Model
#     #tag("POLISH.txtclean.txtout.txtout.txt", "Spanish2M.txtclean.txtout.txtout.txt", "Pl", "Es")
#     #tag1("POLISH.txtclean.txtout.txtout.txt", "Es")
#     #rmvtag("Spanish2M.txtclean.txtout.txtout.txt")
#     #split("POLISH.txtclean.txtout.txtout.txtMulti.txt", True)
#     #split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", False)
#     
#     
#     tag1("Spanish2M.txtclean.txtout.txtout.txt", "Pl")
#     rmvtag("POLISH.txtclean.txtout.txtout.txt")
#     split("POLISH.txtclean.txtout.txtout.txtMulti.txt", False)
#     split("Spanish2M.txtclean.txtout.txtout.txtMulti.txt", True)
#     
# =============================================================================
# =============================================================================
#     rmvtag("src-test.txt")
#     rmvtag("src-train.txt")
#     rmvtag("src-val.txt")
# =============================================================================
    
# =============================================================================
#     tag1("En-Pl_Model/src-test.txt", "Pl")
#     tag1("En-Pl_Model/src-train.txt", "Pl")
#     tag1("En-Pl_Model/src-val.txt", "Pl")
#     rmvtag("En-Pl_Model/tgt-test.txt")
#     rmvtag("En-Pl_Model/tgt-train.txt")
#     rmvtag("En-Pl_Model/tgt-val.txt")
# =============================================================================
    
# =============================================================================
#     tag1("En-Pl_Model/tgt-test.txt", "En")
#     tag1("En-Pl_Model/tgt-train.txt", "En")
#     tag1("En-Pl_Model/tgt-val.txt", "En")
#     rmvtag("En-Pl_Model/src-test.txt")
#     rmvtag("En-Pl_Model/src-train.txt")
#     rmvtag("En-Pl_Model/src-val.txt")
# =============================================================================
    
# =============================================================================
#     tag1("Es-Cz Model/nottoy-enpl/src-test.txt", "Cz")
#     tag1("Es-Cz Model/nottoy-enpl/src-train.txt", "Cz")
#     tag1("Es-Cz Model/nottoy-enpl/src-val.txt", "Cz")
#     rmvtag("Es-Cz Model/nottoy-enpl/tgt-test.txt")
#     rmvtag("Es-Cz Model/nottoy-enpl/tgt-train.txt")
#     rmvtag("Es-Cz Model/nottoy-enpl/tgt-val.txt")
# =============================================================================
    
# =============================================================================
#     tag1("Es-Cz Model/nottoy-enpl/tgt-test.txt", "Es")
#     tag1("Es-Cz Model/nottoy-enpl/tgt-train.txt", "Es")
#     tag1("Es-Cz Model/nottoy-enpl/tgt-val.txt", "Es")
#     rmvtag("Es-Cz Model/nottoy-enpl/src-test.txt")
#     rmvtag("Es-Cz Model/nottoy-enpl/src-train.txt")
#     rmvtag("Es-Cz Model/nottoy-enpl/src-val.txt")
# =============================================================================
    
# =============================================================================
# 
#     """Create Complete Model txt files"""
#     #En
#     en_test, en_val, en_train = split2("Cz_tok.txt", "Cz_tok")
#     
#     #Cz
#     cz_test, cz_val, cz_train = split2("En_tok.txt", "En_tok")
#     
#     #Es
#     es_test, es_val, es_train = split2("Es_tok.txt", "Es_tok")
#     
#     #Pl
#     pl_test, pl_val, pl_train = split2("Pl_tok.txt", "Pl_tok")
#     
# =============================================================================

# =============================================================================
#     rmvtag("tgt-test.txtMulti.txt")
#     rmvtag("tgt-train.txtMulti.txt")
#     rmvtag("tgt-val.txtMulti.txt")
#     
#     rmvtag("src-test.txt")
#     rmvtag("src-train.txt")
#     rmvtag("src-val.txt")
# =============================================================================
    
    #rmvtag("Es-Cz Model/src-test.txt")
    
    pass
    
    
    
    
    
    
    
    