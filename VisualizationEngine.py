import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget


# Matplotlib Figure object
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)

    def setEquation(self):
        self.fig.subplots_adjust(top=0.85)
#        self.ax.text(3, 8, 'boxed italics text in data coords', style='italic',
#        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
        self.ax.text(-0.8, 1.6, r'$\minus{\frac{d}{dx} \left[p(x)\frac{du}{dx}\right]} + q(x)u = f(x)$', fontsize=40)
#        self.ax.text(3, 2, unicode('unicode: Institut f\374r Festk\366rperphysik', 'latin-1'))
#        self.ax.text(0.95, 0.01, 'colored text in axes coords',
#        verticalalignment='bottom', horizontalalignment='right',
#        transform=self.ax.transAxes,
#        color='green', fontsize=15)
#        self.ax.plot([2], [1], 'o')
#        self.ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
#        arrowprops=dict(facecolor='black', shrink=0.05))
        self.ax.axis([0,10,0,5])
        self.ax.set_axis_off()
        self.draw()

    def set_FEM_Viz(self, Grid, u):
        self.ax.plot(Grid,u,'*')
        self.ax.xaxis.set_label_text('$x_j$')
        self.ax.yaxis.set_label_text('$u(x)$')
        #self.ax.x_label('$x_j$')
        #self.ax.title('FE solution for $u(x)$')
        self.ax.grid()
        self.draw()
        
    def restart(self):
        print "I have been called and I clean everything :)"
        self.ax.clear()
        self.ax.plot([0], [0], 'o')
        self.draw()
        
class FE_Viz(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
    

class Eq_Viz(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
        self.canvas.setEquation()

class MplWidget(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.mpl_toolbar = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.mpl_toolbar)
        self.setLayout(self.vbl)
    def addPlot(self,plot):
        x,y = plot.getArrays()
        self.canvas.ax.plot(x,y, plot.getStyle(), label=plot.getName(),color=plot.getColor())
    def draw(self):
        self.canvas.draw()
        self.canvas.ax.legend()
    def clearPlots(self):
        self.canvas.draw()