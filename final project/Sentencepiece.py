# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:20:05 2022

@author: bryant
"""

import sentencepiece as spm


def get_models():
# =============================================================================
#     spm.SentencePieceTrainer.Train(input="English2M.txtclean.txtout.txtout.txt", model_prefix='en2', vocab_size=8000)
#     spm.SentencePieceTrainer.Train(input="Spanish2M.txtclean.txtout.txtout.txt", model_prefix='es2', vocab_size=16000)
#     spm.SentencePieceTrainer.Train(input="CZECH.txtclean.txtout.txtout.txt", model_prefix='cz2', vocab_size=16000)
#     spm.SentencePieceTrainer.Train(input="POLISH.txtclean.txtout.txtout.txt", model_prefix='pl2', vocab_size=16000)
# =============================================================================

    spm.SentencePieceTrainer.Train(input="Good_En.txt", model_prefix='en2', vocab_size= 7000)
    spm.SentencePieceTrainer.Train(input="Good_Es.txt", model_prefix='es2', vocab_size = 7000)
    spm.SentencePieceTrainer.Train(input="Good_Cz.txt", model_prefix='cz2', vocab_size= 11000)
    spm.SentencePieceTrainer.Train(input="Good_Pl.txt", model_prefix='pl2', vocab_size= 11000)
    
    spm.SentencePieceTrainer.Train(input="fullcorpus.txt", model_prefix='full', vocab_size= 25000)
    
    
#get_models()


def tokenize(file, src_lang):
    
    if src_lang == "Pl":
        sp = spm.SentencePieceProcessor(model_file="Sentencepiece built on/pl2.model")
    elif src_lang == "Cz":
        sp = spm.SentencePieceProcessor(model_file="Sentencepiece built on/cz2.model")
    elif src_lang == "Es":
        sp = spm.SentencePieceProcessor(model_file="Sentencepiece built on/es2.model")
    elif src_lang == "En":
        sp = spm.SentencePieceProcessor(model_file='Sentencepiece built on/en2.model')
    elif src_lang == "full":
        sp = spm.SentencePieceProcessor(model_file='Sentencepiece built on/full.model')
    else:
        raise ValueError("language given not in domain")
    
    with open(file, 'r', encoding = "utf-8") as myfile:
        data = myfile.readlines()
        print(len(data))
        
    for i in range(len(data)):
        data[i] = " ".join(sp.encode(data[i], out_type=str))+"\n"
        if i ==0:
            print(data[i])
    
    with open(src_lang+"_tok.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(data)
        
        
        
def untokenize(file, src_lang):
    if src_lang == "Pl":
        sp = spm.SentencePieceProcessor(model_file="Multi Model/Sentencepiece built on/pl2.model")
    elif src_lang == "Cz":
        sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/cz.model")
    elif src_lang == "Es":
        sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/es.model")
    elif src_lang == "En":
        sp = spm.SentencePieceProcessor(model_file='Sentencepiece built on/en2.model')
    elif src_lang == "full":
        sp = spm.SentencePieceProcessor(model_file='Sentencepiece built on/full.model')
    else:
        raise ValueError("language given not in domain")
        
    with open(file, 'r', encoding = "utf-8") as myfile:
        data = myfile.readlines()
        print(len(data))
        
    for i in range(len(data)):
        data[i] = sp.decode(data[i].split())+"\n"
        if i ==0:
            print(data[i])
        
    with open(src_lang+"_OUT.txt", 'w', encoding = "utf-8") as outfile:
        outfile.writelines(data)

if __name__ == "__main__":
    
    #untokenize("Es-Cz Model/From Google Colab/Tokens/pred_88000.txt", "Cz")
    untokenize("Pl-Cz Model/Google Colab/Tokens/pred_88000.txt", "Cz")
    untokenize("Pl-Es Model/From Colab/Tokens/pred_88000.txt", "Es")
    
    #tokenize("Method1-separate tokenizers/Demo/En-pl_Demo.txt", "En")
    #tokenize("Method1-separate tokenizers/Demo/Es-cz_Demo.txt", "Es")
    #tokenize("Method1-separate tokenizers/Demo/Pl-cz_Demo.txt", "Pl")
    #tokenize("Method1-separate tokenizers/Demo/Pl-es_Demo.txt", "Pl")
    
# =============================================================================
#     tokenize("Spanish2M.txtclean.txtout.txtout.txt", "Es")
#     tokenize("CZECH.txtclean.txtout.txtout.txt", "Cz")
#     tokenize("POLISH.txtclean.txtout.txtout.txt", "Pl")
#     tokenize("English2M.txtclean.txtout.txtout.txt", "En")
# =============================================================================
    #untokenize("pred_40000.txt", "Cz")
    
    #untokenize("Method2-same tokenizer/En-pl_ref.txt", "Pl")
# =============================================================================
#     untokenize("Method1-separate tokenizers/Es-cz_ref.txt", "Cz")
#     untokenize("Method1-separate tokenizers/Pl-cz_ref.txt", "Cz")
#     untokenize("Method1-separate tokenizers/Pl-es_ref.txt", "Es")
# # =============================================================================
# =============================================================================
#     sentence = "elemento añadido a"
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/es.model")
#     y = sp.encode(sentence, out_type=str)
#     print(" ".join(y))
# =============================================================================
# =============================================================================
#     sentence = "▁paweł ▁wyjaśnił , ▁jak ▁abraham ▁został ▁usprawiedliwion y ▁poprzez ▁łaskę"
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/pl.model")
#     print(sp.decode(sentence.split()))
# =============================================================================
    
    
# =============================================================================
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/en.model")
#     
#     with open("test1.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         
#     for i in range(len(data)):
#         data[i] = sp.decode(data[i].split())+"\n"
#         
#     with open("En-pl_Demo.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(data)
#         
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/es.model")
#     
#     with open("test2.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         
#     for i in range(len(data)):
#         data[i] = sp.decode(data[i].split())+"\n"
#         
#     with open("Es-cz_Demo.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(data)
#     
#     
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/pl.model")
#     
#     with open("test3.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         
#     for i in range(len(data)):
#         data[i] = sp.decode(data[i].split())+"\n"
#         
#     with open("Pl-es_Demo.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(data)
#     
#     sp = spm.SentencePieceProcessor(model_file="Sentencepiece models/pl.model")
#     
#     with open("test4.txt", 'r', encoding = "utf-8") as myfile:
#         data = myfile.readlines()
#         
#     for i in range(len(data)):
#         data[i] = sp.decode(data[i].split())+"\n"
#         
#     with open("Pl-cz_Demo.txt", 'w', encoding = "utf-8") as outfile:
#         outfile.writelines(data)
# =============================================================================
        
    
    

    pass


