'''
Created on 27/06/2011

@author: poissonbreaker
'''
from numpy import *
from scipy.sparse import linalg
from sympy import *

class FE_Solver():
    
    u = []
    MSE = 0
    
    def __init__(self):
        pass
    
    def solve(self, A, F,Solver):
        # "spsolve" for internal solver
        # "cg" for conjugate gradient
        A = A.tocsc()
        #F = F.toarray()
        if (Solver == "spsolve"):
            self.u = linalg.spsolve(A.astype(float32),F.astype(float32))
        if (Solver == "cg"):    
            self.u = linalg.cg(A.toarray(),F.toarray())[0]
        
    def retrieve_U(self):
        return [self.u, self.MSE]
    