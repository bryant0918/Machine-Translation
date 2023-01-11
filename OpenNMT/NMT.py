# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:55:23 2022

@author: Bryant McArthur
"""

import os

#os.system('pip install OpenNMT-py')

#os.system('head -n 2 nottoy-enpl/src-train.txt')

os.system('onmt_build_vocab -config nottoy_en_pl_yaml.txt -n_sample 50000')

os.system('onmt_train -config nottoy_en_pl_yaml.txt')