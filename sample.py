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
    
def main():
    data = pd.read_csv('data/data_set_end_171116_fixRate.csv', encoding='u8')
    data = data[data[u'贷款期数（月）'] > 3]
    train, test = train_test_split(data, test_size=0.3)
    train.to_csv('data/train.csv', index=False, encoding='u8')
    test.to_csv('data/test.csv', index=False, encoding='u8')
    print train[u'标注'].value_counts()
    print test[u'标注'].value_counts()
    return

    

if __name__ == '__main__':
    main()

