from envtest import build_circuit

num_qubits = 3
qc = build_circuit(num_qubits)
print(qc)