# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:50:50 2022

@author: Bryant McArthur
"""

import spacy

nlp_eng = spacy.load("en_core_web_md")
nlp_pol = spacy.load("pl_core_news_md")

"""
doc = nlp(u"I love coding. Geeks for Geeks helped me in this regard. Bryant is the coolest. yeah.")

for sent in doc.sents:
    print(sent)
    
print(type(doc.sents))
"""

print()
    
def sentence_segmenter(filename):
    with open(filename, 'r', encoding='utf-8') as myfile:
        data = myfile.read()
        doc = nlp_pol(data)
        
        sentences = list(doc.sents)
        
        sentences = [str(sentence) for sentence in sentences]
        
        with open(filename, 'w',encoding='utf-8') as outfile:
            newdata = '\n'.join(sentences)
            outfile.write(newdata)


if __name__ == "__main__":
    #sentence_segmenter("churchenglish200c.txt")
    sentence_segmenter("churchpolish200c.txt")
    #sentence_segmenter("short.txt")
    pass