import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(nodes_list):
    tree_root = Node(nodes_list[0])
    nodes = [tree_root]

    for i in range(len(nodes_list)):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        if left_child_idx < len(nodes_list):
            nodes[i].left = Node(nodes_list[left_child_idx])
            nodes.append(nodes[i].left)
        if right_child_idx < len(nodes_list):
            nodes[i].right = Node(nodes_list[right_child_idx])
            nodes.append(nodes[i].right)

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=1400, font_size=14, node_color=colors)
    plt.show()


if __name__ == "__main__":
    heap = [2,55,12,4,36,8,7,45,27,11,5,17,31]

    heapq.heapify(heap)

    draw_tree(heap)
