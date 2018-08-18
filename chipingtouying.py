# !/usr/bin/env python
# -*- coding=UTF-8 -*-
# this is a shell bond.s

from pylab import *
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Arrow
import matplotlib
import numpy as np

fig = plt.figure(figsize=(4, 4))
#数据
input1 = "180"
input2 = "70"
input3 = "115"
input4 = "45"
input5 = "245"
input6 = "45"

an = np.linspace(0, 2 * np.pi, 100)
plot(np.cos(an), np.sin(an))

#投影刻度
s = np.linspace(0, 2 * np.pi, 37)
sub = fig.add_subplot(111)
for ang in s:
    l = Line2D([np.cos(ang), 1.02 * np.cos(ang)], [np.sin(ang), 1.02 * np.sin(ang)])
    sub.add_line(l)

plt.text(0, 1.05, 'N')
plt.text(1.05,  0, 'E')
plt.text(-1.15, 0, 'W')
plt.text(0, -1.1, 'S')

# 生成结构面圆弧J1
qinxiang1 = float(input3) / 180 * np.pi
qinjiao1 = float(input4) / 180 * np.pi
t1 = -qinjiao1 / np.pi * 180 - qinxiang1 / np.pi * 180
t2 = 2 * (90 - qinxiang1 / np.pi * 180) - t1

banjing = 1 / np.cos(qinjiao1)
yuanxin = [np.tan(qinjiao1) * np.sin(qinxiang1), np.tan(qinjiao1) * np.cos(qinxiang1)]
circle = Arc(yuanxin, 2 * banjing, 2 * banjing, color='purple', fill=False, theta1=t2, theta2=t1)
sub.add_patch(circle)

t3 = np.tan(qinjiao1) * np.sin(qinxiang1) - np.cos(np.pi / 2 - qinxiang1) / np.cos(qinjiao1)
t4 = np.tan(qinjiao1) * np.cos(qinxiang1) - np.sin(np.pi / 2 - qinxiang1) / np.cos(qinjiao1)
sub.arrow(t3, t4, 0 - t3, 0 - t4, length_includes_head=True, color='purple')

sub.annotate('J1', xy=(t3, t4), xytext=(t3 - 0.2, t4), arrowprops=dict(facecolor='black', arrowstyle="->"))

#生成结构面圆弧J2
qinxiang2 = float(input5)/180*np.pi
qinjiao2 = float(input6)/180*np.pi
t1 = -qinjiao2/np.pi*180-qinxiang2/np.pi*180
t2 = 2*(90-qinxiang2/np.pi*180)-t1

banjing = 1/np.cos(qinjiao2)
yuanxin = [np.tan(qinjiao2)*np.sin(qinxiang2), np.tan(qinjiao2)*np.cos(qinxiang2)]
circle = Arc(yuanxin, 2*banjing, 2*banjing, color='purple', fill=False, theta1=t2, theta2=t1)
sub.add_patch(circle)

t3=np.tan(qinjiao2)*np.sin(qinxiang2)-np.cos(np.pi/2-qinxiang2)/np.cos(qinjiao2)
t4=np.tan(qinjiao2)*np.cos(qinxiang2)-np.sin(np.pi/2-qinxiang2)/np.cos(qinjiao2)
sub.arrow(t3, t4, 0-t3, 0-t4, length_includes_head=True, color='purple')

sub.annotate('J2', xy=(t3, t4), xytext=(t3+0.2, t4), arrowprops=dict(facecolor='black', arrowstyle="->"))

# 生成坡面圆弧
qinxiang3 = float(input1) / 180 * np.pi
qinjiao3 = float(input2) / 180 * np.pi
t1 = -qinjiao3 / np.pi * 180 - qinxiang3 / np.pi * 180
t2 = 2 * (90 - qinxiang3 / np.pi * 180) - t1

banjing = 1 / np.cos(qinjiao3)
yuanxin = [np.tan(qinjiao3) * np.sin(qinxiang3), np.tan(qinjiao3) * np.cos(qinxiang3)]
circle = Arc(yuanxin, 2 * banjing, 2 * banjing, color='red', fill=False, theta1=t2, theta2=t1)
sub.add_patch(circle)

t3 = np.tan(qinjiao3) * np.sin(qinxiang3) - np.cos(np.pi / 2 - qinxiang3) / np.cos(qinjiao3)
t4 = np.tan(qinjiao3) * np.cos(qinxiang3) - np.sin(np.pi / 2 - qinxiang3) / np.cos(qinjiao3)
sub.arrow(t3, t4, 0 - t3, 0 - t4, length_includes_head=True, color='red')

sub.annotate('Slope', xy=(t3, t4), xytext=(t3 + 0.2, t4),
                          arrowprops=dict(facecolor='black', arrowstyle="->"))

#生成结构面交割线投影
x1=np.tan(qinjiao1)*np.sin(qinxiang1)
y1=np.tan(qinjiao1)*np.cos(qinxiang1)
x2=np.tan(qinjiao2)*np.sin(qinxiang2)
y2=np.tan(qinjiao2)*np.cos(qinxiang2)
#plt.axes().arrow(x1,y1,0-x1,0-y1,length_includes_head=True)
#plt.axes().arrow(x2,y2,0-x2,0-y2,length_includes_head=True)
r1=1/np.cos(qinjiao1)
r2=1/np.cos(qinjiao2)
#print(r1)
#print(r2)
d=np.sqrt((x1-x2)**2+(y1-y2)**2)
#print(d)
x = (r1**2-r2**2+d**2)/(2*d)
#print(x)
a = np.arctan((y1-y2)/(x1-x2))
b = a+np.pi/2
if x1 >= x2:
    if (x1-(x*np.cos(a)))>=x2 and (x1-(x*np.cos(a)))<=x1:
        x0 = x1-(x*np.cos(a))
        y0 = y1-(x*np.sin(a))
    else:
        x0 = x1+(x*np.cos(a))
        y0 = y1+(x*np.sin(a))
else:
    if (x1-(x*np.cos(a)))>=x1 and (x1-(x*np.cos(a)))<=x2:
        x0 = x1-(x*np.cos(a))
        y0 = y1-(x*np.sin(a))
    else:
        x0 = x1+(x*np.cos(a))
        y0 = y1+(x*np.sin(a))
#plt.axes().arrow(x0,y0,0-x0,0-y0,length_includes_head=True)
h=np.sqrt(r1**2.0-x**2)
t3=x0+(h*np.cos(b))
t4=y0+(h*np.sin(b))
if np.sqrt(t3**2+t4**2)>1:
    t3 = x0-(h*np.cos(b))
    t4 = y0-(h*np.sin(b))
#print('交割线倾向',90-b/np.pi*180)#交割线倾向
#print('交割线倾角',90-2*np.arctan(np.sqrt(t3**2+t4**2))*180/np.pi)#交割线倾角
sub.arrow(t3, t4, 0-t3, 0-t4, length_includes_head=True, color='green')
# 在屏幕上显示

show()
