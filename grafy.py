import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (перехресть)
G.add_nodes_from(["Перехрестя 1", "Перехрестя 2", "Перехрестя 3", "Перехрестя 4", "Перехрестя 5", "Перехрестя 6", "Перехрестя 7", "Перехрестя 8", "Перехрестя 9", "Перехрестя 10"])

# Додавання ребер (вулиць) і встановлення їх ваг
G.add_edge("Перехрестя 1", "Перехрестя 2", weight=5)
G.add_edge("Перехрестя 1", "Перехрестя 3", weight=3)
G.add_edge("Перехрестя 2", "Перехрестя 3", weight=2)
G.add_edge("Перехрестя 2", "Перехрестя 4", weight=7)
G.add_edge("Перехрестя 3", "Перехрестя 4", weight=4)

# Додавання ще ребер і їх ваг
G.add_edge("Перехрестя 4", "Перехрестя 5", weight=6)
G.add_edge("Перехрестя 5", "Перехрестя 6", weight=4)
G.add_edge("Перехрестя 4", "Перехрестя 7", weight=3)
G.add_edge("Перехрестя 7", "Перехрестя 8", weight=5)
G.add_edge("Перехрестя 6", "Перехрестя 8", weight=2)
G.add_edge("Перехрестя 7", "Перехрестя 9", weight=4)
G.add_edge("Перехрестя 8", "Перехрестя 9", weight=6)
G.add_edge("Перехрестя 9", "Перехрестя 10", weight=3)

# Візуалізація графа
pos = nx.spring_layout(G)  # Визначення позицій вузлів для кращого відображення
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
