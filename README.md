Quantum Computation library to implement qubit gates.
To use import the single_qubit.py file into your project and create an object from the class singleQubit

Methods accessible for single qubit:

SingleQubit(x) -> takes integer x as the probability of state |1} and initializes qubit
print_state() -> prints the current state of the qubit to the terminal
xGate() -> pauli x gate
yGate() -> pauli y gate
zGate() -> pauli z gate
hGate() -> hadamard gate
measure0() -> take a measurement of the qubit in the |0} direction
measure1() -> take a measurement of the qubit in the |1} direction
pGate(phase) -> phase that rotates the qubit in the bloch sphere by the given phase along the z direction
virtualzGate() -> phase gate with phase as pi
iGate() -> identity gate
sGate() -> phase gate with phase as pi/2
sDaggerGate() -> phase gate with phase as -pi/2
tGate() -> phase gate with phase as pi/4
tDaggerGate() -> phase gate with phase as -pi/4
uGate(theta, phi, lambda) -> u gate with parameters theta, phi and lambda

Methods accessible for double qubit system:

DoubleQubitSystem(q1, q2) -> takes two single qubits and returns the entagled two qubit system for them
print_state() -> prints the current state of the qubit to the terminal
cnotGate() -> controlled not gate where first qubit acts as the control qubit
swapGate() -> swaps the two qubits as per usage
sqrtSwapGate() -> square root swap gate
sqrtISwapGate() -> square root i swap gate
sycamoreGate() - > sycamore gate
czGate() -> cz gate