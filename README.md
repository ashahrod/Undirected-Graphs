# Undirected Graphs: Bridge Identification

## Project Overview

This project revolves around the exploration of undirected graphs, providing algorithms to identify critical bridges that, if removed, would disconnect the graph. Additionally, the project includes a mathematical characterization of these bridges.

## Bridge Identification Algorithm

### Part 1: Bridges
Consider a graph where vertices represent cities, and edges represent highways between cities. The goal is to find bridges, i.e., edges whose removal would disconnect the graph. The algorithm must have a complexity of O(|E|²). Observations and constraints are provided to guide the algorithm's design.

For example, given the edge list:
- 0, 1
- 1, 2
- 2, 0
- 1, 3
- 3, 4
- 4, 5
- 5, 3

The program should output:
```bash
Contains 1 bridge(s):
1, 3
```
## Part 2: Mathematical Characterization

A fundamental theorem is introduced and proven: An edge, denoted as e, is considered a bridge if and only if there exist no cycles traversing e in the connected graph G.

## Implementation Details

To bring the theoretical understanding into practice, the bridge identification algorithm is implemented. The program accepts a file containing an edge list as input and print the identified bridges to stdout following the specified format.

## Usage Example

```bash
$ ./compile.sh
$ ./run.sh input.txt
