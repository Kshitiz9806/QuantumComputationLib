import numpy as np

class NonIdealQubit:

    def __init__(self,  x, freq=5000000000):
        if(x<=1 and x>=0):
            y = (1 - x**2)**0.5
            self.qubit_state = [[y],[x]]
            # self.decays = ideal
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

    def printState(self):
        print("(" + str(self.qubit_state[0][0]) + ")|0} + (" + str(self.qubit_state[1][0]) + ")|1}")