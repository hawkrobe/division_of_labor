#!/bin/bash#
# parallel --bar --colsep ',' "sh ./run_RR_grid.sh {1} {2} {3} {4}" :::: input/coarse-grid.csv
# parallel --bar --colsep ',' "sh ./run_RR_grid.sh {1} {2} {3} {4}" :::: input/fine-grid.csv
webppl RR_simulations.wppl --require ./refModule/ --require webppl-csv -- --perspectiveCost $1 --alpha $2 --uttCost $3 --chainNum $4
