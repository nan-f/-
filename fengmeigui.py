# !/usr/bin/env python
# -*- coding=UTF-8 -*-


from pylab import *
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Arrow
import matplotlib
import numpy as np
import pandas as pd


mpl.rcParams['font.sans-serif'] = ['SimHei']  #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False      #解决保存图像是负号'-'显示为方块的问题

address = '/Users/fangnan/Desktop/shuju.xlsx'
data = pd.read_excel(address, index_col='No.')

Dip = data['Dip'].values.tolist()

fig = plt.figure(figsize=(7, 6))
sub = fig.add_subplot(111)

#设置大圆半径R=1
#生成投影网外圆
an = np.linspace(0,np.pi,100)
sub.plot(np.cos(an), np.sin(an) )
sub.plot(0.2*np.cos(an), 0.2*np.sin(an), color='blue')
sub.plot(0.4*np.cos(an), 0.4*np.sin(an), color='blue')
sub.plot(0.6*np.cos(an), 0.6*np.sin(an), color='blue')
sub.plot(0.8*np.cos(an), 0.8*np.sin(an), color='blue')

#生成投影网刻度
s = np.linspace(0,np.pi,19)
for ang in s:
    l = Line2D([np.cos(ang), 0*np.cos(ang)], [np.sin(ang), 0*np.sin(ang)])
    sub.add_line(l)
sub.text(-0.30, 1.20, u'节理走向玫瑰花图', fontsize=16)
sub.text(0, 1.05, 'N')
sub.text(1.05,  0, 'E')
sub.text(-1.05, 0, 'W')
sub.text(0.15, -0.05, '30')
sub.text(0.35, -0.05, '60')
sub.text(0.55, -0.05, '90')
sub.text(0.75, -0.05, '120')
sub.text(0.95, -0.05, '150')
sub.add_line(Line2D([-0.05,0.05],[0, 0]))
sub.add_line(Line2D([0, 0],[-0.05,0.05]))

# 统计走向区间
# sorted(self.Dip)
a = [[]]
for i in range(0, 36):
    num = 0
    sum = 0
    # print j,Dip[j]
    for j in range(0, len(Dip)):
        if Dip[j] >= (i * 10) and Dip[j] < (i * 10 + 10):
            # print(j)
            a[i].append(Dip[j])
            num = num + 1
            sum = sum + Dip[j]
    a[i].append(num)
    # print num
    if num == 0:
        a[i].append(0)
    else:
        a[i].append(sum / num)
        # print(a[i][-2],a[i][-1])
    a.append([])

x = [0, ]
y = [0, ]
for i in range(17, -1, -1):
    # print(a[i][-2],a[i][-1])
    t1 = (a[i][-2] + a[i + 18][-2]) / 150.0
    if 0 == t1:
        t2 = 0
    else:
        t2 = (a[i][-2] * (180 - a[i][-1]) + a[i + 18][-2] * (360 - a[i + 18][-1])) / (a[i][-2] + a[i + 18][-2])
    # print(t1,t2)
    x.append(t1 * np.cos(t2 / 180 * np.pi))
    y.append(t1 * np.sin(t2 / 180 * np.pi))

x.append(0)
y.append(0)
sub.fill(x, y, 'r')
sub.plot(x, y)

show()

