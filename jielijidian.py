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
Dia = data['Dia'].values.tolist()

fig = plt.figure(figsize=(7, 6))
sub = fig.add_subplot(111)

#设置大圆半径R=1.5
#生成投影网外圆
an = np.linspace(0, 2*np.pi, 100)
sub.plot(1.5*np.cos(an), 1.5*np.sin(an))

#生成投影网刻度
s = np.linspace(0,2*np.pi,37)
for ang in s:
    l = Line2D([1.5*np.cos(ang), 1.52*np.cos(ang)], [1.5*np.sin(ang), 1.52*np.sin(ang)])
    sub.add_line(l)
sub.text(-0.35, 1.7, u'节理极点图', fontsize=16)
sub.text(0, 1.55, 'N')
sub.text(1.55,  0, 'E')
sub.text(-1.60, 0, 'W')
sub.text(0, -1.65, 'S')

s = np.linspace(-1.5,1.5,21)
for ang in s:
    l = Line2D([-1.5, 1.5], [ang, ang],color='black')
    sub.add_line(l)
s = np.linspace(-1.5,1.5,21)
for ang in s:
    l = Line2D([ang, ang],[-1.5, 1.5],color='black')
    sub.add_line(l)
sub.add_line(Line2D([-0.05,0.05],[0, 0]))
sub.add_line(Line2D([0, 0],[-0.05,0.05]))

#绘制极点图
def f1(x, y):
    return 1.5*np.sqrt(2)*np.sin(x/180*np.pi/2)*np.sin(y/180*np.pi)
def f2(x, y):
    return 1.5*np.sqrt(2)*np.sin(x/180*np.pi/2)*np.cos(y/180*np.pi)
x = []
y = []
for nmb in range(0, len(Dip)):
    x.append(f1(Dia[nmb], Dip[nmb]))
    y.append(f2(Dia[nmb], Dip[nmb]))
    sub.plot(x[-1],y[-1], 'r.')

show()