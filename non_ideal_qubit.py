import numpy as np
import gates.ugate as uGate

class NonIdealQubit:

    def __init__(self,  x, freq=5000000000):
        if(x<=1 and x>=0):
            y = (1 - x**2)**0.5
            self.qubit_state = [[y],[x]]
            self.omega = 2*np.pi*freq
            self.driveline_dissipation_qf = 50000000
            self.driveline_noise_qf = 50000000
            self.instrinsic_qf = 4000000
            self.readout_qf = 104719755119659774.61
        else:
            raise Exception("Enter a valid qubit state")

    def decoherenceDecay(self, time):
        a = self.qubit_state[0][0]
        b = self.qubit_state[1][0]
        qf_total = self.driveline_dissipation_qf + self.driveline_noise_qf + self.instrinsic_qf + self.readout_qf
        omega = self.omega
        time = time/1000000000
        a_final = (1 + (a**2-1)*np.exp(-qf_total*time/omega))**0.5
        b_final = ((b**2)*np.exp(-qf_total*time/omega))**0.5
        self.qubit_state = [[a_final],[b_final]]

    def printState( self):
        print("(" + str(self.qubit_state[0][0]) + ")|0} + (" + str(self.qubit_state[1][0]) + ")|1}")

    def xGate(self):
        steps = 1000
        gate_time = 50
        phase_steps = np.pi/(2*steps)
        time_steps = gate_time/steps
        b_start_value = self.qubit_state[1][0]
        a_start_value = self.qubit_state[0][0]
        f1 = np.cos(phase_steps)
        f2 = np.sin(phase_steps)
        for step in range(0, steps):
            b = self.qubit_state[0][0]
            a = self.qubit_state[1][0] 
            if(a_start_value<0):
                a = -1*a
            if(b_start_value<0):
                b = -1*b
            b = b*f1 - a*f2
            a = a*f1 + b*f2
            b_start_value = b
            a_start_value = a
            self.qubit_state = [[abs(b)],[abs(a)]]
            self.decoherenceDecay(time_steps)

    def hGate(self):
        steps = 1000
        gate_time = 50
        phase_steps = np.pi/(4*steps)
        time_steps = gate_time/steps
        b_start_value = self.qubit_state[1][0]
        a_start_value = self.qubit_state[0][0]
        f1 = np.cos(phase_steps)
        f2 = np.sin(phase_steps)
        for step in range(0, steps):
            b = self.qubit_state[0][0]
            a = self.qubit_state[1][0] 
            if(a_start_value<0):
                a = -1*a
            if(b_start_value<0):
                b = -1*b
            b = b*f1 - a*f2
            a = a*f1 + b*f2
            b_start_value = b
            a_start_value = a
            self.qubit_state = [[abs(b)],[abs(a)]]
            self.decoherenceDecay(time_steps)

    def uGate(self, theta, phi, lamda):
        steps = 1000
        gate_time = 50
        theta_steps = theta/steps
        phi_steps = phi/steps
        lamda_steps = lamda/steps
        time_steps  = gate_time/steps
        for step in range(0, steps):
            self.qubit_state = uGate.u_gate.u_gate(self.qubit_state, theta_steps, phi_steps, lamda_steps)
            self.decoherenceDecay(time_steps)