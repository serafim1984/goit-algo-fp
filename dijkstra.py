import heapq
import math

def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Example usage
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node", start_node)
for node, distance in shortest_paths.items():
    print(f"To node {node}: {distance}")