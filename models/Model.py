from typing import List
from dataclasses import dataclass, field
import numpy as np
from numpy.typing import NDArray

@dataclass
class DataProblem:
    costs: List[List[int]] | None = field(default_factory=list)
    offer: NDArray[np.int_] | None = None
    demand: NDArray[np.int_] | None = None


@dataclass
class TotalCost:
    costs: List[List[int]] | None = field(default_factory=list)
    assignments: List[List[int]] | None = field(default_factory=list)