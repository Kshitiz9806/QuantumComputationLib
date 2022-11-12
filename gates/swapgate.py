import numpy as np

class swapGate:

    def swap_gate(qubit_state):
        swap_operator = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
        output = np.dot(swap_operator, qubit_state)
        return output

    def sqrt_swap_gate(qubit_state):
        sqrt_swap_operator = [[1,0,0,0],[0,complex(0.5,0.5),complex(0.5,-0.5),0],[0,complex(0.5,-0.5),complex(0.5,0.5),0],[0,0,0,1]]
        output = np.dot(sqrt_swap_operator, qubit_state)
        return output

    def sqrt_i_swap_gate(qubit_state):
        a = 1/np.sqrt(2)
        sqrt_i_swap_operator = [[1,0,0,0],[0,a,complex(0,a),0],[0,complex(0,a),a,0],[0,0,0,1]]
        output = np.dot(sqrt_i_swap_operator, qubit_state)
        return output