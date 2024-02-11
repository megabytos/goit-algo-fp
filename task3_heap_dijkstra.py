import heapq
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    plt.figure(figsize=(8, 8))
    G = nx.Graph()
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            G.add_edge(vertex, neighbor, weight=weight)
  
    pos = nx.spring_layout(G, seed=23)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=14, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    routes = {vertex: [] for vertex in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                routes[neighbor] = routes[current_vertex] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    return distances, routes


if __name__ == "__main__":

    sample_graph = {
        "A": {"B": 3, "C": 2, "D": 4, "E": 1},
        "B": {"A": 3, "C": 1, "F": 2},
        "C": {"A": 2, "B": 1, "D": 2, "F": 3},
        "D": {"A": 4, "C": 2, "E": 3, "G": 2},
        "E": {"A": 1, "D": 3, "H": 2},
        "F": {"B": 2, "C": 3, "G": 1, "I": 3},
        "G": {"D": 2, "F": 1, "H": 3, "I": 2},
        "H": {"E": 2, "G": 3, "I": 1, "J": 2},
        "I": {"F": 3, "G": 2, "H": 1, "J": 3},
        "J": {"H": 2, "I": 3},
    }

    start_vertex = "A"

    shortest_distances, shortest_routes = dijkstra(sample_graph, start_vertex)

    print("Shortest distances from ", start_vertex)
    for v, dist in shortest_distances.items():
        if v != start_vertex:
            print(f"to {v}: {dist} {shortest_routes[v]}")

    draw_graph(sample_graph)
