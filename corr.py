#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by cmbfae-data @2017-11-10 17:12:59 
# Copyright 2017 NONE rights reserved.
"""
File descriptions in one line

more informations if needed
"""
import pandas as pd

def main():
    data = pd.read_csv('data/train.csv', encoding='u8')
    label = data[u'标注']
    corr_dict = dict()
    for col in data.columns:
        if data[col].dtype == 'int64' or data[col].dtype == 'float64':
            corr_dict[col] = data[col].corr(label)

    l = sorted(corr_dict, key=corr_dict.get, reverse=True)
    for key in l:
        print key, corr_dict[key]
    return
        

if __name__ == '__main__':
    main()

