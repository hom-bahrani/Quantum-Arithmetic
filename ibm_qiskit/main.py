from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import (
    SamplerV2 as Sampler,
    QiskitRuntimeService,
    IBMRuntimeService,
)


def main(args=None):
    # Create a Quantum Circuit acting on a quantum register of four qubits
    qc = QuantumCircuit(4)

    # Initialize the state to binary number 1 (0001)
    qc.x(0)  # Apply X gate to the least significant qubit

    # Add the binary number 2 (0010) to it
    qc.cx(0, 1)  # Flip the second least significant qubit if the first qubit is 1
    qc.x(0)  # Reset the first qubit back to 0

    # Add a barrier to prevent optimization changes
    qc.barrier()

    # Map the quantum measurement to the classical bits
    qc.measure_all()

    service = QiskitRuntimeService()

    # Specify a system to use for the noise model
    real_backend = service.backend("ibm_brisbane")
    aer = AerSimulator.from_backend(real_backend)

    # Run the sampler job locally using AerSimulator.
    pm = generate_preset_pass_manager(backend=aer, optimization_level=1)
    isa_qc = pm.run(qc)
    sampler = Sampler(backend=aer)
    result = sampler.run([isa_qc]).result()

    # Extract and Print States
    measurement_results = result.quasi_dists[0]

    print("Measured States and their Probabilities:")
    for state, probability in measurement_results.items():
        print(f"State: {state}, Probability: {probability}")

    # # Drawing the circuit
    # print("Circuit:")
    # print(qc.draw(output="text"))


if __name__ == "__main__":
    main()
