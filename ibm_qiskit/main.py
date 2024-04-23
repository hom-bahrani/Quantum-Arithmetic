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
    n = 8  # 8 qubits in total
    m = 4  # We're only handling 4-bit numbers
    qc = QuantumCircuit(
        n, m
    )  # Circuit with 8 qubits and 4 classical bits to store results

    # Binary representations for debugging
    a_bin = format(a, "04b")
    b_bin = format(b, "04b")
    sum_bin = format(a + b, "04b")

    print("a in binary:", a_bin)
    print("b in binary:", b_bin)
    print("Expected sum in binary:", sum_bin)

    # Set initial states based on binary inputs
    for i in range(m):
        if a & (1 << i):
            qc.x(i)
        if b & (1 << i):
            qc.x(m + i)

    print("Initial Circuit:")
    print(qc.draw())

    # Addition using quantum gates
    for i in range(m):
        qc.cx(i, m + i)
        if i < m - 1:  # Propagate carry if not the last bit
            qc.ccx(i, m + i, i + 1)

    # Measure results into classical bits
    for i in range(m):
        qc.measure(m + i, i)  # Measure the result of addition into classical bits

    qc.barrier()

    print("Final Circuit after addition:")
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
