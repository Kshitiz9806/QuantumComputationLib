Quantum Computation library to implement qubit gates.
To use import the single_qubit.py file into your project and create an object from the class singleQubit

Methods accessible (gates):
print_state()
    prints the current state of the qubit to the terminal

Xgate()
    pauli x gate

Ygate()
    pauli y gate

Zgate()
    pauli z gate

Hgate()
    hadamard gate

measure0()
    take a measurement of the qubit in the |0} direction

measure1()
    take a measurement of the qubit in the |1} direction

Pgate(phase)
    phase that rotates the qubit in the bloch sphere by the given phase along the z direction

VirtualZgate()
    phase gate with phase as pi

Igate()
    identity gate

Sgate()
    phase gate with phase as pi/2

Sdaggergate()
    phase gate with phase as -pi/2

Tgate()
    phase gate with phase as pi/4

Tdaggergate()
    phase gate with phase as -pi/4

Ugate(theta, phi, lambda)
    u gate with parameters theta, phi and lambda