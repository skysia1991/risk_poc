#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by cmbfae-data @2017-11-23 15:19:58 
# Copyright 2017 NONE rights reserved.
"""
File descriptions in one line

more informations if needed
"""
def extract(x, n):
    l = x.split('|')
    for elm in l:
        v = elm.split(':')
        if v[0] == n:
            return v[1]
    raise Exception('no such period')

def run():
    num = 12
    for i in xrange(2, num):
        df[str(i)+'th'] = df[u'历史逾期次数'].apply(extract, arg=(i,))


def main():
    hello()

if __name__ == '__main__':
    main()

