from queue import PriorityQueue
from misc import PathInfo, h, calc_path_distance, calc_path_energy, load_json_files
from timeit import default_timer as timer

def astar(source: str, dest: str, budget: int, coord: dict, cost: dict, dist: dict, g: dict, gamma: float =1) -> PathInfo:
    prio_queue = PriorityQueue()

    # priority queue item is a such: ( $energy_used: int, $path_taken: list )
    prio_queue.put((0, (0, [source])))

    # nodes to not revisit accidentally
    visited = set()

    while not prio_queue.empty():
        pair = prio_queue.get()

        energy_used, current_path = pair[1]

        # current node will be the last node in the path taken
        current_node = current_path[-1]

        # return path taken if node is the destination
        if current_node == dest:
            path_info = PathInfo()
            path_info.path = "->".join(current_path)
            path_info.dist = calc_path_distance(current_path, dist)
            path_info.energy = calc_path_energy(current_path, cost)
            return path_info

        # add paths for neighbouring nodes into the priority queue
        for neighbour in g[current_node]:
            # prevent same edge from being taken
            if (current_node, neighbour) not in visited:
                visited.add((current_node, neighbour))
                visited.add((neighbour, current_node))

                new_energy = energy_used + cost[f"{current_node},{neighbour}"]

                # take new path if energy cost is within budget
                if new_energy <= budget:
                    path_dist = pair[0] + dist[f"{current_node},{neighbour}"]
                    h_dist = h(neighbour, dest, coord) * gamma
                    score = path_dist + h_dist

                    new_path = current_path.copy()
                    new_path.append(neighbour)

                    prio_queue.put((score, (new_energy, new_path)))


coord, cost, dist, g = load_json_files()
energyBudget = 287932

#track computational time for search algorithm
start_time = timer()
path = astar('1', '50', energyBudget,coord, cost, dist, g)
end_time = timer()

print("time taken for A* algorithm: ", end_time- start_time)

shortestPath = "S" + path.path[(1):path.path.index("50")] + "T"
print(f"Shortest path: {path.path}")
print(f"Shortest path: {shortestPath}")
print(f"Shortest distance: {path.dist}")
print(f"Total energy cost: {path.energy}\n")

