# MODI Method - Software Implementation

A Python-based implementation for solving and optimizing transportation problems in Linear Programming using the **MODI (Modified Distribution) Method**, also known as the **U-V Method**.

---

## 📌 About the Project

This project was developed as part of an **Operations Research** course. Its main goal is to solve transportation optimization problems by determining the optimal distribution plan that minimizes the total shipping cost while satisfying supply and demand constraints.

The project follows a layered modular architecture consisting of a controller, data models, service layer, and interface helper utilities.

---

## 🧠 What is the MODI Method?

The **MODI Method** (Modified Distribution / U-V Method) is an optimization technique used to evaluate whether an initial feasible solution to a transportation problem is optimal:

1. **Calculate Potentials:** Assign values $u_i$ (row/origin potentials) and $v_j$ (column/destination potentials) such that $u_i + v_j = c_{ij}$ for all occupied (basic) cells.
2. **Evaluate Opportunity Costs:** Compute the marginal opportunity cost $\Delta_{ij} = c_{ij} - (u_i + v_j)$ for all unoccupied (non-basic) cells.
3. **Optimality Check:** If all $\Delta_{ij} \ge 0$, the current solution is optimal. If any negative values exist, an entering cell is selected to construct a closed reallocation loop ($\theta$) to reduce the total cost until the minimum is achieved.

---

## 📁 Project Structure

```text
MODI Method - Software Implementation/
│
├── controller/
│   ├── __init__.py
│   └── controller.py       # Main controller: orchestrates solving and calculates total costs
│
├── models/
│   └── Model.py            # Data classes (DataProblem, TotalCost) for structured problem definition
│
├── service/
│   ├── __init__.py
│   └── service.py          # Service logic implementing MODI resolution via OTTools
│
├── interface/
│   └── helpers.py          # Logging helpers and console output formatters
│
├── tests/                  # Directory for unit tests
├── app.py                  # Application entry point and demo problem execution
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```

---

## 🛠️ Technologies & Libraries

- **[Python](https://www.python.org/)** (v3.10+) – Core programming language.
- **[NumPy](https://numpy.org/)** – Matrix operations and array handling.
- **[OTTools](https://pypi.org/project/OTTools/)** – Transportation Problem optimization solver.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Faiderasp/MODI-Method---Software-Implementation.git
cd "MODI Method - Software Implementation"
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

---

## 📖 Sample Problem Formulation

A manufacturing company produces goods across **3 production plants** ($P_1, P_2, P_3$) and needs to distribute them to **3 fulfillment centers** ($D_1, D_2, D_3$).

### Problem Parameters

- **Production Capacities (Supply):**
  - Plant 1 ($P_1$): 20 units
  - Plant 2 ($P_2$): 30 units
  - Plant 3 ($P_3$): 25 units
  - Total Supply: $20 + 30 + 25 = \mathbf{75\text{ units}}$

- **Customer Requirements (Demand):**
  - Center 1 ($D_1$): 10 units
  - Center 2 ($D_2$): 35 units
  - Center 3 ($D_3$): 30 units
  - Total Demand: $10 + 35 + 30 = \mathbf{75\text{ units}}$ *(Balanced problem)*

- **Unit Transportation Cost Matrix ($c_{ij}$ in USD):**

| Origin / Destination | Center 1 ($D_1$) | Center 2 ($D_2$) | Center 3 ($D_3$) | Supply ($O_i$) |
| :--- | :---: | :---: | :---: | :---: |
| **Plant 1 ($P_1$)** | $\$4$ | $\$8$ | $\$8$ | **20** |
| **Plant 2 ($P_2$)** | $\$2$ | $\$5$ | $\$7$ | **30** |
| **Plant 3 ($P_3$)** | $\$6$ | $\$4$ | $\$3$ | **25** |
| **Demand ($D_j$)** | **10** | **35** | **30** | **75** |

---

## 💻 Python Execution

This problem is modeled in `app.py`:

```python
from controller.controller import c_MODI
from interface.helpers import printer

# Unit shipping costs matrix
costs = [
    [4, 8, 8],
    [2, 5, 7],
    [6, 4, 3]
]

# Supply capacities (Origins)
offer = [20, 30, 25]

# Demand requirements (Destinations)
demand = [10, 35, 30]

# Initial basic allocation (optional baseline)
assignment = [
    [10, 5, 5],
    [0, 30, 0],
    [0, 0, 25]
]

# Run MODI solver controller
result = c_MODI(p_costs=costs, p_demand=demand, p_offer=offer, p_assignments=assignment)

# Print results
printer(result)
```

---

## 👥 Authors

Developed for the **Operations Research** course:

- [Faiderasp](https://github.com/Faiderasp)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
