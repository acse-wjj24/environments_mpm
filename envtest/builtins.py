import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
from qiskit import QuantumCircuit

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'build_circuit']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv() * b

def build_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)
    # build circuits with random gates
    qc.h(range(num_qubits))
    qc.barrier()
    qc.measure_all()
    return qc
    
    