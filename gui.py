import tkinter as tk 
from graph_operations import GraphOperations 

class GraphVisualizerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.graph_ops = GraphOperations()

    def create_widgets(self):
        tk.Label(self, text="Enter nodes (comma-separated):").pack(side=tk.LEFT)
        self.node_entry = tk.Entry(self)
        self.node_entry.pack(side=tk.LEFT)

        tk.Label(self, text="Enter edges (node1-node2, comma-separated):").pack(side=tk.LEFT)
        self.edge_entry = tk.Entry(self)
        self.edge_entry.pack(side=tk.LEFT)

        tk.Button(self, text="Visualizer", command = self.visualize_graph).pack(side=tk.LEFT)

    def visualize_graph(self):
        nodes = self.node_entry.get().split(',')
        nodes = [node.strip() for node in nodes if node.strip()]

        edges = self.edge_entry.get().split(',')
        edges = [(edge.split('-')[0].strip(), edge.split('-')[1].strip()) for edge in edges if '-' in edge]
        
        self.graph_ops.create_and_draw_graph(nodes, edges)
