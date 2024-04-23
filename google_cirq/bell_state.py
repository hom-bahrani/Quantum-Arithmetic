import os
import cirq
import numpy as np
import matplotlib.pyplot as plt

from cirq_sim import sim_engine, processor_id

# Define qubits
q0, q1 = cirq.LineQubit.range(2)

# Define the circuit for creating a Bell state
circuit = cirq.Circuit()
circuit.append([cirq.H(q0), cirq.CNOT(q0, q1), cirq.measure(q0, q1, key="m")])

# Initialize simulator
simulator = cirq.Simulator()

# Simulate the circuit
result = simulator.run(circuit, repetitions=10000)
counts = result.histogram(key="m")


# Function to plot histogram
def plot_histogram(counts, title="Histogram"):
    labels = list(counts.keys())
    values = list(counts.values())
    plt.bar(labels, values, tick_label=[f"{i:02b}" for i in labels])
    plt.xlabel("State")
    plt.ylabel("Counts")
    plt.title(title)
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    plt.savefig(f"{results_dir}/{title}.png")
    plt.close()


# Plotting the histogram
plot_histogram(counts, "Bell_state_cirq")

# Optional: print the circuit
print("Circuit:")
print(circuit)
