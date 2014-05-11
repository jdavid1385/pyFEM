'''
Created on 27/06/2011

@author: poissonbreaker
'''
from numpy import *
from scipy import linalg
from scipy import sparse

    #  This Class should be initialized with the whole FE space 
class FEMatrix_Assembler():

    #  Final Stiffness Matrix and Force Vector   
    A = []
    F = []
    
    #  Matrix Data
    data_A = []
    rows_A = []
    cols_A = []
    
    data_F = []
    rows_F = []
    cols_F = []    
    
    def Assemble(self, FE):

    #  Assembling the final A matrix
    
        for Element in FE:
            for i in Element.Aj['data']:
                self.data_A.append(i)
            for i in Element.Aj['rows']:
                for j in Element.Aj['cols']:
                    self.rows_A.append(i)
                    self.cols_A.append(j)
        
    #  Retrieve a linked list version of the matrix for a fast modification
    #  of the terms at the moment of applying boundary conditions.
        self.A = sparse.coo_matrix((self.data_A,(self.rows_A,self.cols_A)), dtype=float32).tolil()
        
    #  Assembling the final F vector
        
        for Element in FE:
            for i in Element.Fj['data']:
                self.data_F.append(i)
            for i in Element.Fj['rows']:
                for j in Element.Fj['cols']:
                    self.rows_F.append(i)
                    self.cols_F.append(j)
        
    #  Retrieve a linked list version of the matrix for a fast modification
    #  of the terms at the moment of applying boundary conditions.            
        self.F = sparse.coo_matrix((self.data_F,(self.rows_F,self.cols_F)),dtype=float32).tolil()
    
    def restart(self):
        self.A = []
        self.F = []
        #  Matrix Data
        self.data_A = []
        self.rows_A = []
        self.cols_A = []
           
        self.data_F = []
        self.rows_F = []
        self.cols_F = []    
    
           
    def retrieve_System(self):
        return [self.A, self.F]    
        