# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:12:47 2022

@author: Bryant McArthur
"""



if __name__ == "__main__":
    
    import torch
    import os
    
    print(torch.version.cuda)
    print(torch.cuda.is_available())
    torch.cuda.init()
    print(torch.cuda.is_initialized())
    print(torch.cuda.get_device_name())
    print(torch.cuda.current_device())
    
    
    os.system("pip install OpenNMT-py")
    #Add C:\\Users\\bryan\\OneDrive\\Documents\\Winter 2022\\CS 401R\\Final Project\\
    os.system('onmt_build_vocab -config nottoy_en_pl.yaml -n_sample 40000')
    

# =============================================================================
# import os
# import subprocess
# from torch import cuda
# 
# print(cuda.is_available())
# cuda.init()
# print(cuda.is_initialized())
# print(cuda.get_device_name())
# print(cuda.current_device())
# 
# #pip install OpenNMT-py
# x = os.system("head -n 2 toy-ende/src-train.txt")
# print(x)
# 
# args = ["head","-n 2", "C:\\Users\\bryan\\OneDrive\\Documents\\Winter 2022\\CS 401R\\OpenNMT\\churchenglish.txt"]
# x = subprocess.run(args, capture_output=True)
# print("#####")
# print(x.returncode)
# print(x.stdout.decode("utf-8"))
# #x = subprocess("head -n 2 toy-ende/src-train.txt")
# 
# #!onmt_build_vocab -config toy_en_de.yaml -n_sample 10000
# 
# #!onmt_train -config toy_en_de.yaml
# 
# #!onmt_translate -model toy-ende/run/model_step_1000.pt -src toy-ende/src-test.txt -output toy-ende/pred_1000.txt -gpu 0 -verbose
# 
# os.system("echo hello world")
# =============================================================================

