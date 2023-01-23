import single_qubit as singleQubit

class MultipleQubitSystem:

    def __init__(self, n):
        if(n>10):
            raise Exception("The maximum permissble number of qubits is 10")
        else:
            self.num_of_qubits = n
            qubit_state = [[1],[0]]
            system_state = []
            for i in range(n):
                system_state.append(qubit_state)
            self.qubit_state = system_state

    def setQubits(self, qubit_num, one_state_value):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            zero_state_value = (1 - one_state_value**2)**0.5
            self.qubit_state[qubit_num-1] = [[zero_state_value], [one_state_value]]

    def xGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.xGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def yGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.yGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def zGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.zGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def hGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.hGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def pGate(self, qubit_num, phase):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.pGate(phase)
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def virtualzGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.virtualzGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def iGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.iGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def sGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.sGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def sDaggerGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.sDaggerGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def tGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.tGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def tDaggerGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.tDaggerGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()

    def uGate(self, qubit_num):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            qubit = self.qubit_state[qubit_num-1]
            qubit_obj = singleQubit.SingleQubit(qubit[1][0])
            qubit_obj.uGate()
            self.qubit_state[qubit_num-1] = qubit_obj.getState()