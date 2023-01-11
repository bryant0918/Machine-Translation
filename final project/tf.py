# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:04:32 2022

@author: bryan
"""

import tensorflow as tf
import os

print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

os.system("head -n 2 toy-ende/src-train.txt")