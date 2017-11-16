#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by cmbfae-data @2017-11-10 13:56:33 
# Copyright 2017 NONE rights reserved.
"""
File descriptions in one line

more informations if needed
"""
import pandas as pd

from sklearn.metrics import roc_auc_score

import sys

money_const = 2645239.2058

def lift_at_n(df, n, pos):
    df.sort_values(by='XGB', ascending=False, inplace=True)
    new_df = df.iloc[:n]
    return new_df['Label'].sum()*1.0/pos
    
def rateOfBadAccount(df, money):
    df.sort_values(by='XGB', inplace=True)
    n = len(df)
    label_sum = 0
    index = 0
    total_money = money
    while (money > 0):
        if (index > n):
            raise Exception('There is not enough money to pick')
        elm = df.iloc[index, :]
        label_sum += elm['Label']
        money -= 1
        index += 1

    return label_sum, total_money, label_sum*1.0/total_money
        
def pickAccount(df, money):
    df.sort_values(by='XGB', inplace=True)
    n = len(df)
    label_sum = 0
    index = 0
    candidates = list()
    while (money > 0):
        if (index > n):
            raise Exception('There is not enough money to pick')
        elm = df.iloc[index, :]
        money -= elm['Money']
        index += 1

    return df.iloc[:index, :]


def auc(df):
    return roc_auc_score(df['Label'], df['XGB'])
    
def main():
    result = pd.read_csv('data/result.csv', encoding='u8')
    metric = sys.argv[1]

    if metric == 'lift':
        try:
            n = int(sys.argv[2])
        except:
            raise Exception('Please enter the n number')
        pos = result['Label'].sum() 
        print "the %d lift is %lf" %(n, lift_at_n(result, n, pos))

    #if metric == 'rateOfBadAccount':
    #    print rateOfBadAccount(result, num - pos_num)

    if metric == 'auc':
        print "The auc score is %lf" %(auc(result))

    #rlt = pickAccount(result, money_const)
    #rlt[['ID', 'XGB', 'Money']].to_csv('data/final_result.csv', index=False, encoding='u8')
    
    raise Exception('This metris is not supported now')
    
    return

if __name__ == '__main__':
    main()

