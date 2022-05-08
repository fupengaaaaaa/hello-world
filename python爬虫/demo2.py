# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:35:28 2022

@author: Administrator
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
# df=pd.read_excel('C:/Users\Administrator\Desktop\data1.xlsx', 
#                  sheet_name=1, header=0)
# print(type(df))
# print(df)
# print('*'*100)
# print(df.loc[0]['A'])
# print(df['A'][0])
# print('-'*100)
# df['B'][0]=100
# print(df)
# df.loc[0]=9
# print(df)
# print(df.index)
# print(df.columns)
 
# print(df)
# print(df.values)

# df=pd.DataFrame(df.values, index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
# df.loc['d']=['张一', 3, 'd']
# print(df.loc['d']['A'])
# print(df)

# plt.figure(figsize=(10,10), dpi=1000, facecolor='w', frameon=True)
# plt.rcParams['font.family']='SimHei'
# plt.rcParams['axes.unicode_minus']=False
# a=np.linspace(0, 10, 100)
# plt.plot(a, np.sin(a), label='sin(x)')
# plt.legend(loc='upper right')
# plt.xticks([0,1,2,3,4,5,6,7])
# plt.yticks([-2,-1,0,1,2],['曹县', '北京', '上海', '广州', '深圳'])
# plt.title('sinx', fontsize=20)
# plt.xlim(0,8)
# plt.ylim(-2,3)
# plt.xlabel('时间')
# plt.ylabel('路程')    
# plt.grid(True)
# plt.savefig('1.jpg')
# plt.show()


# li=[1,23,33,45,56,67,44,55,33]
# num, bins, patch=plt.hist(li,bins=4, edgecolor='b')
# plt.xticks(bins)
# print(num, bins, patch)
# for num,bins in zip(num,bins):
#     plt.annotate(num, (bins,num),(bins+7,num+0.05))
# plt.show()




bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
make_snapshot(snapshot, bar.render(),'bar.png')







