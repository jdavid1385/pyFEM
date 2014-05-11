# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/poissonbreaker/Escritorio/FEM/UI/FormulaParser.ui'
#
# Created: Sat May 28 20:30:11 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from VisualizationEngine import FE_Viz
from sympy import *

class Formula_Input_Form(QtGui.QDialog):
    f_x = 0
    p_x = 0
    q_x = 0
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(384, 204)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtGui.QLineEdit(Frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.EvaluatedFormula = QtGui.QLineEdit(Frame)
        self.EvaluatedFormula.setObjectName("EvaluatedFormula")
        self.gridLayout.addWidget(self.EvaluatedFormula, 2, 0, 1, 1)
        self.Parse_formulas = QtGui.QPushButton(Frame)
        self.Parse_formulas.setObjectName("Parse_formulas")
        self.gridLayout.addWidget(self.Parse_formulas, 3, 0, 1, 1)
        self.mpl = FE_Viz(Frame)
        self.mpl.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mpl.setObjectName("mpl")
        self.gridLayout.addWidget(self.mpl, 0, 0, 1, 1)
        self.actionParse = QtGui.QAction(Frame)
        self.actionParse.setCheckable(True)
        self.actionParse.setObjectName("actionParse")
        
        self.retranslateUi(Frame)
        QtCore.QObject.connect(self.Parse_formulas, QtCore.SIGNAL("clicked()"), self.ParseFormula)
        #QtCore.QMetaObject.connectSlotsByName(self)

    def ParseFormula(self):
        #formula = compile(str(self.lineEdit.text()),'formula.py','eval')
        self.lineEdit.setValidator(QtGui.QDoubleValidator(-999.0, 999.0, 2, self.EvaluatedFormula))
        y = QtCore.QString()
        
        #print self.EvaluatedFormula.validator()
        import PyQt4
        
        try:
            y = self.lineEdit.text()
        except ValueError:
            pass
        QtGui.QMessageBox.warning(self,"Error de entrada", y,"Valor no numérico")
        y = y.toFloat()[0]
        
        x = 5.2
        z = x+y
        #formula = compile(str(self.lineEdit.text()),'formula.py','eval')    
        # a = eval(formula)
        #self.EvaluatedFormula.setText(str(a))
        self.EvaluatedFormula.setText(str(z))
        self.mpl.canvas.setEquation()

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.Parse_formulas.setText(QtGui.QApplication.translate("Frame", "Parse Formula", None, QtGui.QApplication.UnicodeUTF8))
        self.actionParse.setText(QtGui.QApplication.translate("Frame", "Parse", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Formula_Input_Form()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())


