import os
from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import SamplerV2 as Sampler, QiskitRuntimeService

# Retrieve the IBM Quantum token from the environment variable
token = os.getenv("IBM_QUANTUM_TOKEN")
if not token:
    raise ValueError("IBM_QUANTUM_TOKEN is not set in the environment variables")

# Bell Circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

service = QiskitRuntimeService(channel="ibm_quantum", token=token)

# Specify a system to use for the noise model
real_backend = service.backend("ibm_brisbane")
aer = AerSimulator.from_backend(real_backend)

# Run the sampler job locally using AerSimulator.
pm = generate_preset_pass_manager(backend=aer, optimization_level=1)
isa_qc = pm.run(qc)
sampler = Sampler(backend=aer)
result = sampler.run([isa_qc]).result()
