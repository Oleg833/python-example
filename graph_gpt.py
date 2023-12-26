import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

# Задаємо послідовність подій в проекті
events = ["0", "1", "2", "3", "4", "5", "6",
          "7", "8", "9"]
# Задаємо послідовність подій в проекті
events1 = ["Start", "Task1", "Task2", "Task3", "Task4",
           "Task5", "Task6", "Task7", "Task8", "End"]

# Задаємо тривалості кожного завдання
durations1 = {"Start": 0, "Task1": 3, "Task2": 4, "Task3": 1, "Task4": 2,
              "Task5": 4, "Task6": 7, "Task7": 3, "Task8": 2, "End": 0}
# Задаємо тривалості кожного завдання
durations = {"0": 0, "1": 3, "2": 4, "3": 1, "4": 2,
             "5": 4, "6": 7, "7": 3, "8": 2, "9": 0}
# Задаємо залежності між подіями (ребра графа)
edges1 = [("Start", "Task1"), ("Start", "Task2"), ("Task1", "Task3"),
          ("Task2", "Task3"), ("Task3", "Task4"), ("Task3", "Task5"),
          ("Task4", "Task6"), ("Task5", "Task6"), ("Task6", "Task7"),
          ("Task7", "Task8"), ("Task8", "End")]
# Задаємо залежності між подіями (ребра графа)
dependencies = [("0", "1"), ("0", "2"), ("1", "3"),
         ("2", "3"), ("1", "4"), ("2", "4"),
         ("3", "4"), ("2", "5"), ("3", "5"),
         ("4", "5"), ("5", "6"), ("3", "6"),
         ("6", "7"), ("7", "8"), ("8", "9")]
dependencies2 = [('start', 'task1'), (' end', 'task1'), ('2', 'hgfh'), ('3', 'hgfh'), ('4', 'hgfh'), ('4', 'res'), ('7', 'res'), ('1', 'res')]

# Створюємо граф
# Create graph
G = nx.DiGraph()
G.add_edges_from(dependencies)

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700,node_color='skyblue', font_size=8)
plt.show()

# Calculate early and late start times
early_start = {event: 0 for event in events}
late_start = {event: 0 for event in events}

for event in nx.topological_sort(G):
    early_start[event] = max([early_start[predecessor] + durations[predecessor] for predecessor in G.predecessors(event)], default=0)

end_value = max(early_start.values())
for event in nx.topological_sort(G, reverse=True):
    successors = list(G.successors(event))
    if successors:
        late_start[event] = min([late_start[successor] - durations[event] for successor in successors], default=end_value)

# Find critical path
critical_path = [event for event in events if early_start[event] == late_start[event] and G.out_degree(event) > 0]

# Draw graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700,node_color='skyblue', font_size=8)

# Highlight critical path
nx.draw_networkx_nodes(G, pos, nodelist=critical_path, node_color='red', node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=[(critical_path[i-1], critical_path[i]) for i in range(1, len(critical_path))], edge_color='red', width=2)

# Display the graph
# plt.show()

# Створюємо матрицю суміжності
adjacency_matrix = nx.adjacency_matrix(G).todense()
print("Матриця суміжності:")
print(adjacency_matrix)

