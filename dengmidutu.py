# !/usr/bin/env python
# -*- coding=UTF-8 -*-


from pylab import *
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Arrow
from matplotlib.tri import Triangulation
import numpy as np
import pandas as pd


mpl.rcParams['font.sans-serif'] = ['SimHei']  #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False      #解决保存图像是负号'-'显示为方块的问题

address = '/Users/fangnan/Desktop/shuju.xlsx'
data = pd.read_excel(address, index_col='No.')

Dip = data['Dip'].values.tolist()
Dia = data['Dia'].values.tolist()

fig = plt.figure(figsize=(7, 6))
sub = fig.add_subplot(111)

#设置大圆半径R=1
#生成投影网外圆
#an = np.linspace(0,2*np.pi,100)
#plt.plot( np.cos(an), np.sin(an), color='white')
sub.text(-0.4, 1.15, u'节理极点等密度图', fontsize=16)
sub.text(0, 1.05, 'N')
sub.text(1.05,  0, 'E')
sub.text(-1.15, 0, 'W')
sub.text(0, -1.1, 'S')

#极点坐标
def f1(x, y):
    return 1.5*np.sqrt(2)*np.sin(x/180*np.pi/2)*np.sin(y/180*np.pi)
def f2(x, y):
    return 1.5*np.sqrt(2)*np.sin(x/180*np.pi/2)*np.cos(y/180*np.pi)
x = []
y = []
for nmb in range(0, len(Dip)):
    x.append(f1(Dia[nmb], Dip[nmb]))
    y.append(f2(Dia[nmb], Dip[nmb]))
    #sub.plot(x[-1],y[-1], 'r.')

#统计极点个数
num = []
x0 = []
y0 = []
i = -10
while i<=10:
    #print('i =',i)
    #num.append([])
    j=-10
    while j<=10:
        #print('j =',j)
        if np.sqrt((0.1*i)**2+(0.1*j)**2)<=1:
            x0.append(0.1*i)
            y0.append(0.1*j)
            #num[-1].append(0)
            num.append(0)
            #print('%.1f' % x[-1],'%.1f' % y[-1])
            k=0
            while k<len(x):
                bn = np.sqrt((0.1*i-x[k])**2+(0.1*j-y[k])**2)
                if bn <= 0.1:
                    #num[-1][-1]=num[-1][-1]+1
                    num[-1]=num[-1]+1
                k=k+1
        j=j+1
    i=i+1
#print(num)
s = np.linspace(0,2*np.pi,37)
for ang in s:
    #l = Line2D([np.cos(ang), 1.02*np.cos(ang)], [np.sin(ang), 1.02*np.sin(ang)])
    #ax.add_line(l)
    if 0==np.cos(ang) or 0==np.sin(ang):
        continue
    x0.append(np.cos(ang))
    y0.append(np.sin(ang))
    num.append(0)
    while k<len(x):
        bn = np.sqrt((0.1*i-x[k])**2+(0.1*j-y[k])**2)
        if bn <= 0.1:
            #num[-1][-1]=num[-1][-1]+1
            num[-1]=num[-1]+1
tri = Triangulation(x0, y0)
atri = tri.get_masked_triangles()

#绘图
levels = np.arange(0., 110., 5)
#plt.triplot(tri)
a = sub.tricontourf(tri, num, levels=levels)
fig.colorbar(a, shrink=0.7)

show()