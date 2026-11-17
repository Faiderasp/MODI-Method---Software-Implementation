from controller.controller import c_MODI
from interface.helpers import *

costs = [
    [4, 8, 8],
    [2, 5, 7],
    [6, 4, 3]
]

offer = [20, 30, 25]

demand = [10, 35, 30]

assignment = [
    [10, 5, 5],
    [0, 30, 0],
    [0, 0, 25]
]

result = c_MODI(p_costs=costs, p_demand=demand, p_offer=offer, p_assignments=assignment)

printer(result)