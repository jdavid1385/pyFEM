'''
Created on 27/06/2011

@author: poissonbreaker
'''
from sympy import Symbol

x = Symbol('x')
class ShapeFunctionsSpace():

    #     Here is created a dictionary which holds the different shape functions in order to call them by name  
    #     Each functional receives as parameter the interval over which the element is placed along the grid. 
    
    def __init__(self):
        self.Shape_Functions = {'v_(j,j)': self.v_j_left, 'v_(j-1,j)': self.v_j_right, 'v_(j-1/2,j)': self.v_j_middle}
        self.SF_names = self.Shape_Functions.keys()
    
    def v_j_left(self,K_j):
        h_j = K_j[2] - K_j[0]
        v_j = 1 + 3*(x - K_j[2])/h_j+2*((x - K_j[2])/h_j)**2   
        return v_j
    
    def v_j_right(self,K_j):
        h_j = K_j[2] - K_j[0]
        v_j =1 - 3*(x - K_j[0])/h_j+2*((x - K_j[0])/h_j)**2
        return v_j
    
    def v_j_middle(self,K_j):
        h_j = K_j[2] - K_j[0]
        v_j = 1 - 4*((x - K_j[1])/h_j)**2
        return v_j
    
    def getSF_Names(self):
        return self.SF_names
    
    def getFunctional(self,String):
        return self.Shape_Functions[String]
    