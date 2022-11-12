import numpy as np

class czGate:

    def cz_gate(qubit_state):
        cz_operator = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]]
        output = np.dot(cz_operator, qubit_state)
        return output