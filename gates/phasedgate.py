import numpy as np

class phased_gate:

    def p_gate(qubit_state, angle):
        a = np.exp(complex(0,angle))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output

    def virtual_z_gate(qubit_state):
        a = np.exp(complex(0, np.pi))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output

    def i_gate(qubit_state):
        operator = [[1,0],[0,1]]
        output = np.dot(operator, qubit_state)
        return output

    def s_gate(qubit_state):
        a = np.exp(complex(0, np.pi/2))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output
    
    def t_gate(qubit_state):
        a = np.exp(complex(0, np.pi/4))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output

    def s_dagger_gate(qubit_state):
        a = np.exp(complex(0, -np.pi/2))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output

    def t_dagger_gate(qubit_state):
        a = np.exp(complex(0, -np.pi/4))
        operator = [[1,0],[0,a]]
        output = np.dot(operator, qubit_state)
        return output  