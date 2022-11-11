import numpy as np

class measure:

    def measure_x(qubit_state):
        operator = [[1,0],[0,0]]
        output = np.dot(operator, qubit_state)
        return output

    def measure_y(qubit_state):
        operator = [[0,0],[0,1]]
        output = np.dot(operator, qubit_state)
        return output
