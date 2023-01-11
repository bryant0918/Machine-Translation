# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:20:05 2022

@author: bryan
"""

import urllib.request
import io
import sentencepiece as spm

# Loads model from URL as iterator and stores the model to BytesIO.
model = io.BytesIO()
with urllib.request.urlopen(
    'https://raw.githubusercontent.com/google/sentencepiece/master/data/botchan.txt'
) as response:
  spm.SentencePieceTrainer.train(
      sentence_iterator=response, model_writer=model, vocab_size=5000)

# Serialize the model as file.
with open('out.model', 'wb') as f:
    f.write(model.getvalue())

# Directly load the model from serialized model.
sp = spm.SentencePieceProcessor(model_proto=model.getvalue())
print(sp.encode('this is test', out_type=str))

#spm.SentencePieceTrainer.Train(input=)