from math import dist

def dbscan(data, eps, minPts):
    n = len(data)
    labels = [None] * n
    cluster_id = 0

    for id in range(n):
        if labels[id] is not None:
            continue

        neighbors = [j for j in range(n) if dist(data[id], data[j]) <= eps]

        if len(neighbors) < minPts:
            labels[id] = -1
            continue

        cluster_id += 1
        labels[id] = cluster_id
        queue = neighbors

        while queue:
            j = queue.pop()
            if labels[j] is None:
                labels[j] = cluster_id
                new_neighbors = [k for k in range(n) if dist(data[j], data[k]) <= eps]
                if len(new_neighbors) >= minPts:
                    queue.extend(new_neighbors)
            elif labels[j] == -1:
                labels[j] = cluster_id

    return labels

file = open('27-38b.txt')

dots = []
for line in file:
    dots.append(
        list(map(lambda x: float(x.replace(',', '.')), line.split('\t')))
    )

labels = dbscan(dots, 0.9, 6)
for i, cluster_id in enumerate(labels):
    dots[i].append(cluster_id)

import matplotlib.pyplot as plt

colors = ['blue', 'green', 'orange', 'red', 'yellow', 'black']
plt.figure(figsize=(10, 6))

for idx, point in enumerate(dots):
        plt.scatter(point[0], point[1], c=colors[point[2]], s=30)

plt.title("Ручная реализация DBSCAN")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
