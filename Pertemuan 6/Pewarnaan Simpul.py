import networkx as nx
import matplotlib.pyplot as plt

def welch_powell_coloring(G):
    # Urutkan simpul berdasarkan derajat secara menurun
    sorted_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)
    colors = {}
    current_color = 0

    for node, _ in sorted_nodes:
        if node not in colors:
            colors[node] = current_color
            for other_node, _ in sorted_nodes:
                if other_node not in colors:
                    if all(colors.get(neigh) != current_color for neigh in G.neighbors(other_node)):
                        colors[other_node] = current_color
            current_color += 1

    return colors

G = nx.Graph()
edges = [
    ('v1', 'v2'), ('v1', 'v3'), ('v1', 'v4'), ('v1', 'v5'), ('v1', 'v6'),
    ('v2', 'v3'), ('v2', 'v6'), ('v2', 'v7'),
    ('v3', 'v4'),
    ('v4', 'v5'),
    ('v5', 'v6'),
    ('v6', 'v7')
]
G.add_edges_from(edges)

coloring = welch_powell_coloring(G)

color_map = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']
node_colors = [color_map[coloring[node]] for node in G.nodes()]

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color=node_colors, node_size=1000, font_color='white')
plt.title(f"Pewarnaan Graf dengan Algoritma Welch-Powell\nJumlah Warna: {max(coloring.values()) + 1}")
plt.show()