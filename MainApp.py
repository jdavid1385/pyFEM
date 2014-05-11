# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/poissonbreaker/Escritorio/FEM/UI/MainApp4.1.ui'
#
# Created: Mon Jun 27 17:58:25 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from VisualizationEngine import MplWidget 
from sympy import *

class Ui_MainWindow(object):
    p_x = 0
    q_x = 0
    f_x = 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 604)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Visuallization = QtGui.QWidget()
        self.Visuallization.setObjectName("Visuallization")
        self.Visuallization
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Visuallization)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = MplWidget(self.Visuallization)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3.addWidget(self.widget_2)
        self.tabWidget.addTab(self.Visuallization, "")
        self.Configuration = QtGui.QWidget()
        self.Configuration.setObjectName("Configuration")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Configuration)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtGui.QSplitter(self.Configuration)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_fx = QtGui.QLabel(self.widget)
        self.label_fx.setObjectName("label_fx")
        self.horizontalLayout_2.addWidget(self.label_fx)
        self.f_x_viz = QtGui.QLineEdit(self.widget)
        self.f_x_viz.setObjectName("f_x_viz")
        self.horizontalLayout_2.addWidget(self.f_x_viz)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_px = QtGui.QLabel(self.widget)
        self.label_px.setObjectName("label_px")
        self.horizontalLayout.addWidget(self.label_px)
        self.px_viz = QtGui.QLineEdit(self.widget)
        self.px_viz.setObjectName("px_viz")
        self.horizontalLayout.addWidget(self.px_viz)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_gx = QtGui.QLabel(self.widget)
        self.label_gx.setObjectName("label_gx")
        self.horizontalLayout_3.addWidget(self.label_gx)
        self.gx_viz = QtGui.QLineEdit(self.widget)
        self.gx_viz.setObjectName("gx_viz")
        self.horizontalLayout_3.addWidget(self.gx_viz)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.solve = QtGui.QPushButton(self.widget)
        self.solve.setObjectName("solve")
        self.verticalLayout_4.addWidget(self.solve)
        self.verticalLayout_5.addWidget(self.splitter)
        self.tabWidget.addTab(self.Configuration, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.MSE = QtGui.QLineEdit(self.centralwidget)
        self.MSE.setObjectName("MSE")
        self.verticalLayout_2.addWidget(self.MSE)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionX = QtGui.QAction(MainWindow)
        self.actionX.setCheckable(True)
        self.actionX.setObjectName("actionX")
        self.actionGetr = QtGui.QAction(MainWindow)
        self.actionGetr.setObjectName("actionGetr")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        #QtCore.QObject.connect(self.solve, QtCore.SIGNAL("clicked()"), self.Solve)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Solve(self):
        self.p_x = sympify(self.px_viz.text())
        self.q_x = sympify(self.gx_viz.text())
        self.f_x = sympify(self.f_x_viz.text())
        params = {'p_x': self.p_x, 'q_x': self.q_x, 'f_x':self.f_x} 
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visuallization), QtGui.QApplication.translate("MainWindow", "Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fx.setText(QtGui.QApplication.translate("MainWindow", "f(x)=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_px.setText(QtGui.QApplication.translate("MainWindow", "p(x)=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_gx.setText(QtGui.QApplication.translate("MainWindow", "g(x)=", None, QtGui.QApplication.UnicodeUTF8))
        self.solve.setText(QtGui.QApplication.translate("MainWindow", "Solve", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configuration), QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "MSE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionX.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGetr.setText(QtGui.QApplication.translate("MainWindow", "Getr", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




