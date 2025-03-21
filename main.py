import tkinter as tk 
from gui import GraphVisualizerGUI

def main():
    root = tk.Tk()
    root.title('gTheory Visualizer')
    gui = GraphVisualizerGUI(root)
    gui.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
