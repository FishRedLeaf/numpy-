# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:52:42 2018

@author: Administrator
如果两个数组的维数不相同，则元素到元素的操作是不可能的。 
然而，在 NumPy 中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能。 
较小的数组会广播到较大数组的大小，以便使它们的形状可兼容。

如果满足以下规则，可以进行广播：
ndim较小的数组会在前面追加一个长度为 1 的维度。
输出数组的每个维度的大小是输入数组该维度大小的最大值。
如果输入在每个维度中的大小与输出大小匹配，或其值正好为 1，则可以进行计算。
如果输入的某个维度大小为 1，则该维度中的第一个数据元素将用于该维度的所有计算。

如果上述规则产生有效结果，并且满足以下条件之一，那么数组被称为可广播的。
数组拥有相同形状。
数组拥有相同的维数，每个维度拥有相同长度，或者长度为 1。
数组拥有极少的维度，可以在其前面追加长度为 1 的维度，使上述条件成立。
"""

import numpy as np 

x = np.array([1,2,3,4]) 
y = np.array([10,20,30,40]) 
z = x * y 
print(x);print(y);print(z)

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])
print(a);print(b);print(a+b)

'''注意广播操作一般只在两个数组间进行'''
  