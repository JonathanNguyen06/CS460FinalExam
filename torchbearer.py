"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Jonathan Nguyen
Student ID:   131671537

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    return """
    A single shortest-path run from S only tells the cheapest cost from S to each location, and therefore cannot decide the optimal order in which to visit the relic chambers. 
    After all inter-location costs are known, the order of relic chambers to traverse in between S and T. 
    This requires a search over orders because the total route cost depends on how the relic visits are ordered, not just on each individual cheapest path.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.
    """
    sources = []
    seen = set()

    # Prevent duplicate nodes
    for node in [spawn] + relics + [exit_node]:
        if node not in seen:
            sources.append(node)
            seen.add(node)

    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    """
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Prevent suboptimal distances from being pushed
        if current_dist > distances[current_node]:
            continue

        for neighbor, cost in graph[current_node]:
            new_dist = current_dist + cost

            # If current distance is shorter than stored distance, replace
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.
    """
    sources = select_sources(spawn, relics, exit_node)

    dist_table = {}

    # Run dijkstra from each source
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    """
    return ("If a node, v, is in S, dist[v] is the true shortest-path distance from the source. "
            "If a node, u, is not in S, dist[u] is the current shortest-path distance discovered from the source."
            "Before iteration 1, the only vertex finalized in S is the source node, x, with a distance of 0. "
            "This holds true globally, so the invariant holds true through initialization."
            "Finalizing the min-dist node is always correct because any other alternative path through another node "
            "cannot produce a shorter path. This is held true by the fact that all edge weights are nonnegative because "
            "if some alternative path through another node is the same length as the min-dist, traveling along an extra "
            "edge cannot make the path shorter."
            "The invariant guarantees that when the algorithm ends, S holds the true shortest-path distance for every reachable node."
            "This matters for the route planner because having incorrect distances can affect the routing decisions and produce a sub-optimal route.")


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    """
    return ("Greedy fails in the case that choosing the nearest relic can ignore a shorter overall route later."
            "S --> B = 1, S --> C = 2, S --> D = 2"
            "B --> C = 100, B --> D = 100"
            "C --> D = 1, C --> B = 1, C --> T = 1"
            "D --> B = 1, D --> T = 1"
            "Greedy chooses B from S first because it is the closest relic."
            "Optimal chooses C first."
            "Greedy loses because although B is the locally optimal choice, traversing from B to other nodes is "
            "extremely expensive. Optimal chooses C and has access to the cheapest overall path."
            "The algorithm must explore different relic visit order choices because the cheapest overall route "
            "depends on the order, not just the length of the paths.")


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    relics_remaining = set(relics)
    relics_visited_order = []

    best = [float('inf'), []]

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        0,
        exit_node,
        best
    )

    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    def lower_bound_remaining(dist_table, current_loc, relics_remaining, exit_node):
        if len(relics_remaining) == 0:
            return dist_table[current_loc].get(exit_node, float('inf'))

        cheapest_next = min(
            dist_table[current_loc].get(relic, float('inf'))
            for relic in relics_remaining
        )

        cheapest_exit = min(
            dist_table[relic].get(exit_node, float('inf'))
            for relic in relics_remaining
        )

        return cheapest_next + cheapest_exit

    lower_bound = lower_bound_remaining(
        dist_table,
        current_loc,
        relics_remaining,
        exit_node
    )

    # Pruning: if this partial route already costs at least as much as the
    # best complete route found so far, adding more nonnegative edge costs
    # cannot make it better. Therefore, this branch cannot contain the optimal route.
    if cost_so_far + lower_bound >= best[0]:
        return

    # Base case
    if len(relics_remaining) == 0:
        exit_cost = dist_table[current_loc].get(exit_node, float('inf'))

        if exit_cost == float('inf'):
            return

        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return

    # Recursive case
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc].get(relic, float('inf'))

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

        # Backtracking
        relics_visited_order.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
