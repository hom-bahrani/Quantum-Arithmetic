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

    # Prepare the quantum circuit to add two binary numbers a and b
    # Initialize the qubits based on the binary representation of the numbers
    for i in range(m):  # m is 4, for the binary digits
        if a & (1 << i):
            qc.x(i)  # Setting up the first number
        if b & (1 << i):
            qc.x(m + i)  # Setting up the second number

    # Addition logic using a series of CX and CCX gates to perform binary addition
    # We'll use qubits q_0 to q_3 for 'a', q_4 to q_7 for 'b', and calculate into 'a'
    for i in range(m - 1):
        # Use an ancilla qubit for the carry (qubits q_4 to q_7)
        qc.ccx(
            i, m + i, m + i + 1
        )  # Compute the carry from bits i and m+i, store in m+i+1
        qc.cx(i, m + i)  # Compute the sum for bit i, store in m+i
        qc.ccx(i, m + i, m + i + 1)  # Apply correction to carry if necessary

    # Handle the last bit separately (no carry out needed)
    qc.cx(m - 1, 2 * m - 1)  # Just compute the sum for the last bit

    qc.barrier()
    # Measure only the bits that stored the result of the addition
    qc.measure(range(m), range(m))  # Output the result in the first 4 classical bits
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
