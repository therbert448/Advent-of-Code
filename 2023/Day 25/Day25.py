"""
Advent of Code
2023 Day 25

@author: Tom Herbert
"""

import networkx as nx

day = 25

def open_file(day):
    #filename = "test.txt"
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip() for line in file.readlines()]
    return inputs

def find_links(inputs):
    graph = nx.Graph()
    for line in inputs:
        start, ends = line.split(": ")
        ends = ends.split(" ")
        for end in ends:
            graph.add_edge(start, end)
    return graph

def part_one():
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    one, two = nx.connected_components(graph)
    print(f"Part One = {len(one) * len(two)}")

inputs = open_file(day)
graph = find_links(inputs)

part_one()