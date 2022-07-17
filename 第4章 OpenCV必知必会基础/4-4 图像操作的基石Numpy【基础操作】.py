"""
创建数组 array()
创建全0数组 zeros()/ones
创建全值数组full()
创建单元数组 identity/eye()
"""

from cgi import print_form
import numpy as np

#
# # 一维数组
# a = np.array([2, 3, 4])
# print(a)
#
# # 二维数组
# c = np.array([[1.0, 2.0], [3.0, 4.0]])
# print(c)

# # 行的个数，列的个数，通道数/层数，数据类型
# 定义zeros矩阵
c = np.zeros((4, 5, 3), np.uint8)  # 数组数、行、列
print(c)

#  定义ones矩阵
d = np.ones((4,3,3),np.uint8)
print(d)

#  定义full矩阵
e = np.full((8,8), 0, np.uint8)
print(e)

#  定义单位矩阵
f = np.identity(4)
print(f)

# 
g = np.eye(5,7,k=3)
print(g)
