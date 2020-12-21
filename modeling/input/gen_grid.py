import csv
import numpy as np

chainNum = 1
with open('coarse-grid.csv', 'w') as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    for alpha in [x for x in np.linspace(1,10,num=9)] :
        for perspectiveCost in np.linspace(0, 1, num=21) :
            for uttCost in [0.0001, 0.001, 0.009, 0.01, 0.02, 0.03, 0.05, 0.075, 0.1] :
                writer.writerow([round(perspectiveCost, 2), round(alpha,2), round(uttCost, 2), chainNum])
                chainNum = chainNum + 1

chainNum = 40000
with open('fine-grid.csv', 'w') as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    for perspectiveCost in np.linspace(0, 0.5, num=21) :
        writer.writerow([perspectiveCost, 2, 0.03, chainNum])
        chainNum = chainNum + 1
