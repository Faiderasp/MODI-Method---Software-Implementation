# MODI Solver – Transportation Optimization

A Python-based software project that implements the **MODI (Modified Distribution) Method**, also known as the **U-V Method**, to solve transportation problems in Linear Programming.

## About the Project

MODI Solver is an academic project developed as part of an Operations Research course. Its main purpose is to implement the MODI algorithm to find an optimal transportation plan while minimizing total transportation costs.

The software aims to automate the mathematical procedures involved in the method, making it easier to understand, calculate, and analyze transportation optimization problems.

## What is the MODI Method?

The MODI Method is an optimization technique used to determine whether an initial feasible solution to a transportation problem is optimal.

It works by calculating row and column potentials (U and V), evaluating opportunity costs, and improving the current allocation whenever a better solution is possible.

The process continues until the optimality condition is satisfied.

## Main Features

- Transportation problem configuration.
- Cost matrix input.
- Supply and demand management.
- Initial feasible solution generation.
- Calculation of U and V potentials.
- Opportunity cost calculation.
- Entering cell identification.
- Closed-loop construction.
- Theta calculation and allocation adjustment.
- Iterative optimization process.
- Optimal transportation cost calculation.

*Features will be updated as development progresses.*

## Technologies

- **Python** – Core programming language.
- **NumPy** – Numerical and matrix operations.
- **Tkinter / CustomTkinter** – Graphical user interface (depending on implementation).
- **Matplotlib** – Data visualization (if implemented).

## Project Structure

```text
MODI-Solver/
│
├── main.py
│
├── algorithms/
│   ├── northwest.py
│   ├── potentials.py
│   ├── opportunity_cost.py
│   ├── cycles.py
│   └── modi.py
│
├── models/
│   └── transportation.py
│
├── interface/
│   ├── window.py
│   ├── input_form.py
│   └── results.py
│
├── tests/
│   └── test_modi.py
│
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Faiderasp/MODI-Method---Software-Implementation.git
```

### 2. Navigate to the project directory

```bash
cd MODI-Solver
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

## How It Works

The MODI algorithm follows these steps:

1. Define the transportation problem using costs, supply, and demand.
2. Generate an initial feasible solution.
3. Calculate the U and V potentials for occupied cells.
4. Calculate opportunity costs for unoccupied cells.
5. Check the optimality condition.
6. Identify the entering cell if an improvement is possible.
7. Construct a closed loop and determine the adjustment value (Theta).
8. Update the allocations.
9. Repeat the process until an optimal solution is found.

## Example

Consider the following transportation cost matrix:

| | Destination 1 | Destination 2 | Destination 3 | Supply |
|---|---:|---:|---:|---:|
| Origin 1 | 4 | 8 | 8 | 20 |
| Origin 2 | 2 | 5 | 7 | 30 |
| Origin 3 | 6 | 4 | 3 | 25 |
| **Demand** | **10** | **35** | **30** | **75** |

The objective is to determine the optimal allocation that satisfies all supply and demand constraints while minimizing the total transportation cost.

## Academic Context

This project is being developed in pairs as a final project for an Operations Research course.

The implementation focuses on understanding and applying the mathematical principles behind the MODI algorithm through original programming and problem-solving.

## Authors

Developed by:

- [Developer Name](https://github.com/Faiderasp)

## License

This project was developed for academic and educational purposes.
