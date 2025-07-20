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

file = open('7581b.txt')
points = []

for line in file:
    # 20,133309069966206 27,48116774734547
    x, y = line.split() # ['20,13330906996620', '27,48116774734547']
    points.append([float(x.replace(',', '.')), float(y.replace(',', '.'))])

clusters = [[], [], []]
for point in points:
    if point[0] < 3 and point[1] < 4:
        clusters[0].append(point)
    elif point[0] > 2 and point[1] > 6 and point[0] < 5:
        clusters[1].append(point)
    else:
        clusters[2].append(point)

centers = []
for cluster in clusters:
    center = get_center_of_cluster(cluster)
    centers.append(center)
print(f"Центры кластеров - {centers}")

Px = int(sum([center[0] for center in centers])/len(centers)*10000)
Py = int(sum([center[1] for center in centers])/len(centers)*10000)

print(Px, Py)