#!/usr/bin/env python
# -*- coding: utf-8  

from builtins import int
from numpy import *
from BasicKNN.KNN import knn_classifier

#导入数据
xy = []
labels = []
#数据路径用户根据自己存放位置更改
for line in open("D:/knn.txt"):  
    line_tmp = line.split()
    x = int(line_tmp[0])
    y = int(line_tmp[1])
    label = line_tmp[2]
    
    point = [x,y]
    xy.append(point) 
    
    labels.append(label)

train_set = array(xy)

#开始测试
validation_set = array([15676, 173])
k = 3
outputLabel = knn_classifier(validation_set, train_set, labels, 3)
print ("验证数据:", validation_set, "模型计算标签: ", outputLabel)
