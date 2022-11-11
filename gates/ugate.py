import numpy as np

class u_gate:

    def u_gate(qubit_state, t, p, l):
        a = np.cos(t/2)
        b = -np.exp(complex(0,l))*np.sin(t/2)
        c = np.exp(complex(0,p))*np.sin(t/2)
        d = np.exp(complex(0,p+l))*np.cos(t/2)
        operator = [[a,b],[c,d]]
        output = np.dot(operator, qubit_state)
        return output