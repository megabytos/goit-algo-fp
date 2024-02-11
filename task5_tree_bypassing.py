import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

color_map = [
    "003AC6",
    "0045CA",
    "004FCE",
    "005AD2",
    "0064D6",
    "006EDA",
    "0079DE",
    "0083E3",
    "008EE7",
    "0098EB",
    "00A2EF",
    "00ADF3",
    "00B7F7",
    "00C2FB",
    "00CCFF",
]


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def insert_node(node, key):
    if node is None:
        return Node(key)
    if key < node.val:
        node.left = insert_node(node.left, key)
    elif key > node.val:
        node.right = insert_node(node.right, key)
    return node


def add_edges(graph, node, position, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            position[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, position, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            position[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, position, x=r, y=y - 1, layer=layer + 1)
    return graph


def set_graph(graph, position, axis, title=None):
    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}
    nx.draw(
        graph,
        pos=position,
        labels=labels,
        ax=axis,
        arrows=False,
        node_size=1000,
        node_color=colors,
    )
    axis.set_title(title)


def bfs_iterative(graph, start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            color_value = len(visited)
            graph.nodes[node.id]["color"] = "#" + color_map[color_value]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node.id not in visited:
            color_value = len(visited)
            graph.nodes[node.id]["color"] = "#" + color_map[color_value]
            visited.add(node.id)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


if __name__ == "__main__":
    sample_list = [55, 12, 4, 36, 8, 7, 45, 27, 11, 5, 17, 31, 2, 15]
    root = Node(sample_list[0])
    for num in sample_list[1:]:
        root = insert_node(root, num)

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    g = nx.DiGraph()
    pos = {root.id: (0, 0)}
    g = add_edges(g, root, pos)

    bfs_iterative(g, root)
    set_graph(g, pos, ax[0], title="BFS bypassing")

    dfs_iterative(g, root)
    set_graph(g, pos, ax[1], title="DFS bypassing")

    plt.show()
