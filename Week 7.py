import os
import pandas as pd

# Pandas Indexing

# # Pandas Series Example
# # Ex. 1
data = [100, 200, 300, 400, 500, 600, 700, 800]
date = ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07', '10-08']
ser = pd.Series(data=date, index=date)
# print(ser)

# # some attributes
# print(ser.size)
# print(ser.shape) 纬度, tuple
# print(ser.dtype) 混合, 不都是字符串
# print(ser.index)

# object - string (整数, 字符串混合都会显示 object)

#indexing/selection elements - 3 ways
# .iloc - index/position based - 按照位置
# .loc - label based - 按照index名字
# [] label + position with confusing notations - 不推荐

print(ser)
#
# # Series index - select single row - third row
# # .iloc
d = ser.iloc[2]
# print(d)
# print(ser.iloc[2]) # 返回得失第三行的data

# # .loc
# print(ser.loc['10-03'])
# # [] - 不推荐使用在series里，尤其涉及到row label
# print(ser['10-03']) # 可行， 因为series有'10-03'这个index名 .loc[]
# print(ser[2]) # 造成困惑，此时执行的是.iloc的indexing方法

# index - 回忆list的知识点， -2代表从倒数第二个元素 -1倒数第一
# print(ser.iloc[-2])
# 也可以打印倒数的顺序
# print(ser.iloc[::-1])

# print(ser.iloc[1:5:2])
