from OTTools import TransportationProblem
from models.Model import DataProblem
from typing import List


def s_MODI(Data: DataProblem):
    
    Problem = TransportationProblem(
        cost_matrix=Data.costs,
        supply=Data.offer,
        demand=Data.demand
    )
    result = Problem.solve("MODI")

    return result


    