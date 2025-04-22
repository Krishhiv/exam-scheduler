import networkx as nx
import matplotlib.pyplot as plt

def visualise(graph):
    G = nx.Graph(graph)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")

    plt.title("Graph: Course vs Conflicting Courses")
    plt.show()
