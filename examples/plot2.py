from math import sin, pi

from numpy import array
from jsplot import plot, show

def get_data1():
    x1 = 0
    x2 = 3*pi
    d = []
    for i in range(101):
        x = x1 + i * (x2 - x1) / 100.
        d.append([x, sin(x * sin(x))])
    return d

def get_data2():
    x1 = 0
    x2 = 3*pi
    d = []
    for i in range(101):
        x = x1 + i * (x2 - x1) / 100.
        d.append([x, sin(x)])
    return d

d = array(get_data1())
x = d[:, 0]
y = d[:, 1]
plot(x, y, label="sin(x*sin(x))")
d = array(get_data2())
x = d[:, 0]
y = d[:, 1]
plot(x, y, label="sin(x)")
show()
