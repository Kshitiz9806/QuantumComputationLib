import numpy as np

class phased_gate:

    def p_gate(qubit_state, angle):
        a = np.exp(complex(0,angle))
        p_operator = [[1,0],[0,a]]
        output = np.dot(p_operator, qubit_state)
        return output

    def virtual_z_gate(qubit_state):
        a = np.exp(complex(0, np.pi))
        virtual_z_operator = [[1,0],[0,a]]
        output = np.dot(virtual_z_operator, qubit_state)
        return output

    def i_gate(qubit_state):
        i_operator = [[1,0],[0,1]]
        output = np.dot(i_operator, qubit_state)
        return output

    def s_gate(qubit_state):
        a = np.exp(complex(0, np.pi/2))
        s_operator = [[1,0],[0,a]]
        output = np.dot(s_operator, qubit_state)
        return output
    
    def t_gate(qubit_state):
        a = np.exp(complex(0, np.pi/4))
        t_operator = [[1,0],[0,a]]
        output = np.dot(t_operator, qubit_state)
        return output

    def s_dagger_gate(qubit_state):
        a = np.exp(complex(0, -np.pi/2))
        s_dagger_operator = [[1,0],[0,a]]
        output = np.dot(s_dagger_operator, qubit_state)
        return output

    def t_dagger_gate(qubit_state):
        a = np.exp(complex(0, -np.pi/4))
        t_dagger_operator = [[1,0],[0,a]]
        output = np.dot(t_dagger_operator, qubit_state)
        return output  