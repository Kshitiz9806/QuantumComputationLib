import single_qubit as singleQubit
import double_qubit_system as doubleQubit

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

    def cnotGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.cnotGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def swapGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.swapGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def sqrtSwapGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.sqrtSwapGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def sqrtISwapGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.sqrtISwapGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def sycamoreGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.sycamoreGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def czGate(self, qubit1, qubit2):
        if(self.num_of_qubits<qubit1 or self.num_of_qubits<qubit2):
            raise Exception("Required Qubit numbers does not exist")
        else:
            q1 = singleQubit.SingleQubit(self.qubit_state[qubit1-1][1][0])
            q2 = singleQubit.SingleQubit(self.qubit_state[qubit2-1][1][0])
            twoQubitSystem = doubleQubit.DoubleQubitSystem(q1, q2)
            twoQubitSystem.czGate()
            q1, q2 = twoQubitSystem.getState()
            self.qubit_state[qubit1-1] = q1
            self.qubit_state[qubit2-1] = q2

    def printState(self):
        print("Printing State of all " + str(self.num_of_qubits) + " qubits")
        for i in range(self.num_of_qubits):
            print("Qubit " + str(i+1) + "----->")
            print(str(self.qubit_state[i][0][0]) + "|0} + " +  str(self.qubit_state[i][1][0]) + "|1}")