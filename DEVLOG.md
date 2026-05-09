# Development Log – The Torchbearer

**Student Name:** Jonathan Nguyen
**Student ID:** 131671537


---

## Entry 1 – [5/5/26]: Initial Plan

_I will first implement Dijkstra's algorithm to find the shortest path from each relevant source node, and store the distances in a dictionary. Then, I will implement the order-search step
to try possible relic orders and compute the total route cost. I expect it to be difficult to handle directed
edges and cases where there are unreachable paths. I plan to test with small graphs where I can quickly 
and manually verify the best route._

---

## Entry 2 – [5/8/26]: Find Optimal Path and Explore

_I've implemented the 'find_optimal_route' and 'explore' functions. The solution is a recursive backtracking 
search over all possible relic visit orders. The state tracks current location, remaining relics, the order
of visited relics, and the cost so far. The remaining relics are stored in a set for constant time operations.
Added a pruning condition that stops exploring a branch if its cost is greater than or equal to the best stored
route so far. I realized during development that 'relics_visiited_order' would update during backtracking,
so I had to store a copy of it when updating the best solution._

---

## Entry 3 – [5/9]: Lower Bound Pruning

_Improved 'explore' by adding a lower-bound pruning check. The earlier version only pruned when the cost so far
was already greater than or equal to the best complete solution. I added a helper function to estimate a safer
lower bound using the cheapest possible move._

---

## Entry 4 – [5/9]: Post-Implementation Reflection


_There isn't anything in particular I would improve with my code besides checking specific edge cases. While
more common edge cases like unreachable nodes are addressed in my code, there may be certain cases, like duplicate
nodes or nodes that only appear as neighbors instead of keys, that aren't addressed in my code._

---

## Final Entry – [5/9]: Time Estimate


| Part                           | Estimated Hours |
|--------------------------------|-----------------|
| Part 1: Problem Analysis       | 0.5             |
| Part 2: Precomputation Design  | 1               |
| Part 3: Algorithm Correctness  | 0.5             |
| Part 4: Search Design          | 0.5             |
| Part 5: State and Search Space | 3               |
| Part 6: Pruning                | 1               |
| Part 7: Implementation         | 1               |
| README and DEVLOG writing      | 1.5             |
| **Total**                      | 9               |
