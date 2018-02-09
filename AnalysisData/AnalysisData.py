#!/usr/bin/env python
# -*- coding: utf-8 

import matplotlib.pyplot as plt

x_list_r = []
y_list_r = []

x_list_g = []
y_list_g = []

#数据路径用户根据自己存放位置更改
for line in open("D:/knn.txt"):  
    line_list = line.split()
    x_int = int(line_list[0])
    y_int = int(line_list[1])
    label = line_list[2]
    
    if label == '1':
        x_list_r.append(x_int)
        y_list_r.append(y_int)
    else:
        x_list_g.append(x_int)
        y_list_g.append(y_int)


plt.scatter(x_list_r, y_list_r, c = 'r')
plt.scatter(x_list_g, y_list_g, c = 'g')
plt.show()