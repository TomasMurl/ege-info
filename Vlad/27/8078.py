file = open('8078b.txt')
points = []

def get_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_center_of_cluster(cluster):
    min_dists = 10000000000000000
    result = 0
    for actual_point in cluster:
        sum_dists = 0
        for other_point in cluster:
            sum_dists += get_dist(actual_point, other_point)
        if sum_dists < min_dists:
            min_dists = sum_dists
            result = actual_point
    return result

for line in file:
    # 20,133309069966206 27,48116774734547
    x, y = line.split() # ['20,13330906996620', '27,48116774734547']
    points.append([float(x.replace(',', '.')), float(y.replace(',', '.'))])

clusters = [[], []]
for point in points:
    if point[1] < 0:
        clusters[0].append(point)
    else:
        clusters[1].append(point)

centers = []
for cluster in clusters:
    center = get_center_of_cluster(cluster)
    centers.append(center)
print(f"Центры кластеров - {centers}")

avg_x = 0
avg_y = 0
for center in centers:
    avg_x += center[0]
    avg_y += center[1]

avg_x = avg_x / len(centers)
avg_y = avg_y / len(centers)

Px = int(avg_x * 10000)
Py = int(avg_y * 10000)
print(Px, Py)