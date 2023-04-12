import gates.cnotgate as cnotGate
import gates.sycamoregate as sycamoreGate
import gates.czgate as czGate
import gates.swapgate as swapGate

class DoubleQubitSystem:

    def __init__(self, q1, q2):
        a = q1.qubit_state[0][0]*q2.qubit_state[0][0]
        b = q1.qubit_state[0][0]*q2.qubit_state[1][0]
        c = q1.qubit_state[1][0]*q2.qubit_state[0][0]
        d = q1.qubit_state[1][0]*q2.qubit_state[1][0]
        self.qubit_state = [[a],[b],[c],[d]]

    def printState(self):
        print("(" + str(self.qubit_state[0][0]) + ")|00} + (" + str(self.qubit_state[1][0]) + ")|01} + (" + str(self.qubit_state[2][0]) + ")|10} + (" + str(self.qubit_state[3][0]) + ")|11}")

    def cnotGate(self):
        self.qubit_state = cnotGate.cnotGate.cnot_gate(self.qubit_state)
    
    def swapGate(self):
        self.qubit_state = swapGate.swapGate.swap_gate(self.qubit_state)
    
    def sqrtSwapGate(self):
        self.qubit_state = swapGate.swapGate.sqrt_swap_gate(self.qubit_state)

    def sqrtISwapGate(self):
        self.qubit_state = swapGate.swapGate.sqrt_i_swap_gate(self.qubit_state)

    def sycamoreGate(self):
        self.qubit_state = sycamoreGate.sycamoreGate.sycamore_gate(self.qubit_state)
    
    def czGate(self):
        self.qubit_state = czGate.czGate.cz_gate(self.qubit_state)
    
    def getState(self):
        a = self.qubit_state[0][0]
        b = self.qubit_state[1][0]
        c = self.qubit_state[2][0]
        d = self.qubit_state[3][0]
        if((a!=0) or (b!=0)):
            q2 = [[a/((a**2 + b**2)**0.5)],[b/((a**2 + b**2)**0.5)]]
        else:
            q2 = [[c/((c**2 + d**2)**0.5)],[d/((c**2 + d**2)**0.5)]]
        if((a!=0) or (c!=0)):
            q1 = [[a/((a**2 + c**2)**0.5)],[c/((a**2 + c**2)**0.5)]]
        else:
            q1 = [[b/((b**2 + d**2)**0.5)],[d/((b**2 + d**2)**0.5)]]
        return q1, q2