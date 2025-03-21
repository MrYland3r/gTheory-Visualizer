import tkinter as tk 
from graph_operations import GraphOperations 

class GraphVisualizerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(bg="#2f2f2f")
        self.pack(pady=20, padx=10, fill="both", expand=True)
        self.create_widgets()
        self.graph_ops = GraphOperations()

    def create_widgets(self):
        self.node_label = tk.Label(self, text="Enter nodes (comma-separated):", bg="#2f2f2f", fg="white")
        self.node_label.pack(side=tk.LEFT, padx=10)
        self.node_entry = tk.Entry(self, bg="#4f4f4f", fg="white")
        self.node_entry.pack(side=tk.LEFT, padx=10)

        self.edge_label = tk.Label(self, text="Enter edges (node1-node2, comma-separated):", bg="#2f2f2f", fg="white")  
        self.edge_label.pack(side=tk.LEFT, padx=10)
        self.edge_entry = tk.Entry(self, bg="#4f4f4f", fg="white")
        self.edge_entry.pack(side=tk.LEFT, padx=10)

        self.visualize_button = tk.Button(self, text="Visualizer", command = self.visualize_graph, bg="#4f4f4f", fg="white")
        self.visualize_button.pack(side=tk.LEFT, padx=10)

    def visualize_graph(self):
        nodes = self.node_entry.get().split(',')
        nodes = [node.strip() for node in nodes if node.strip()]

        edges = self.edge_entry.get().split(',')
        edges = [(edge.split('-')[0].strip(), edge.split('-')[1].strip()) for edge in edges if '-' in edge]
        
        self.graph_ops.create_and_draw_graph(nodes, edges)
