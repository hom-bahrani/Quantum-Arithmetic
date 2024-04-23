# Quantum-Arithmetic-

## Setup

Sign up to IBM Quantum at https://quantum.ibm.com/

Get an API key from the `Manage Account` section and then export this in your environment.

```bash
export IBM_QUANTUM_TOKEN="your_ibm_quantum_token"
```

Install the dependencies:

```bash
python3.9 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Run code

```bash
cd Quantum-Arithmetic-
```

Pass in the numbers to add as command line arguments

```bash
python3 ibm_qiskit/main.py 2 1
```