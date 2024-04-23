import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
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
    n = 8  # Total number of qubits required
    m = 4  # Number of bits in each number
    qc = QuantumCircuit(n, m)  # 8 qubits, 4 classical bits

    # Convert a and b into binary representation
    a_bin = format(a, "04b")
    b_bin = format(b, "04b")
    sum_bin = format(a + b, "04b")  # Expected sum in binary

    # Print the binary representations for debugging
    print("a in binary:", a_bin)
    print("b in binary:", b_bin)
    print("Expected sum in binary:", sum_bin)

    # Initialize the qubits based on the binary representation of the numbers
    for i in range(m):
        if a & (1 << i):
            qc.x(i)  # Set qubit for first number
        if b & (1 << i):
            qc.x(m + i)  # Set qubit for second number

    print("Initial Circuit:")
    print(qc.draw())  # Print the circuit in its initial state

    # Add using quantum gates, correcting for sum and carry
    for i in range(m):
        qc.cx(
            i, m + i
        )  # Apply CX gate for sum calculation, results stored in 'a' qubits
        if i < m - 1:
            qc.ccx(i, m + i, i + 1)  # Compute carry, store in next bit of 'a'

    # Propagate final carries if any
    for i in range(1, m):
        qc.cx(m + i, i)

    qc.barrier()
    qc.measure(
        range(m), range(m)
    )  # Measure the lower half where the results are expected to be

    print("Final Circuit after addition:")
    print(qc.draw())  # Print the circuit after addition

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
    print(qc.draw())


if __name__ == "__main__":
    main()
