import gates.pauligates as pauliGates
import gates.hadamardgate as hGate
import gates.measure as measurementGates
import gates.phasedgate as pGate
import gates.ugate as uGate

class SingleQubit:

    def __init__(self, x):
        if(x<=1 and x>=0):
            y = (1 - x**2)**0.5
            self.qubit_state = [[x],[y]]
        else:
            raise Exception("Enter a valid qubit state")

    def print_state(self):
        # print(str(self.qubit_state[0][0]) + "|0} + " + str(self.qubit_state[1][0]) + "|1}")
        print(self.qubit_state)
    
    def Xgate(self):
        self.qubit_state = pauliGates.PauliGates.pauli_x_gate(self.qubit_state)

    def Ygate(self):
        self.qubit_state = pauliGates.PauliGates.pauli_y_gate(self.qubit_state)

    def Zgate(self):
        self.qubit_state = pauliGates.PauliGates.pauli_z_gate(self.qubit_state)

    def Hgate(self):
        self.qubit_state = hGate.HadamardGate.h_gate(self.qubit_state)
        
    def measure0(self):
        self.qubit_state = measurementGates.measure.measure_x(self.qubit_state)
        print(self.qubit_state[0][0])
        self.qubit_state[0][0] = 1

    def measure1(self):
        self.qubit_state = measurementGates.measure.measure_y(self.qubit_state)
        print(self.qubit_state[1][0])
        self.qubit_state[1][0] = 1

    def Pgate(self, phase):
        self.qubit_state = pGate.phased_gate.p_gate(self.qubit_state, phase)
        
    def VirtualZgate(self):
        self.qubit_state = pGate.phased_gate.virtual_z_gate(self.qubit_state)

    def Igate(self):
        self.qubit_state = pGate.phased_gate.i_gate(self.qubit_state)

    def Sgate(self):
        self.qubit_state = pGate.phased_gate.s_gate(self.qubit_state)
    
    def Sdaggergate(self):
        self.qubit_state = pGate.phased_gate.s_dagger_gate(self.qubit_state)

    def Tgate(self):
        self.qubit_state = pGate.phased_gate.t_gate(self.qubit_state)
    
    def Tdaggergate(self):
        self.qubit_state = pGate.phased_gate.t_dagger_gate(self.qubit_state)

    def Ugate(self, theta, phi, lamda):
        self.qubit_state = uGate.u_gate.u_gate(self.qubit_state, theta, phi, lamda)
        