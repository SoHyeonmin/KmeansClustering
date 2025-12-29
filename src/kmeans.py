import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Data
X = np.array([
    [6, 3], [11, 15], [17, 12], [24, 10], [20, 25], [22, 30],
    [85, 70], [71, 81], [60, 79], [56, 52], [81, 91], [80, 81]
])

# 1) Raw scatter
plt.figure()
plt.scatter(X[:, 0], X[:, 1])
plt.title("Raw points")
plt.savefig("images/scatter_raw.png", dpi=200, bbox_inches="tight")
plt.close()

# 2) KMeans
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto")
kmeans.fit(X)

print("cluster centers:")
print(kmeans.cluster_centers_)
print("labels:")
print(kmeans.labels_)

# 3) Clustered scatter
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="rainbow")
plt.title("KMeans clustered (k=2)")
plt.savefig("images/scatter_clustered.png", dpi=200, bbox_inches="tight")
plt.close()
