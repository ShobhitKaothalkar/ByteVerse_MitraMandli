import pandas as pd
from sklearn.cluster import KMeans

def generate_recommendations(user_data, curr_user_index):
    # One-hot encode the genres column
    genres = user_data['genres'].str.get_dummies(',')

    # Concatenate user_id column with genres DataFrame
    user_data = pd.concat([user_data['myindex'], user_data['user_ID'], genres], axis=1)

    # Determine optimal number of clusters using elbow method
    wcss = []
    for i in range(1, len(user_data)):
        kmeans = KMeans(n_clusters=i, random_state=0)
        kmeans.fit(user_data.iloc[:, 2:])
        wcss.append(kmeans.inertia_)

    # Cluster users based on genre preferences using optimal number of clusters
    kmeans = KMeans(n_clusters=3, random_state=0).fit(user_data.iloc[:, 2:])

    # Get cluster label for each user
    clusters = kmeans.labels_
    print(clusters)
    recommendations = []
    curr_cluster = clusters[curr_user_index]
    for i in range(len(clusters)):
        if clusters[i] == curr_cluster:
            if i != curr_user_index:
                recommendations.append(user_data.loc[user_data["myindex"] == i]["user_ID"])

    # Generate recommendations for each user
    return recommendations