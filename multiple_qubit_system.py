

class MultipleQubitSystem:

    def __init__(self, n):
        if(n>10):
            raise Exception("The maximum permissble number of qubits is 10")
        else:
            self.num_of_qubits = n
            qubit_state = [[1],[0]]
            system_state = []
            for i in range(n+1):
                system_state.append(qubit_state)
            self.qubit_state = system_state

    def setQubits(self, qubit_num, one_state_value):
        if(self.num_of_qubits<qubit_num):
            raise Exception("Required Qubit number does not exist")
        else:
            zero_state_value = (1 - one_state_value**2)**0.5
            self.qubit_state[qubit_num-1] = [[zero_state_value], [one_state_value]]