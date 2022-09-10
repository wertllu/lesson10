# # from db.dbConnection import dbConnection
# from less1 import printHelloWord
# import db

# db.dbConnection.dbConnection()

from math import sin
import matplotlib.pyplot as plt

from cProfile import label
from matplotlib.pyplot import plot, xlabel, ylabel, title, legend, show
from numpy import linspace

from myChartLib import myChart

x = linspace(0, 2, 100)

plot (x,myChart(x),label='linear')

# plot (x,x,label='linear')
# plot (x,x**2,label='quadratic')
# plot (x,x**3,label='cubic')
xlabel ('x label')
ylabel ('y label')
title ('Simple Plot')
legend ('Simple Plot')
show()