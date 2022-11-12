import numpy as np

class cnotGate:

    def cnot_gate(qubit_state):
        cnot_operator =  [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
        output = np.dot(cnot_operator, qubit_state)
        return output