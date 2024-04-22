import os
import cirq
import numpy as np
import matplotlib.pyplot as plt

from cirq_sim import sim_engine, processor_id


q0 = cirq.GridQubit(4, 4)
q1 = cirq.GridQubit(4, 5)
circuit = cirq.Circuit(
    cirq.X(q0), cirq.SQRT_ISWAP(q0, q1), cirq.measure([q0, q1], key="measure")
)

results = sim_engine.get_sampler(processor_id).run(circuit, repetitions=3000)
print(results.histogram(key="measure"))

# Save the results
counts = results.measurements["measure"]

# Convert the binary results to decimal
decimal_counts = counts.dot(1 << np.arange(counts.shape[-1] - 1, -1, -1))

# Get unique measurement outcomes and their counts
unique_outcomes, unique_counts = np.unique(decimal_counts, return_counts=True)

# Plot the histogram for all possible outcomes
plt.bar(
    range(4),
    [
        unique_counts[unique_outcomes == i][0] if i in unique_outcomes else 0
        for i in range(4)
    ],
    tick_label=range(4),
)

plt.xlabel("Measurement Outcome (decimal)")
plt.ylabel("Frequency")
plt.title("Histogram of Quantum Circuit Simulation Results")

# Ensure the "results" directory exists and save the plot
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
plt.savefig(os.path.join(results_dir, "measurement_histogram.png"))

# Draw the circuit
print("Circuit:")
print(circuit)
