#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by cmbfae-data @2017-11-10 13:56:33 
# Copyright 2017 NONE rights reserved.
"""
File descriptions in one line

more informations if needed
"""
import pandas as pd

negative_const = 377

def lift_at_n(df, n):
    df.sort_values(by='XGB', ascending=False, inplace=True)
    new_df = df.iloc[:n]
    return new_df['Label'].sum()*1.0/negative_const
    
def main():
    result = pd.read_csv('data/result.csv', encoding='u8')
    for n in xrange(400, 6000, 1000):
        print n, lift_at_n(result, n)
    

if __name__ == '__main__':
    main()

