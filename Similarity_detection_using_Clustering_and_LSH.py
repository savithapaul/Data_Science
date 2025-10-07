from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import hashlib

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Apply DBSCAN for clustering
dbscan = DBSCAN(eps=0.5, min_samples=2)
df['cluster'] = dbscan.fit_predict(X_scaled)

# Locality-Sensitive Hashing for quick approximate neighbor search
def lsh_hash(vector):
    return hashlib.md5(vector.tobytes()).hexdigest()

df['lsh'] = df['content'].apply(lambda x: lsh_hash(np.frombuffer(x.encode(), dtype=np.uint8)))

# Identify duplicates using LSH
duplicate_groups = df[df['cluster'] != -1]

print("Duplicate Groups:")
for cluster in df['cluster'].unique():
    if cluster != -1:
        duplicates = df[df['cluster'] == cluster]
        print(duplicates[['file_id', 'lsh']])
