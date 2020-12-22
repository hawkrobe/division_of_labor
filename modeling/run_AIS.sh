#!/bin/bash#
# parallel --bar --colsep ',' "sh ./run_AIS.sh {1} {2}" :::: input/BF_grid.csv 
webppl BDA.wppl --require ./refModule/ --require webppl-csv -- --chainNum $1 --model $2 --AIS true
