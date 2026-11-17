# MODI Method - Software Implementation

Implementación en Python para la resolución y optimización de problemas de transporte en Programación Lineal utilizando el **Método MODI (Modified Distribution Method)** o **Método U-V**.

---

## 📌 Acerca del Proyecto

Este proyecto forma parte de la asignatura de **Investigación de Operaciones** y tiene como objetivo resolver problemas de optimización de transporte, encontrando la distribución óptima que minimice el costo total de envío satisfaciendo las restricciones de oferta y demanda.

El software está diseñado con una arquitectura modular basada en capas (controlador, modelo, servicio e interfaz auxiliar de logging).

---

## 🧠 ¿Qué es el Método MODI?

El **Método MODI** (también conocido como Método de Distribución Modificada o Método U-V) permite verificar si una solución factible inicial de un problema de transporte es óptima:

1. **Cálculo de Potenciales:** Asigna valores $u_i$ (para filas/orígenes) y $v_j$ (para columnas/destinos) tales que $u_i + v_j = c_{ij}$ para las celdas básicas (ocupadas).
2. **Evaluación de Costos Marginales:** Calcula el costo de oportunidad $\Delta_{ij} = c_{ij} - (u_i + v_j)$ para las celdas no básicas.
3. **Prueba de Optimalidad:** Si todos los $\Delta_{ij} \ge 0$, la solución actual es óptima. Si existe algún valor negativo, se introduce la celda más negativa al circuito de reasignación ($\theta$) hasta alcanzar el costo mínimo.

---

## 📁 Estructura del Proyecto

```text
MODI Method - Software Implementation/
│
├── controller/
│   ├── __init__.py
│   └── controller.py       # Controlador principal: orquesta la resolución y calcula costos totales
│
├── models/
│   └── Model.py            # Modelos de datos (DataProblem, TotalCost) con dataclasses
│
├── service/
│   ├── __init__.py
│   └── service.py          # Lógica del servicio MODI utilizando OTTools
│
├── interface/
│   └── helpers.py          # Helpers auxiliares para logging formateado y salidas
│
├── tests/                  # Directorio para pruebas unitarias
├── app.py                  # Script principal de entrada y ejecución
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación
```

---

## 🛠️ Tecnologías y Librerías

- **[Python](https://www.python.org/)** (v3.10+) – Lenguaje base del proyecto.
- **[NumPy](https://numpy.org/)** – Manejo de matrices y operaciones numéricas vectorizadas.
- **[OTTools](https://pypi.org/project/OTTools/)** – Herramienta especializada para problemas de transporte e investigación de operaciones.

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Faiderasp/MODI-Method---Software-Implementation.git
cd "MODI Method - Software Implementation"
```

### 2. Crear y activar un entorno virtual

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

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el proyecto

```bash
python app.py
```

---

## 💻 Ejemplo de Uso

En `app.py` se define un problema de transporte con la matriz de costos, oferta y demanda:

```python
from controller.controller import c_MODI
from interface.helpers import printer

# Matriz de costos unitarios de transporte
costs = [
    [4, 8, 8],
    [2, 5, 7],
    [6, 4, 3]
]

# Oferta de cada origen
offer = [20, 30, 25]

# Demanda de cada destino
demand = [10, 35, 30]

# Solución básica asignada inicial (opcional para cálculo de costo actual)
assignment = [
    [10, 5, 5],
    [0, 30, 0],
    [0, 0, 25]
]

# Ejecutar el controlador MODI
result = c_MODI(p_costs=costs, p_demand=demand, p_offer=offer, p_assignments=assignment)

# Imprimir resultado
printer(result)
```

### Salida esperada:

```json
{
  "Total Cost": 345,
  "Solution": [
    [10.0,  0.0,  0.0],
    [10.0, 25.0,  0.0],
    [ 0.0,  5.0, 25.0]
  ]
}
```

---

## 👥 Autores

Desarrollado para el curso de **Investigación de Operaciones**:

- [Faiderasp](https://github.com/Faiderasp)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
