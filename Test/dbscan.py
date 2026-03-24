from math import dist

# data - точки
# eps - минимальное расстояние между точками (радиус ядра)
# minPts - мин. кол-во соседей для ядра
def dbscan(data, eps, minPts):
    n = len(data)
    labels = [None] * n
    cluster_id = 0

    for id in range(n):
        if labels[id] is not None:
            continue

        # Находим соседей (расстояние до них <= eps)
        neighbors = [j for j in range(n) if dist(data[id], data[j]) <= eps]

        # Аномальная точка? Если меньше минимального кол-ва соседей
        if len(neighbors) < minPts:
            labels[id] = -1
            continue

        # Начали обработку новой "пачки" точек
        cluster_id += 1
        labels[id] = cluster_id
        queue = neighbors

        # Пока существует очередь из соседей
        while queue:
            j = queue.pop()
            if labels[j] is None:
                labels[j] = cluster_id
                new_neighbors = [k for k in range(n) if dist(data[j], data[k]) <= eps]
                # Добавляем соседей этого соседа только если кол-во больше минимального кол-ва соседей
                if len(new_neighbors) >= minPts:
                    queue.extend(new_neighbors)
            # Если помечены как аномалии, но на самом деле крайние точки кластера
            elif labels[j] == -1:
                labels[j] = cluster_id

    return labels
