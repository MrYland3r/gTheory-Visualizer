import networkx as nx 
import matplotlib.pyplot as plt 

class GraphOperations:
    def create_and_draw_graph(self, nodes, edges):
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        nx.draw(G, with_labels=True)
        plt.show()
