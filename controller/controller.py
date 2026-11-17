from numpy.typing import NDArray
import numpy as np
from models.Model import DataProblem
from interface.helpers import *
from typing import List
from service.service import s_MODI

def c_MODI(
        p_costs: List[List[int]],
        p_offer: List[int],
        p_demand: List[int],
        p_assignments: List[List[int]]
    ):

    try:
        array_offer = np.array(p_offer)
        array_demand = np.array(p_demand)

        Problem = DataProblem(
            costs=p_costs,
            offer=array_offer,
            demand=array_demand
        )

        result = {
            "Total Cost": total_cost(cost=p_costs, assignments=p_assignments),
            "Solution": s_MODI(Problem)
        }
        
        return result
    
    except Exception as e:

        h_error(f"Something went wrong: {e}")


def total_cost(
        cost: List[List[int]], 
        assignments: List[List[int]]
    ):
    
    return sum(
        cost[i][j] * assignments[i][j]
        for i in range(len(cost))
        for j in range(len(cost[0]))
    )