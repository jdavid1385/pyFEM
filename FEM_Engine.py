'''
Created on 27/06/2011

@author: poissonbreaker
'''
from Model.Solver import FE_Solver
from Model.Builder import FESpace_Builder
from Model.Assembler import FEMatrix_Assembler
from Model.Boundary_Conditions import BC_Dirichlet_Handler

        #                                     ToolChain
        #     ____________________________________________________________________________
        #    |   _________          ___________         ____________           ________   |
        #    |  |         |  FE[]  |           | [A,F] |            | [A*,F*] |        |  |
        #    |  | Builder |------->| Assembler |------>| BC_Handler |-------->| Solver |  |
        #    |  |_________|        |___________|       |____________|         |________|  | 
        #    |_______^_____________________________________________________________|______|
        #            |                           ENGINE                            |  
        #            |Parameters                                                   | [u,MSE]
        #            |                                                             |
        #     _______|_______                   _________                   _______v________
        #    |               |                 /         \                 |                |                                         
        #    | Configuration |================||   APP   ||================|  Visualization | 
        #    |_______________|                 \_________/                 |________________|
        #                                                                          |
        #                                                                          | [x,u]
        #                                                                   _______v________
        #                                                                  |                |
        #                                                                  |  Visualization |
        #                                                                  |     Engine     |
        #                                                                  |________________|

        
class Engine():
    
    params = {'p_x':0,'q_x':0,'f_x':0,'a':0,'b':0, 'Nelems':0, 'Boundary':0}
    FE = []
    A = [];  A_bc = []
    F = [];  F_bc = []
    u = [];  MSE = 0
    
    FE_Builder = None
    FE_Assembler = None
    FE_BC_Handler = None
    FE_Solver = None
    
    def __init__(self):
        self.FE_Builder = FESpace_Builder()
        self.FE_Assembler = FEMatrix_Assembler()
        self.FE_BC_Dirichlet_Handler = BC_Dirichlet_Handler()
        self.FE_Solver = FE_Solver()
        
    def RetrieveParams(self,**AppParams):
        self.params['p_x']    = AppParams['p_x'] 
        self.params['q_x']    = AppParams['q_x']
        self.params['f_x']    = AppParams['f_x']
        self.params['a']      = AppParams['a']
        self.params['b']      = AppParams['b']
        self.params['Nelems'] = AppParams['Nelems']
        self.params['Boundary']= AppParams['Boundary']
        
    def Solve(self):
                
        #________________________________________________
        # Building the FE space with the given parameters
        self.FE_Builder.SetParams(**self.params)
        self.FE_Builder.BuildSpace()
        # Retrieve the Finite Element Space
        self.FE = self.FE_Builder.retrieve_FESpace()
        #________________________________________________
        #                      |
        #                      |  FE[]
        #______________________V_________________________        
        #  Assembling the Global Stiffness Matrix and F  |
        #________________________________________________|
        self.FE_Assembler.Assemble(self.FE) 
        # Retrieve A and F. The retrieved system is in general Singular
        [self.A, self.F] = self.FE_Assembler.retrieve_System()
        #________________________________________________
        #                      |
        #                      |  [A,F]
        #______________________V_________________________        
        #     Applying Dirichlet Boundary Conditions     |
        #________________________________________________|
        self.FE_BC_Dirichlet_Handler.ApplyBoundaryConditions(self.A, self.F, self.params['Boundary'])

        # Retrieve the modified system 
        [self.A_bc, self.F_bc] = self.FE = self.FE_BC_Dirichlet_Handler.retrieve_System()
        #________________________________________________
        #                      |
        #                      |  [A*,F*]
        #______________________V_________________________        
        # Finally the system of equations is solved for  |
        #____by the solver given on it parameters _______|
        self.FE_Solver.solve(self.A_bc,self.F_bc,'cg')

        # Finally retrieve the solution for the given system
        [self.u, self.MSE] = self.FE_Solver.retrieve_U()
        #________________________________________________
        #                   |
        #                   V
        
    def retrieve_Solution(self):
        return [self.u, self.MSE]
    
    def restart(self):
        self.FE_Assembler.restart()
        self.FE_Builder.restart()
        
    def retrieve_Grid(self):
        return self.FE_Builder.retrieve_Grid()
    