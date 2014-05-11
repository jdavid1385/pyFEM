'''
Created on 27/06/2011

@author: poissonbreaker
'''
from numpy import *
from scipy.sparse import linalg
from sympy import *

from Mesh import Mesh
from FiniteElement.FiniteElement import Finite_Element 
from FiniteElement.Shape_Functions import ShapeFunctionsSpace

class FESpace_Builder():

    #    List of finite Elements to create.  
    FE = []
      
    #    p(x), q(x) and f(x) may come from a text input in the user interface 
    #    and it must be sympified.
    x = Symbol('x')
    p_x = 0
    q_x = 0
    f_x = 0
    
    #    Data for building the 1-D Mesh --> a: left_bound, b: right_bound
    Nelems = 3
    a = 1
    b = 5
    Grid = []
    Boundary = [1,3]
    
    
    def __init__(self):
        self.Shape_Funct = ShapeFunctionsSpace()

    def SetParams(self,**params):
        self.p_x = params['p_x']
        self.q_x = params['q_x']
        self.f_x = params['f_x']
        self.a = params['a']
        self.b = params['b']
        self.Nelems = params['Nelems']
            
    def BuildSpace(self):
        #   Generating the Mesh
        Params = {'Nelems': self.Nelems,'a': self.a,'b': self.b}        
        mesh = Mesh(**Params)
        #   Retreiving the mesh ends up with a tuple with the Grid and its iterator
        (self.Grid, Grid_itr) = mesh.get_Mesh()
        print self.Grid
        i = 0
        #   Generate the elements over the Grid
        NodesPerElem = len(self.Shape_Funct.getSF_Names())
        for k in Grid_itr:
            Segment_Props = {'k':i,'Interval':self.Grid[k:k+NodesPerElem]}
            self.FE.insert(i,Finite_Element(**Segment_Props))
            i=i+1

        #   Calculate functionals
        for Element in self.FE:
            for funct in self.Shape_Funct.getSF_Names():
                Element.Functional(self.Shape_Funct.getFunctional(funct))(Element.interval)

        #   For each element assign p(x), q(x) and f(x)
        for Element in self.FE:
            Element.p_x = self.p_x
            Element.q_x = self.q_x
            Element.f_x = self.f_x
    
        #   Creating the local symbolic Matrices and evaluating the numerical integrals over the interval
        for Element in self.FE:
            Element.create_stiff_local_Sym()
            Element.create_nodal_forces_local_Sym()
            Element.solve_stiff_local()
            Element.solve_forces_local()

    def retrieve_FESpace(self):
        return self.FE
    
    def restart(self):
        self.FE = []
    
    def retrieve_Grid(self):
        return self.Grid    