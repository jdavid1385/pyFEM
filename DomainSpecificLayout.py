# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/poissonbreaker/Escritorio/FEM/UI/MainApp4.3.ui'
#
# Created: Sun Jul  3 13:48:13 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sympy import sympify
from sympy.simplify import nsimplify
from sympy import lambdify
from sympy import Symbol
from FEM_Engine import Engine as FEM_Eng

class Layout(QtGui.QWidget):
    progress = 0
    parent = None
    engine = []
    p_x = 0
    q_x = 0
    f_x = 0
    a = 0; b = 0
    Nelems = 0
    Boundary = [0, 0]
    currtab = 2
    #input_px = None
    #input_qx = None
    #input_fx = None
    #input_valX0 = None
    #input_valXN = None
    Wizard = None 
#    viz_FE_Sol = None
    
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        self.engine = FEM_Eng()
        
    def Change_Tab(self):
        
        if (self.currtab <= 0) :
            self.parent.Wizard.setCurrentIndex(2)
            self.currtab = 2
            if self.progress > 90 :
                self.parent.Progress_conf.setProperty("value", 100)
        else:          
            self.currtab -= 1
            if self.progress < 90 :
                self.progress = self.progress + 33  
                self.parent.Progress_conf.setProperty("value", self.progress)
            if self.progress > 90 :
                self.parent.Progress_conf.setProperty("value", 100)
            self.parent.Wizard.setCurrentIndex(self.currtab)

                        
    def CleanAll(self):
        self.engine.restart()    
        self.parent.viz_FE_Sol.canvas.restart()  
        self.progress = 0
        self.parent.Progress_conf.setProperty("value", 0)
 
    def setParent(self, parent):   
        self.parent = parent
        self.parent.Wizard.setCurrentIndex(2)
        self.parent.Progress_conf.setProperty("value", 0)
        
    def Solve(self):
        
        self.p_x = sympify(unicode(self.parent.input_px.text()),rational=False)
        self.q_x = sympify(unicode(self.parent.input_qx.text()))
        self.f_x = sympify(unicode(self.parent.input_fx.text()))
        
        leftbound = self.parent.input_valX0.text()
        self.Boundary[0] = leftbound.toFloat()[0] 
        
        rightbound = self.parent.input_valXN.text()
        self.Boundary[1]=rightbound.toFloat()[0]
        
        self.a = self.parent.input_Domain_L.text().toFloat()[0]
        self.b = self.parent.input_Domain_R.text().toFloat()[0]
        self.Nelems = self.parent.NofElems_viz.text().toFloat()[0]
        
        params = {'p_x': self.p_x, 'q_x': self.q_x, 
                  'f_x':self.f_x, 'a': self.a, 'b': self.b,
                  'Nelems': self.Nelems, 'Boundary':self.Boundary}
     
        self.engine.RetrieveParams(**params)
        self.engine.Solve()
        [U, MSE] = self.engine.retrieve_Solution()
        Grid = self.engine.retrieve_Grid()
        self.parent.viz_FE_Sol.canvas.set_FEM_Viz(Grid, U)
        
        t= Symbol('t')
        Exact_sol = sympify(unicode(self.parent.viz_MSE.text()),rational=False) #compile(str(self.parent.viz_MSE.text()),'Exact_sol.py','eval')
    
        #Exact_sol_lambda = lambdify(Exact_sol, [t])#[]
        Exact_u = []
        itr = 0
        for x in Grid: 
            Exact_u.insert(itr,Exact_sol.subs({t:x}))
            itr +=1
        itr = 0    
        for x in Grid:
            MSE += (Exact_u[itr] - U[itr])**2
            itr+=1
        
        MSE = MSE/len(Grid)
        MSE = MSE.evalf()
        self.parent.viz_MSE.setText(str(MSE))                  
        #self.EvaluatedFormula.setText(str(a))
        
