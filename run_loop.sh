#!/bin/bash

for ((j=9;j<=12;j=j+1)); do (for ((i=0;i<10;i=i+1)); do bash run.sh $j; done>output_$j.txt) done;
