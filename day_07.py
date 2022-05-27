"""
Advent of Code 2020 - Puzzel 7
https://adventofcode.com/2020/day/7
jshiles
"""

import networkx as nx
import re
from typing import List
from adventofcode import utils


def input_to_graph(filename: str) -> nx.DiGraph:
    """
    Parse rulesets into a networkx graph.
    """
    G = nx.DiGraph()

    with open(filename) as f:
        for rule in f.readlines():
            bag, contains = rule.strip().split(" bags contain ")
            G.add_node(bag)  # add our bag as node.
            for content in contains.split(", "):
                m = re.search(r"^(\d+)\s([\w\s]+)\sbag", content)
                if m:
                    G.add_edge(m.group(2), bag, weight=int(m.group(1)))
    return G


def total_bags(G: nx.DiGraph, bag: str = "shiny gold") -> int:
    """
    Recursively count the bags contained in bag.
    """

    def _total_bags_recrusive(G: nx.DiGraph, node: str = "shiny gold") -> int:
        if len(list(G.neighbors(node))) == 0:
            return 1
        else:
            cost = 1
            for neighbor in G.neighbors(node):
                cost += G.get_edge_data(node, neighbor).get(
                    "weight", 0
                ) * _total_bags_recrusive(G, neighbor)
            return cost

    return _total_bags_recrusive(G.reverse(), bag) - 1


def main():
    """
    execute part 1 and part 2
    """

    filename: str = utils.input_location(day="7")

    # How many bag colors can eventually contain at least one shiny gold bag?
    test_filename: str = utils.test_input_location(day="7", filename="test_input1.txt")
    test_G = input_to_graph(test_filename)
    test_bags_containing_sg = len(nx.shortest_path(test_G, "shiny gold").keys()) - 1
    assert test_bags_containing_sg == 4

    G = input_to_graph(filename)
    bags_containing_sg = len(nx.shortest_path(G, "shiny gold").keys()) - 1
    print(f"Part 1: {bags_containing_sg}.")

    # How many individual bags are required inside your single shiny gold bag?
    assert total_bags(test_G, "shiny gold") == 32

    test_filename: str = utils.test_input_location(day="7", filename="test_input2.txt")
    test_G = input_to_graph(test_filename)
    total_bags(test_G, "shiny gold") == 126

    print(f"Part 2: {total_bags(G, 'shiny gold')}.")


if __name__ == "__main__":
    main()
