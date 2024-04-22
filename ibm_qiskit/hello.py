import os

import numpy as np
import matplotlib.pyplot as plt

# Import Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi

# Create circuit
circ = QuantumCircuit(2)
circ.h(0)
circ.cx(0, 1)
circ.measure_all()

# Transpile for simulator
shots = 10000
simulator = AerSimulator(method="statevector")

job_statevector = simulator.run(circ, shots=shots)
counts = job_statevector.result().get_counts(0)

plot_histogram(counts, title="Bell-State counts")

if not os.path.exists("results"):
    os.makedirs("results")

plt.figure()  # Create a new figure
plt.bar(counts.keys(), counts.values())
plt.xlabel("State")
plt.ylabel("Counts")
plt.title("Bell-State counts")

# Save the histogram
plt.savefig("results/bell_state_histogram.png")
plt.close()  # Close the figure
