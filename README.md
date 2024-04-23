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

The IBM Qiskit code is implemented to add up different numbers which are pass in as command line arguments.

There is currently a bug in the code (PR's welcome :smiley: )

```bash
python3 ibm_qiskit/main.py 2 1
```

Output:

```bash
Initial Circuit:
       ┌───┐                                                                        
  a_0: ┤ X ├──■────■────────────────────────────────────────────────────────────────
       └───┘  │    │                                                                
  a_1: ───────┼────┼────────────■────■──────────────────────────────────────────────
              │    │            │    │                                              
  a_2: ───────┼────┼────────────┼────┼────────────■────■────────────────────────────
              │    │            │    │            │    │                            
  a_3: ───────┼────┼────────────┼────┼────────────┼────┼────────────■────■────■─────
       ┌───┐┌─┴─┐  │       ┌─┐  │    │            │    │            │    │    │     
  b_0: ┤ X ├┤ X ├──■───────┤M├──┼────┼────────────┼────┼────────────┼────┼────┼─────
       └───┘└───┘  │  ┌───┐└╥┘┌─┴─┐  │       ┌─┐  │    │            │    │    │     
  b_1: ────────────┼──┤ X ├─╫─┤ X ├──■───────┤M├──┼────┼────────────┼────┼────┼─────
                   │  └─┬─┘ ║ └───┘  │  ┌───┐└╥┘┌─┴─┐  │       ┌─┐  │    │    │     
  b_2: ────────────┼────┼───╫────────┼──┤ X ├─╫─┤ X ├──■───────┤M├──┼────┼────┼─────
                   │    │   ║        │  └─┬─┘ ║ └───┘  │  ┌───┐└╥┘┌─┴─┐┌─┴─┐  │  ┌─┐
  b_3: ────────────┼────┼───╫────────┼────┼───╫────────┼──┤ X ├─╫─┤ X ├┤ X ├──■──┤M├
                 ┌─┴─┐  │   ║      ┌─┴─┐  │   ║      ┌─┴─┐└─┬─┘ ║ └───┘└───┘┌─┴─┐└╥┘
carry: ──────────┤ X ├──■───╫──────┤ X ├──■───╫──────┤ X ├──■───╫───────────┤ X ├─╫─
                 └───┘      ║      └───┘      ║      └───┘      ║           └───┘ ║ 
  aux: ─────────────────────╫─────────────────╫─────────────────╫─────────────────╫─
                            ║                 ║                 ║                 ║ 
  c: 4/═════════════════════╩═════════════════╩═════════════════╩═════════════════╩═
                            0                 1                 2                 3 
Final counts: {'0000': 10000}
```