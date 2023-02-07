# QUANTUM COMPUTATION LIBRARY

Quantum Computation library to implement qubit gates.
To use import the single_qubit.py, double_qubit_system.py, or multiple_qubit_system.py file as per usage

## Methods accessible for single qubit:

* SingleQubit(x) -> Takes integer x as the probability of state |1} and initializes qubit

* print_state() -> Prints the current state of the qubit to the terminal

* xGate() -> Pauli x gate

* yGate() -> Pauli y gate

* zGate() -> Pauli z gate

* hGate() -> Hadamard gate

* measure0() -> Take a measurement of the qubit in the |0} direction

* measure1() -> Take a measurement of the qubit in the |1} direction

* pGate(phase) -> Phase that rotates the qubit in the bloch sphere by the given phase along the z direction

* virtualzGate() -> Phase gate with phase as pi

* iGate() -> Identity gate

* sGate() -> Phase gate with phase as pi/2

* sDaggerGate() -> Phase gate with phase as -pi/2

* tGate() -> Phase gate with phase as pi/4

* tDaggerGate() -> Phase gate with phase as -pi/4

* uGate(theta, phi, lambda) -> U gate with parameters theta, phi and lambda

## Methods accessible for double qubit system:

* DoubleQubitSystem(q1, q2) -> Takes two single qubits and returns the entagled two qubit system for them

* print_state() -> Prints the current state of the qubit to the terminal

* cnotGate() -> Controlled not gate where first qubit acts as the control qubit

* swapGate() -> Swaps the two qubits as per usage

* sqrtSwapGate() -> Square root swap gate

* sqrtISwapGate() -> Square root i swap gate

* sycamoreGate() - > Sycamore gate

* czGate() -> CZ gate

## Methods accessible for multiple qubit system:
You can create a multiple qubits system with as max as 10 qubits and operate single and double qubit gates on these qubits accordingly.

* MultipleQubitSystem(k) -> Creates a multiple qubit system with k qubits with initial state |0}.

* setQubits(k, a) -> Sets the kth qubit probablity of |1} as a.

* xGate(k) -> Pauli x gate on kth qubit.

* yGate(k) -> Pauli y gate on kth qubit.

* zGate(k) -> Pauli z gate on kth qubit.

* hGate(k) -> Hadamard gate on kth qubit.

* pGate(k, phase) -> Phase that rotates the qubit in the bloch sphere by the given phase along the z direction on the kth qubit.

* virtualzGate(k) -> Phase gate with phase as pi on the kth qubit.

* iGate(k) -> Identity gate on the kth qubit.

* sGate(k) -> Phase gate with phase as pi/2 on the kth qubit.

* sDaggerGate(k) -> Phase gate with phase as -pi/2 on the kth qubit.

* tGate(k) -> Phase gate with phase as pi/4 on the kth qubit.

* tDaggerGate(k) -> Phase gate with phase as -pi/4 on the kth qubit.

* uGate(k, theta, phi, lambda) -> U gate with parameters theta, phi and lambda on the kth qubit.

* cnotGate(k1, k2) -> Controlled not gate where k1th qubit acts as the k2th control qubit.

* swapGate(k1, k2) -> Swaps the two qubits as per usage

* sqrtSwapGate(k1, k2) -> Square root swap gate on the k1 and k2 qubit.

* sqrtISwapGate(k1, k2) -> Square root i swap gate on the k1 and k2 qubit.

* sycamoreGate(k1, k2) - > Sycamore gate on the k1 and k2 qubit.

* czGate(k1, k2) -> CZ gate on the k1 and k2 qubit.