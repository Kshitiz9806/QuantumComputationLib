import numpy as np

class sycamoreGate:

    def sycamore_gate(qubit_state):
        a = np.exp(complex(0,-np.pi/6))
        sycamore_operator = [[1,0,0,0],[0,0,complex(0,-1),0],[0,complex(0,-1),0,0],[0,0,0,a]]
        output = np.dot(sycamore_operator, qubit_state)
        return output