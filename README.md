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

The Google Cirq code only adds 1 + 1

```
python3 google_cirq/main.py
```

IBM's Qiskit code adds an integer to register 'a', but this addition is controlled by the qubits in register 'b'. This means the values in 'b' (including superpositions) directly influence the outcome of the addition.

```bash
python3 ibm_qiskit/main.py
```

Output:

```bash
Circuit:
           ┌───┐            ░                                              ┌───┐                         
      a_0: ┤ X ├────────────░───■───────────────────■────■─────────■────■──┤ X ├─────────────────────────
           └───┘            ░   │                   │    │         │  ┌─┴─┐└─┬─┘                    ┌───┐
      a_1: ─────────────────░───┼────■─────────■────┼────┼────■────┼──┤ X ├──┼────■─────────■────■──┤ X ├
           ┌───┐┌─────────┐ ░   │    │         │    │    │  ┌─┴─┐  │  └─┬─┘  │    │         │  ┌─┴─┐└─┬─┘
      a_2: ┤ H ├┤ Rz(π/4) ├─░───┼────■─────────■────┼────┼──┤ X ├──┼────┼────┼────┼────■────┼──┤ X ├──┼──
           └───┘└─────────┘ ░   │    │  ┌───┐  │    │    │  └─┬─┘  │    │    │    │  ┌─┴─┐  │  └─┬─┘  │  
      a_3: ─────────────────░───┼────┼──┤ X ├──┼────┼────┼────┼────┼────┼────┼────┼──┤ X ├──┼────┼────┼──
           ┌───┐            ░   │    │  └─┬─┘  │    │    │    │    │    │    │    │  └─┬─┘  │    │    │  
      b_0: ┤ X ├────────────░───■────┼────┼────┼────■────■────┼────■────■────■────┼────┼────┼────┼────┼──
           ├───┤┌─────────┐ ░   │    │    │    │    │    │    │    │              │    │    │    │    │  
      b_1: ┤ H ├┤ Rz(π/2) ├─░───┼────┼────┼────┼────┼────┼────┼────┼──────────────■────┼────■────■────■──
           └───┘└─────────┘ ░ ┌─┴─┐  │    │    │  ┌─┴─┐┌─┴─┐  │  ┌─┴─┐          ┌─┴─┐  │  ┌─┴─┐          
scratch_0: ─────────────────░─┤ X ├──┼────■────┼──┤ X ├┤ X ├──■──┤ X ├──────────┤ X ├──■──┤ X ├──────────
                            ░ └───┘┌─┴─┐  │  ┌─┴─┐└───┘└───┘     └───┘          └───┘     └───┘          
scratch_1: ─────────────────░──────┤ X ├──■──┤ X ├───────────────────────────────────────────────────────
                            ░      └───┘     └───┘                                                       
      c: 4/══════════════════════════════════════════════════════════════════════════════════════════════
```

## Next Steps

A useful next step is to explore in depth the effects of superposition and entanglement in our quantum circuit for addition. I've touched on this slightly but as you can see from the circuit diagram these quantum effects bring several theoretical and practical advantages, especially when viewed through the lens of quantum computing capabilities and future applications:

1. **Exploring Multiple States Simultaneously**:
   - **Superposition** allows a quantum system to be in multiple states at once. For an operation like addition, this means the circuit can simultaneously process multiple potential sums. For instance, if your inputs are in superposition, the circuit can effectively perform multiple addition operations in parallel, leading to what is often referred to as quantum parallelism. This can be advantageous in scenarios where you need to perform the same operation across a range of inputs.

2. **Harnessing Quantum Parallelism**:
   - When qubits are in superposition, operations on them affect all possible states simultaneously. In the context of quantum arithmetic, this allows for the computation of multiple outputs at once. For example, using superposition, a quantum circuit could add different pairs of numbers in one go, which is a powerful feature for algorithms that require the evaluation of functions over many inputs (like in search algorithms or optimization problems).

3. **Entanglement and Conditional Operations**:
   - **Entanglement** is a phenomenon where qubits become interconnected such that the state of one (whether in superposition or not) directly correlates with the state of another, no matter the distance between them. In our circuit, entanglement is used to implement conditional logic (like the controlled NOT and Toffoli gates) that is critical for carrying out addition correctly—ensuring that carries are handled properly and that the sum reflects these carries.

4. **Quantum Interference**:
   - This is used to constructively or destructively combine amplitudes (probabilities of quantum states), steering the system toward a desired quantum state. In computational tasks, interference helps in amplifying correct paths (answers) while canceling out the wrong ones.

5. **Practical Implications and Potential**:
   - While it might seem that keeping a binary, deterministic state for each number would be simpler and more practical for addition, the use of superposition and entanglement allows quantum computers to test and develop methods that could scale to solve more complex problems that are not feasible on classical systems. This includes large-scale simulations, optimizations, and cryptographic calculations.
