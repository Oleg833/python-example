import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt


class CPMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPM App")

        self.tasks = {}
        self.dependencies = []
# Задаємо послідовність подій в проекті
# events1 = ["Start", "Task1", "Task2", "Task3", "Task4", "Task5", "Task6", "Task7", "Task8", "End"]
# Задаємо тривалості кожного завдання
# durations1 = {"Start": 0, "Task1": 3, "Task2": 4, "Task3": 1, "Task4": 2, "Task5": 4, "Task6": 7, "Task7": 3, "Task8": 2, "End": 0}
# Задаємо залежності між подіями (ребра графа)
# dependencies = [("Start", "Task1"), ("Start", "Task2"), ("Task1", "Task3"), ("Task2", "Task3"), ("Task3", "Task4"), ("Task3", "Task5"), ("Task4", "Task6"), ("Task5", "Task6"), ("Task6", "Task7"),("Task7", "Task8"), ("Task8", "End")]
        # self.events = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # self.durations = {"0": 0, "1": 3, "2": 4, "3": 1,
        #                   "4": 2, "5": 4, "6": 7, "7": 3, "8": 2, "9": 0}
        # self.dependencies = [("0", "1"), ("0", "2"), ("1", "3"), ("2", "3"),
        #               ("1", "4"), ("2", "4"), ("3", "4"), ("2", "5"),
        #               ("3", "5"), ("4", "5"), ("5", "6"), ("3", "6"),
        #               ("6", "7"), ("7", "8"), ("8", "9")]
        self.create_widgets()

    def create_widgets(self):
        # Task Entry Frame
        task_frame = ttk.LabelFrame(self.root, text="Task Information")
        task_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Task Name
        ttk.Label(task_frame, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
        self.task_name_entry = ttk.Entry(task_frame)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Duration
        ttk.Label(task_frame, text="Duration:").grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = ttk.Entry(task_frame)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Dependency
        ttk.Label(task_frame, text="Dependency (comma-separated):").grid(row=2, column=0, padx=5, pady=5)
        self.dependency_entry = ttk.Entry(task_frame)
        self.dependency_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add Task Button
        add_task_button = ttk.Button(task_frame, text="Add Task", command=self.add_task)
        add_task_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Graph Frame
        graph_frame = ttk.LabelFrame(self.root, text="Graph")
        graph_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Create Graph Button
        create_graph_button = ttk.Button(graph_frame, text="Create Graph", command=self.create_graph)
        create_graph_button.pack(pady=10)

        # Canvas to display the graph
        self.canvas = tk.Canvas(graph_frame, bg="white", width=600, height=400)
        self.canvas.pack()

    def add_task(self):
        task_name = self.task_name_entry.get()
        duration = int(self.duration_entry.get())
        dependencies = self.dependency_entry.get().split(',')

        self.tasks[task_name] = {"duration": duration, "dependencies": dependencies}
        self.dependencies.extend([(dependency, task_name) for dependency in dependencies])
        print("self.dependencies = ", self.dependencies)
        # Clear entry fields
        self.task_name_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        self.dependency_entry.delete(0, 'end')

    def create_graph(self):
        G = nx.DiGraph()
        G.add_edges_from(self.dependencies)

        # Calculate critical path
        critical_path = nx.algorithms.critical_path(G)

        # Draw graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

        # Highlight critical path
        nx.draw_networkx_nodes(G, pos, nodelist=critical_path, node_color='red', node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=[(critical_path[i-1], critical_path[i]) for i in range(1, len(critical_path))], edge_color='red', width=2)

        # Display the graph
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = CPMApp(root)
    root.mainloop()
