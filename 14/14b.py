import re
import sys
import math
from collections import defaultdict


def produce_chemical(recipes, having, chemical, quantity):
    if chemical == "ORE":
        return quantity, quantity

    recipe = recipes[chemical]
    inputs, output = recipe[:-1], recipe[-1]
    reactions = math.ceil(quantity / output[1])
    total_cost = 0

    for in_chemical, in_quantity in inputs:
        needed_amount = in_quantity * reactions

        if having[in_chemical] < needed_amount:
            need_to_produce = needed_amount - having[in_chemical]
            cost, produced_quantity = produce_chemical(
                recipes, having, in_chemical, need_to_produce)
            total_cost += cost
            having[in_chemical] += produced_quantity

        having[in_chemical] -= needed_amount

    return total_cost, reactions * output[1]


def find_fuel_cost(reactions):
    recipes = dict()

    for reaction in reactions:
        recipes[reaction[-1][0]] = reaction

    cost, produced = produce_chemical(recipes, defaultdict(int), "FUEL", 1)
    return cost


def produce_while_can(reactions):
    recipes = dict()

    for reaction in reactions:
        recipes[reaction[-1][0]] = reaction

    ores = 1000000000000
    fuel_cost = find_fuel_cost(reactions)
    fuel_lower_bound = math.floor(ores / fuel_cost)
    fuel_upper_bound = 2 * fuel_lower_bound

    beg, end = fuel_lower_bound, fuel_upper_bound
    while beg <= end:
        mid = (beg + end) // 2
        cost, _ = produce_chemical(recipes, defaultdict(int), "FUEL", mid)

        if cost == ores:
            return mid
        elif cost < ores:
            beg = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == "__main__":
    reactions = []

    for line in sys.stdin:
        line = line.rstrip()
        quantities = list(map(int, re.findall("\d+", line)))
        chemicals = re.findall("[A-Z]+", line)

        tuples = list(zip(chemicals, quantities))
        reactions.append(tuples)

    print(produce_while_can(reactions))
