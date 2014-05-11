'''
Created on 27/06/2011

@author: poissonbreaker
'''
from numpy import *
from scipy import linalg
from scipy import sparse

    #   Class for creating a 1-D Mesh.
class Mesh():

#Initialization of the sub-space (Grid) for which we are looking for an 
#approximate solution to the 1-D n-order ordinary differencial equation.
#The parameter  k  in  the inicialization is the number of element, the
#currently the elements are numbered as follows:
#
#                           For N elements 
#         a                                                    b 
#         |--------|--------|--------|----------------|--------|
#         x0    x1-1/2      x1     x2-1/2 ........ xN-1/2      xN
#         
#       there exist 2N+1 nodes along the grid. X0 and XN correspond
#       to the values at boundaries  (i.e [a,b], X0 = a, XN = b)
#       the iterator over the interval is used as a help function
#       to generate the elements over the interval each 2 nodes. 
 
    def __init__(self,**params):
        self.Nnodes = 2*params['Nelems']+1
        self.grid = linspace(params['a'], params['b'], self.Nnodes, endpoint=True, retstep=False)
        self.iterator = arange(0,size(self.grid)-1,2)
    def get_Mesh(self):
        return  (self.grid,self.iterator)
