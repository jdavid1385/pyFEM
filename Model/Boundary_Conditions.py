'''
Created on 27/06/2011

@author: poissonbreaker
'''
from numpy import *
from scipy import linalg
from scipy import sparse

            #  The process of application of Boundary conditions is depicted 
            #               ---------------------------------    
            #              |    u[1] = u_0       u[n] = u_n  |
            #               ---------------------------------
            #
            #               A[1][2:n]   = 0          F[1] = a11*u_0
            #               A[n][1:n-1] = 0          F[n] = ann*u_n
            #            _                    _   _  _     _       _  
            #           | a11  0  .......  0   | | u1 |   | a11*u_0 |
            #           | a21 a22 .......  0   | | u2 |   |   f2    |
            #           | a31 a32 .......  0   | | u3 | = |   f3    |
            #           |  0   :   .       :   | |  : |   |   :     |
            #           |  :   :      . a(n-1)n| |  : |   |   :     |
            #           |_ 0   0 .....    ann _| |_un_|   |_ann*u_n_| 
            #           
            #               A[2:n][1]   = 0       F[2:n-1]-u_0*A[2:n][1]
            #               A[1:n-1][n] = 0             -u_n*A[1:n-1][n]
            #            _                 _   _  _     _       _  
            #           | a11  0  ......  0 | | u1 |   | a11*u_0 |
            #           |  0  a22 ......  0 | | u2 |   |   f2    |
            #           |  0  a32 ......  0 | | u3 | = |   f3    |
            #           |  :        .     : | |  : |   |   :     |
            #           |  :           .  0 | |  : |   |   :     |
            #           |_ 0   0  0  0  ann_| |_un_|   |_ann*u_n_|
        
class BC_Dirichlet_Handler():
    A = []
    F = []
    Applied = False

    def __init__(self):
        pass
    
        
    def ApplyBoundaryConditions(self, A, F, Boundary):        

        self.Applied = True
        ncols = A.get_shape()[1]; nrows = A.get_shape()[0]                
        
        A[0,1:ncols] = zeros((1,ncols-1))
        A[nrows-1,0:ncols-1] = zeros((1,ncols-1))        
               
        A11 = A[0,0]
        Ann = A[nrows-1,ncols-1]
    
        F[0,0]       = A11*Boundary[0]
        F[ncols-1,0] = Ann*Boundary[1]
        
        Bound_left  = Boundary[0]*A[0:nrows,0]
        Bound_left[0,0] = 0
        Bound_right = Boundary[1]*A[0:nrows,ncols-1]
        Bound_right[nrows-1,0]=0
        
        F = F.tocsc()
        Bound_left = Bound_left.tocsc()
        Bound_right = Bound_right.tocsc()
        
        F = F-Bound_right-Bound_left
        
        for i in range(1,nrows):
            A[i,0] = 0
        for i in range(1,nrows-1):    
            A[i,ncols-1] = 0
            
        self.A = A
        self.F = F
        
    def retrieve_System(self):
        if (self.Applied):
            return [self.A, self.F]
        else: 
            return -1
     
