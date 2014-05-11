from numpy import *
from scipy import linalg
from scipy import integrate as integral
from scipy import sparse
from sympy import *
import matplotlib.pyplot as plt

x = Symbol('x')
                      
    #    The stiffness Matrix on the interval.    
    #                    
    #               x_j       _           _
    #                /       | v'_(j-1,j)  |  _                                _  
    #         s      |       |             | |                                  |
    #        Aj   =  |  p(x) | v'_(j-1/2,j)| | v'_(j-1/2,j) v'_(j-1,j) v'_(j,j) | dx +
    #                /       |             | |_                                _| 
    #             x_(j-1)    |_ v'_(j,j)  _|
    #
    #              x_j       _          _
    #               /       | v_(j-1,j)  |  _                             _  
    #               |       |            | |                               |
    #               |  q(x) | v_(j-1/2,j)| | v_(j-1/2,j) v_(j-1,j) v_(j,j) | dx +
    #               /       |            | |_                             _| 
    #            x_(j-1)    |_ v_(j,j)  _|
    #
    #   The stiffness matrix is stored in COO format (help matrix_COO), based on
    #   coordinates and values, is compact and is suitable for the final assemly
    #   since is possible to summ up repeated values  of  coordinates  as needed
    #   for the values of the Matrix on th right nodes of each preceding element
    #   and the  next leftmost node (i.e element meet at those points as defined
    #   on the functionals  x_(j-1) =< x =< x_j  &&  x_j =< x =< x_j+1) )
    #                                       ^        ^
    #                                       |        |
    #                                        --------
    #    Finite Element for a 1 dimensional ODE with polimorphic use of shape functions

class Finite_Element():
    
    def __init__(self,**SegmentProps):

        # Interval of the actual element (K)
        self.interval = SegmentProps['Interval']
        
        #Shape Functions and their derivatives ()
        self.left_SF   = 0;  self.dleft_SF   = 0
        self.right_SF  = 0;  self.dright_SF  = 0
        self.middle_SF = 0;  self.dmiddle_SF = 0       

        #q(x) and p(x)
        self.p_x = 0
        self.q_x = 0
        self.f_x = 0

        # Stiffness Matrix data
        self.Aj = {'data':0,'rows':0, 'cols':0}
        self.Aj['data'] = zeros((1,9))
        self.Aj['rows'] = SegmentProps['k']*array([2,2,2],dtype=float32) + array([0,1,2],dtype=float32)
        self.Aj['cols'] = SegmentProps['k']*array([2,2,2],dtype=float32) + array([0,1,2],dtype=float32)
 
        # Nodal Forces Vector data
        self.Fj = {'data':0,'rows':0, 'cols':0}
        self.Fj['data'] = zeros((1,3))
        self.Fj['rows'] = SegmentProps['k']*array([2,2,2],dtype=float32) + array([0,1,2],dtype=float32)
        self.Fj['cols'] = [0]        
        #Local symbolic Stiffness Matrix and Nodal Forces Vector
        self.Stiff_loc_Sym = 0
        self.Forces_loc_Sym = 0

    def Functional(self,func):
        def ActualSF(*args):
            print 'The ', func.__name__, 'shape function has been called'
            Piecewise_Polinomial = func(*args)
            if(func.__name__== 'v_j_left'):
                self.left_SF = Piecewise_Polinomial
                self.dleft_SF = Piecewise_Polinomial.diff(x)
            elif(func.__name__== 'v_j_right'):
                self.right_SF = Piecewise_Polinomial
                self.dright_SF = Piecewise_Polinomial.diff(x)
            elif(func.__name__== 'v_j_middle'):
                self.middle_SF = Piecewise_Polinomial
                self.dmiddle_SF = Piecewise_Polinomial.diff(x)               
        return ActualSF
    
    def SetParams(self,**params):
            self.p_x = params['p_x']
            self.q_x = params['q_x']
            self.f_x = params['f_x']
                    
    def create_stiff_local_Sym(self):
        self.StiffLocal_deriv   =  self.p_x*Matrix([[self.dright_SF], [self.dmiddle_SF], [self.dleft_SF]])*Matrix([[self.dright_SF, self.dmiddle_SF, self.dleft_SF]])   
        self.StiffLocal_noderiv =  self.q_x*Matrix([[self.right_SF], [self.middle_SF], [self.left_SF]])*Matrix([[self.right_SF, self.middle_SF, self.left_SF]])
        self.Stiff_loc_Sym = self.StiffLocal_deriv + self.StiffLocal_noderiv

    def create_nodal_forces_local_Sym(self):
        self.Forces_loc_Sym = self.f_x*Matrix([[self.right_SF], [self.middle_SF], [self.left_SF]])
        
    def solve_stiff_local(self):
        j = 0
        for eq in self.Stiff_loc_Sym:
            self.Aj['data'][j]=integral.quad(lambdify(x,eq),self.interval[0],self.interval[2])
            self.Aj['data'][j]=self.Aj['data'][j][0]
            j = j+1
    def solve_forces_local(self):
        j = 0
        for eq in self.Forces_loc_Sym:
            self.Fj['data'][j]=integral.quad(lambdify(x,eq),self.interval[0],self.interval[2])
            self.Fj['data'][j]=self.Fj['data'][j][0]
            j = j+1
            