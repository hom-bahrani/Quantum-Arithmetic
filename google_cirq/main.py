import os
import numpy as np
import matplotlib.pyplot as plt
import cirq


# Define function to get measurement results in histogram form
def get_counts(circuit, simulator, repetitions=1000):
    """Simulate a quantum circuit and return the measurement counts."""
    result = simulator.run(circuit, repetitions=repetitions)
    counts = result.histogram(
        key="m", fold_func=lambda bits: "".join(str(b) for b in reversed(bits))
    )
    return counts


# Function to plot histogram
def plot_histogram(counts, title="Histogram", figsize=(7, 5)):
    """Plot a histogram from a counts dictionary."""
    if not os.path.exists("results"):
        os.makedirs("results")
    labels, values = zip(*sorted(counts.items()))
    plt.figure(figsize=figsize)
    plt.bar([bin(int(l))[2:].zfill(4) for l in labels], values, color="b")
    plt.xticks(rotation=90)
    plt.xlabel("State")
    plt.ylabel("Counts")
    plt.title(title)
    plt.savefig(f"results/{title}.png")
    plt.close()


# Initialize the simulator
simulator = cirq.Simulator()

# Define qubits
qubits = cirq.LineQubit.range(4)

# Create a Quantum Circuit
circuit = cirq.Circuit()

# Initialize the state to binary number 1 (0001)
circuit.append(cirq.X(qubits[0]))  # Apply X gate to the least significant qubit

# Add the binary number 2 (0010) to it
circuit.append(
    cirq.CNOT(qubits[0], qubits[1])
)  # Flip the second least significant qubit if the first is 1
circuit.append(cirq.X(qubits[0]))  # Reset the first qubit back to 0

# Add a barrier to prevent optimization changes (barriers do not exist in Cirq, thus it's more symbolic)
circuit.append(cirq.Moment())  # A Moment in Cirq can act as a visual separator

# Map the quantum measurement to the classical bits
circuit.append(cirq.measure(*qubits, key="m"))

# Run simulation
repetitions = 10000
counts = get_counts(circuit, simulator, repetitions=repetitions)

# Plot histogram
print("Final counts:", counts)
plot_histogram(counts, title="State_counts_after_operations")

# Print the circuit
print("Circuit diagram:")
print(circuit)
