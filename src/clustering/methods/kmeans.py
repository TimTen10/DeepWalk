# kmeans returns centroids
# TODO: Where to put Kosten eines Clusters and Kosten des Clustering


def _generate_clusters(centroids, points):
    pass


def kmeans(points, k):
    centroids = points[:k]
    clusters = _generate_clusters(centroids, points[k:])


def main():
    print(kmeans([[1, 2], [4, 5], [7, 3], [0, 9]], 2))


if __name__ == '__main__':
    main()
