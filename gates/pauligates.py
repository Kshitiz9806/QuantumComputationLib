import numpy as np

class PauliGates:

    def pauli_x_gate(qubit_state):
        pauli_x_operator = [[0,1],[1,0]]
        output = np.dot(pauli_x_operator, qubit_state)
        return output

    def pauli_y_gate(qubit_state):
        pauli_y_operator = [[0,complex(0,-1*1)],[complex(0,1),0]]
        output = np.dot(pauli_y_operator, qubit_state)
        return output

    def pauli_z_gate(qubit_state):
        pauli_z_operator = [[1,0],[0,-1]]
        output = np.dot(pauli_z_operator, qubit_state)
        return output