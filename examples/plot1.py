from math import sin, pi

from numpy import array
from pylab import plot, savefig

def get_data():
    x1 = 0
    x2 = 3*pi
    d = []
    for i in range(101):
        x = x1 + i * (x2 - x1) / 100.
        d.append([x, sin(x * sin(x))])
    return d

d = array(get_data())
x = d[:, 0]
y = d[:, 1]
plot(x, y, label="data1")
savefig("a.png")
