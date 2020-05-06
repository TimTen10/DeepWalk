# TODO: Where to put Kosten eines Clusters and Kosten des Clustering
from src.clustering.util import distances as dist


def _generate_clusters(centroids, points, d):
    clusters = [[] for _ in centroids]
    for point in points:
        distances = [d(centroid, point) for centroid in centroids]
        clusters[distances.index(min(distances))].append(point)
    return clusters


def _generate_centroid(cluster):
    return [sum(p[0] for p in cluster) / len(cluster), sum(p[1] for p in cluster) / len(cluster)]


def kmeans(points, k, d):
    # TODO: implementation of uni course kmeans, not quite real kmeans yet! Initial centroids differ
    # normally split points and generate centroids out of these

    centroids = points[:k]
    # clusters = _generate_clusters(centroids, points, d)
    final_centroids = list()
    while final_centroids != centroids:
        final_centroids = centroids
        clusters = _generate_clusters(final_centroids, points, d)
        print(clusters)
        centroids = [_generate_centroid(cluster) for cluster in clusters]
    return final_centroids


def main():
    print(kmeans([[1, 5], [6, 2], [8, 1], [3, 5], [2, 4], [2, 6],
                  [6, 1], [6, 8], [7, 3], [7, 6], [8, 3], [8, 7]], 3, dist.lp_metric))


if __name__ == '__main__':
    main()
