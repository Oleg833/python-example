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
edges1 = [("Start 0", "Task1"), ("Start 0", "Task2"), ("Task1", "Task3"),
          ("Task2", "Task3"), ("Task3", "Task4"), ("Task3", "Task5"),
          ("Task4", "Task6"), ("Task5", "Task6"), ("Task6", "Task7"),
          ("Task7", "Task8"), ("Task8", "End")]
# Задаємо залежності між подіями (ребра графа)
edges = [("0", "1"), ("0", "2"), ("1", "3"),
         ("2", "3"), ("1", "4"), ("2", "4"),
         ("3", "4"), ("2", "5"), ("3", "5"),
         ("4", "5"), ("5", "6"), ("3", "6"),
         ("6", "7"), ("7", "8"), ("8", "9")]

# Створюємо граф
G = nx.DiGraph()
G.add_edges_from(edges)


# Виводимо граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700,
        node_color='skyblue', font_size=8)


# Створюємо матрицю суміжності
adjacency_matrix = nx.adjacency_matrix(G).todense()
print("Матриця суміжності:")
print(adjacency_matrix)

# Розраховуємо ранній та пізній початок для кожної події
early_start = nx.get_node_attributes(G, 'early_start')
late_start = nx.get_node_attributes(G, 'late_start')
print(f"early_start:{early_start} + late_start:{late_start}")

# Додаємо подію "Start" до словника early_start зі значенням 0
early_start["Start"] = 0

# Ініціалізуємо значення late_start для End як його ранній старт
# end_value = max(early_start.values())
# early_start["End"] = end_value
# late_start["End"] = end_value

# for event in nx.topological_sort(G):
#     early_start[event] = max([early_start[predecessor] + durations[predecessor]
#                              for predecessor in G.predecessors(event)], default=0)

#     successors = list(G.successors(event))
#     if successors:
#         late_start[event] = min([late_start.get(successor, end_value) - durations[event]
#                                 for successor in successors], default=early_start[event])

# Знаходимо критичний маршрут
# critical_path = [
#     event for event in early_start if early_start[event] == late_start[event]]
# print("Критичний маршрут:", critical_path)
plt.show()
