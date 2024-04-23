import os
import math
import argparse
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi


# Function Definitions
def get_counts(simulator, circuit, shots=1000):
    """Return the counts from running a circuit on the Aer."""
    job_statevector = simulator.run(circuit, shots=shots)
    counts = job_statevector.result().get_counts(0)
    return counts


def plot_histogram(counts, title="Histogram", figsize=(7, 5)):
    """Plot a histogram of data from a counts dictionary."""
    if not os.path.exists("results"):
        os.makedirs("results")
    labels, values = zip(*sorted(counts.items()))
    plt.figure(figsize=figsize)
    plt.bar(labels, values, color="b")
    plt.xticks(rotation=90)
    plt.xlabel("State")
    plt.ylabel("Counts")
    plt.title(title)
    plt.savefig(f"results/{title}.png")
    plt.close()


def prepare_circuit(a, b):
    # We'll use 4 qubits for each number and an additional qubit for carry
    num_qubits = 4
    carry = QuantumRegister(1, name="carry")
    a_reg = QuantumRegister(num_qubits, name="a")
    b_reg = QuantumRegister(num_qubits, name="b")
    aux = QuantumRegister(1, name="aux")  # Auxiliary qubit for complex operations
    c_reg = ClassicalRegister(num_qubits, name="c")  # To store the measurement results
    qc = QuantumCircuit(a_reg, b_reg, carry, aux, c_reg)

    # Initialize the quantum circuit with binary values of a and b
    a_bin = format(a, "04b")[::-1]  # Reverse to match LSB to MSB
    b_bin = format(b, "04b")[::-1]

    # Set qubits based on binary input
    for i in range(num_qubits):
        if a_bin[i] == "1":
            qc.x(a_reg[i])
        if b_bin[i] == "1":
            qc.x(b_reg[i])

    # Addition logic using quantum gates
    for i in range(num_qubits - 1):
        qc.cx(a_reg[i], b_reg[i])
        qc.ccx(a_reg[i], b_reg[i], carry[0])
        if i < num_qubits - 1:
            qc.ccx(carry[0], b_reg[i + 1], aux[0])  # Use auxiliary qubit
            qc.cx(aux[0], b_reg[i + 1])
        qc.cx(carry[0], a_reg[i + 1])

    # Last bit addition
    qc.cx(a_reg[num_qubits - 1], b_reg[num_qubits - 1])
    qc.ccx(a_reg[num_qubits - 1], b_reg[num_qubits - 1], carry[0])

    # Measure the result
    for i in range(num_qubits):
        qc.measure(b_reg[i], c_reg[i])

    print("Initial Circuit:")
    print(qc.draw())

    return qc


def main():
    parser = argparse.ArgumentParser(
        description="Add two numbers using a quantum circuit."
    )
    parser.add_argument("num1", type=int, help="First number to add.")
    parser.add_argument("num2", type=int, help="Second number to add.")
    args = parser.parse_args()

    # Check if the sum of the numbers is within the allowed range
    if args.num1 + args.num2 > 15:
        raise ValueError("The sum of the numbers must not exceed 15.")

    shots = 10000
    simulator = AerSimulator(method="statevector")

    # Create and run the quantum circuit
    qc = prepare_circuit(args.num1, args.num2)
    counts = get_counts(simulator, qc, shots=shots)
    print("Final counts:", counts)
    plot_histogram(counts, title=f"Result_of_Adding_{args.num1}_and_{args.num2}")


if __name__ == "__main__":
    main()
