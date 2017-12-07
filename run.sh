#!/bin/bash
#Setting the n
term=$1
#if [ $term > 5 ];then
#thres_term=3
#else
#thres_term=6
#fi

#python sample.py data_set_20171123.csv $term $thres_term

~/anaconda2/bin/python main.py 100 Rand_yuqibenjin

#if $num < 5;then
for i in 400 900 1400 2500 4500;
do
python metric.py lift $i;
done
#else
#for i in 200 400 500 600 800;
#do
#python metric.py lift $i;
#done

python metric.py auc

#run metric introduction
#for lift
#python metric.py lift 100
#for auc
#python metric.py auc
