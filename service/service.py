from OTTools import TransportationProblem
from models.Model import DataProblem
from typing import List


def s_MODI(Data: DataProblem):

    Problem = TransportationProblem(
        Data.costs,
        Data.demand,
        Data.offer
    )
    result = Problem.solve("MODI")

    return result


    