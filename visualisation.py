import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

def visualise(graph):
    # Create a graph object from the adjacency list (graph)
    G = nx.Graph(graph)

    # Draw the graph with node labels (course names)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)  # Layout algorithm for graph nodes

    # Draw the graph with specific properties (color, size, etc.)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", edge_color="gray")

    # Display the plot
    plt.title("Conflict Graph: Course vs Conflicting Courses")
    plt.show()
