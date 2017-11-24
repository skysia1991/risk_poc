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

def extract(x, k, f1, f2):
    n = int(x[f2]) - k
    l = x[f1].split('|')
    for elm in l:
        v = elm.split(':')
        if int(v[0]) == n:
            return int(float(v[1]))
    raise Exception('no such period')

def data_transfer(df, n):
    f_list = [u'历史最长逾期天数',u'已还本金（元）',u'逾期本金（元）',u'已还利息（元）',u'剩余本金（元）',u'剩余利息（元）']
    f_num = u'贷款期数（月）'
    for f in f_list:
        df[f] = df.apply(extract, axis=1, args=(n,f,f_num,))
    
    df[u'历史逾期次数'] = df.apply(extract, axis=1, args=(n-1,u'历史逾期次数', f_num,))
    f = u'本期逾期天数'
    for i in xrange(n+1, n+2):
        df[f+'_'+str(i)+'th'] = df.apply(extract, axis=1, args=(i,f,f_num,))
    del df[f]
    return df


def main():
    data = pd.read_csv('data/'+sys.argv[1], encoding='u8')
    data = data[data[u'贷款期数（月）'] > int(sys.argv[3])]
    pre_n = int(sys.argv[2])
    new_data = data_transfer(data, pre_n)
    train, test = train_test_split(new_data, test_size=0.3)
    train.to_csv('data/train.csv', index=False, encoding='u8')
    test.to_csv('data/test.csv', index=False, encoding='u8')
    return

if __name__ == '__main__':
    main()
