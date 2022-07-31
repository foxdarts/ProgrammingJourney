# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 08:56:41 2020

@author: fox
"""


assets = {} #creates dictionary of assets
assets['tag1'] = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
assets['tag2'] = 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34
assets['tag3'] = 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 #fills 3 keys within dictionary with values


for N, (K, V) in enumerate(assets.items()): # enumerates values in all keys in dictionary
    print(N, K, V) #N = Number, K = key, V = Value
    
print (assets.keys())
print (assets.values())

assets['newtag1'] = assets['tag1'] # renames key 1 in assets 
del assets['tag1']

print (assets.keys())
print (assets.values())
