# The Torchbearer

**Student Name:** Jonathan Nguyen
**Student ID:** 131671537
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _A single shortest-path run from S only tells the cheapest cost from S to each location, and therefore cannot decide the optimal order in which to visit the relic chambers._

- **What decision remains after all inter-location costs are known:**
  _After all inter-location costs are known, the order of relic chambers to traverse in between S and T._

- **Why this requires a search over orders (one sentence):**
  _This requires a search over orders because the total route cost depends on how the relic visits are ordered, not just on each individual cheapest path._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source                                                                 |
|------------------|------------------------------------------------------------------------------------|
| _S_              | _Needed to compute shortest paths from the starting point to every relic chamber._ |
| _R_              | _Needed to compute shortest paths between all pairs of relic chambers._            |
| _T_              | _Included to compute shortest paths from relic chambers to final destination._     |

### Part 2b: Distance Storage


| Property | Your answer                            |
|---|----------------------------------------|
| Data structure name | Hash Map                               |
| What the keys represent | Ordered pairs of nodes (u, v)          |
| What the values represent | Shortest-path distance from u to v     |
| Lookup time complexity | O(1)                                   |
| Why O(1) lookup is possible | Hashing allows direct indexing of keys |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** _k + 2_
- **Cost per run:** _O(m * log n)_
- **Total complexity:** _O(k * m * log n)_
- **Justification (one line):** _Dijkstra is run once from each source: S, each of the relics, and T, and each run costs O(m * log n)._

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  _If a node, v, is in S, dist[v] is the true shortest-path distance from the source._

- **For nodes not yet finalized (not in S):**
  _If a node, u, is not in S, dist[u] is the current shortest-path distance discovered from the source._

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  _Before iteration 1, the only vertex finalized in S is the source node, x, with a distance of 0. This holds true globally, so the invariant holds true through initialization._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Finalizing the min-dist node is always correct because any other alternative path through another node cannot produce a shorter path. This is held true by the fact that all edge weights are nonnegative because if some alternative path through another node is the same length as the min-dist, traveling along an extra edge cannot make the path shorter._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees that when the algorithm ends, S holds the true shortest-path distance for every reachable node._

### Part 3c: Why This Matters for the Route Planner


_This matters for the route planner because having incorrect distances can affect the routing decisions and produce a sub-optimal route._

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** _Greedy fails in the case that choosing the nearest relic can ignore a shorter overall route later._
- **Counter-example setup:**

| From \ To | B  | C   | D   | T  |
|-----------|----|-----|-----|----|
| S         | 1  | 2   | 2   | -- |
| B         | -- | 100 | 100 | 1  |
| C         | 1  | --  | 1   | 1  |
| D         | 1  | --  | --  | 1  |

- **What greedy picks:** _Greedy chooses B from S first because it is the closest relic._
- **What optimal picks:** _Optimal chooses C first._
- **Why greedy loses:** _Greedy loses because although B is the locally optimal choice, traversing from B to other nodes is extremely expensive. Optimal chooses C and has access to the cheapest overall path._

### What the Algorithm Must Explore


- _The algorithm must explore different relic visit order choices because the cheapest overall route depends on the order, not just the length of the paths._

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component                | Variable name in code | Data type | Description                                                                       |
|--------------------------|-----------------------|-----------|-----------------------------------------------------------------------------------|
| Current location         | current_loc           | string    | A string variable that keep tracks of the current node being processed.           |
| Relics already collected | S                     | set       | A set of relics already collected to ensure nodes aren't collected more than once |
| Fuel cost so far         | cost_so_far           | int       | An integer variable to keep track of the fuel used so far.                        |

### Part 5b: Data Structure for Visited Relics


| Property                                    | Your answer                                                                    |
|---------------------------------------------|--------------------------------------------------------------------------------|
| Data structure chosen                       | set                                                                            |
| Operation: check if relic already collected | Time complexity: O(1)                                                          |
| Operation: mark a relic as collected        | Time complexity: O(1)                                                          |
| Operation: unmark a relic (backtrack)       | Time complexity: O(1)                                                          |
| Why this structure fits                     | This structure fits because it executes necessary operations in constant time. |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** _The worst case is k!._
- **Why:** _k! is the worst case because the algorithm may need to consider every possible ordering of k relics._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
