# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:45:15 2022

@author: bryan
"""

"""Make quick plot"""

from matplotlib import pyplot as plt
import numpy as np


data = [[22,24,16,18],[78,76,84,82]]
X = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25, label="NMT")
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25, label="Ref")
ax.legend(loc=0)
ax.set_xticks(X)
ax.set_xticklabels(("En-Pl","Pl-Es","Es-Cz","Pl-Cz"))
plt.title("Bilingual performance vs Reference")


