# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:16:55 2022

@author: bryant mcarthur
"""

import comet
from comet.models import download_model


def cohen(source, hypothesis, reference):
    """This uses comet to evaluate my MT system"""
    model = download_model("wmt-large-da-estimator-1719")
    data = {"src": source, "mt": hypothesis, "ref": reference}
    data = [dict(zip(data, t)) for t in zip(*data.values())]
    #print(model.predict(data, cuda = True, show_progress = True))
    return model.predict(data, cuda = False, show_progress = True)
    
    
with open("churchenglish1k.txt", 'r', encoding = 'utf-8') as myfile:
    source = myfile.readlines()
    
with open("churchpolish1k.txt", 'r', encoding = 'utf-8') as myfile:
    reference = myfile.readlines()
    
with open("GoogleTranslate1k.txt", 'r', encoding = 'utf-8') as myfile:
    hyp1 = myfile.readlines()
    
with open("Sys1k.txt", 'r', encoding = 'utf-8') as myfile:
    hyp2 = myfile.readlines()
    

print(cohen(source, hyp1, reference))
print(cohen(source, hyp2, reference))
    
