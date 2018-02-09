# -*- coding: utf-8 -*-  
 
from builtins import int
from numpy import *

xy = []
labels = []
#数据路径用户根据自己存放位置更改
for line in open("D:/knn.txt"):  
    line_tmp = line.split()
    x = int(line_tmp[0])
    y = int(line_tmp[1])
    label = line_tmp[2]
    
    xy = [x,y]
    xy.append(xy) 
    
    labels.append(label)

train_set = array(xy)
    
print(train_set) 
print(labels) 
