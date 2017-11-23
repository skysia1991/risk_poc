#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by cmbfae-data @2017-11-10 14:17:04 
# Copyright 2017 NONE rights reserved.
"""
File descriptions in one line

more informations if needed
"""
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

def main():
    data = pd.read_csv('data/'+sys.argv[1], encoding='u8')
    train, test = train_test_split(data, test_size=0.3)
    train.to_csv('data/train.csv', index=False, encoding='u8')
    test.to_csv('data/test.csv', index=False, encoding='u8')
    return

    

if __name__ == '__main__':
    main()

