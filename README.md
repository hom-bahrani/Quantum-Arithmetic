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