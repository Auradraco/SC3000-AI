from queue import PriorityQueue
from misc import PathInfo, calc_path_distance

def ucs(source: str, dest: str, dist: dict, g: dict) -> PathInfo:
    prio_queue = PriorityQueue()

    # Priority queue item is such: ( $path_taken: list )
    prio_queue.put((0, [source]))

    # Nodes to not revisit accidentally
    visited = set()

    while not prio_queue.empty():
        pair = prio_queue.get()
        current_path = pair[1]

        # Current node will be the last node in the path taken
        current_node = current_path[-1]

        # Explore node if it hasn't already been visited
        if current_node not in visited:
            visited.add(current_node)

            # Return path taken if the node is the destination
            if current_node == dest:
                path_info = PathInfo()
                path_info.path = "->".join(current_path)
                path_info.dist = calc_path_distance(current_path, dist)
                path_info.energy = "Not Applicable"
                return path_info

            # Add paths for neighboring nodes into the priority queue
            for neighbor in g[current_node]:
                new_dist = dist[f"{current_node},{neighbor}"]
                score = pair[0] + new_dist

                new_path = list(pair[1])
                new_path.append(neighbor)

                prio_queue.put((score, new_path))

    return PathInfo()

coord, cost, dist, g = load_json_files()


path = ucs('1', '50', dist, g)
shortestPath = "S" + path.path[(1):path.path.index("50")] + "T"
print(f"Shortest path: {path.path}")
print(f"Shortest path: {shortestPath}") #shows source node as "S" and terminate state as "T" in path taken 
print(f"Shortest distance: {path.dist}")
print(f"Total energy cost: {path.energy}\n") #no energy constraint due to question nature
