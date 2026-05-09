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

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
