import numpy as np

class HadamardGate:

    def h_gate(qubit_state):
        k = 1/(2**0.5)
        h_operator = [[k,k],[k,-k]]
        output = np.dot(h_operator, qubit_state)
        return output