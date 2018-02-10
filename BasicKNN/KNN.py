#!/usr/bin/env python
# -*- coding: utf-8 

from numpy import *

def knn_classifier(validation_set, train_set, labels, k):
    #计算矩阵行数，即样本数量
    num_samples = train_set.shape[0] 
    #diff是输入样本与每个训练样本的差值矩阵
    diff = tile(validation_set, (num_samples, 1)) - train_set 
    #把diff平方
    squared_diff = diff ** 2 
    #按照每个样本行进行累加
    squared_dist = sum(squared_diff, axis = 1) 
    #开根号计算距离     
    distance = squared_dist ** 0.5
    
    #将distance按照升序排序，返回值是下标
    sorted_dist_indices = argsort(distance)

    #存放最终的分类结果及相应的结果投票数 
    class_count = {} 
    #循环投票，统计前k个最近的样本所属类别包含的样本个数 
    for i in range(k):
        
        #sortedDistIndicies[i]是第i个最相近的样本下标 
        #voteLabel：样本对应的分类结果
        vote_label = labels[sorted_dist_indices[i]]

        #将所属类型票数加1
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    max_count = 0
    #循环唱票，找出票数最多的分类
    for key, value in class_count.items():
        if value > max_count:
            max_count = value
            max_index = key

    return max_index    