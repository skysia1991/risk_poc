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
    num = len(result)
    pos_num = int(num * 0.8)
    pos = result['Label'].sum() 
    for n in range((pos/100 + 1)*100, pos_num, 1000):
        print n, lift_at_n(result, n, pos)

    print rateOfBadAccount(result, num - pos_num)

    try:
        print "The auc score is %lf" %(auc(result))
    except:
        pass

    rlt = pickAccount(result, money_const)
    rlt[['ID', 'XGB', 'Money']].to_csv('data/final_result.csv', index=False, encoding='u8')

    return

if __name__ == '__main__':
    main()

