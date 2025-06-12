# ✅ Step 0: Fix warnings & environment issue
import os
import warnings
os.environ["LOKY_MAX_CPU_COUNT"] = "4"
warnings.filterwarnings("ignore", category=UserWarning, module="joblib")

# ✅ Step 1: Imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ✅ Step 2: Load dataset
df = pd.read_csv('Mall_Customers.csv')

# ✅ Step 3: Preprocessing
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})  # Convert Gender
features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# ✅ Step 4: Elbow Method
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(scaled_features)
    inertias.append(km.inertia_)

# Save Elbow Plot
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid(True)
plt.savefig("elbow_plot.png", dpi=300)
plt.show()

# ✅ Step 5: Apply KMeans with k=5
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# ✅ Step 6: Save Cluster Plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Annual Income (k$)'],
                      df['Spending Score (1-100)'],
                      c=df['Cluster'],
                      cmap='viridis',
                      s=100)

plt.title('Customer Segmentation with K-Means')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.savefig("customer_clusters.png", dpi=300)
plt.show()

# ✅ Step 7: Save clustered dataset
df.to_csv("Mall_Customers_Clustered.csv", index=False)

# ✅ Step 8: Insights – Cluster Summary
print("\n==== Cluster Counts ====")
print(df['Cluster'].value_counts())

print("\n==== Average Spending Score per Cluster ====")
print(df.groupby('Cluster')["Spending Score (1-100)"].mean().round(2))

print("\n==== Average Annual Income per Cluster ====")
print(df.groupby('Cluster')["Annual Income (k$)"].mean().round(2))

print("\n==== Age Distribution per Cluster ====")
print(df.groupby('Cluster')["Age"].mean().round(1))

print("\n==== Gender Count per Cluster ====")
print(df.groupby(['Cluster', 'Gender']).size())

# ✅ Step 9: Suggested Cluster Descriptions (Manual mapping)
print("\n==== Suggested Cluster Interpretation ====")
cluster_insights = {
    0: "🟢 Cluster 0: Moderate income, high spending — Ideal for loyalty rewards.",
    1: "🔵 Cluster 1: High income, low spending — Push luxury brand campaigns.",
    2: "🟡 Cluster 2: Low income, moderate spending — Offer discounts & referral.",
    3: "🟣 Cluster 3: High income, high spending — VIP customer program potential.",
    4: "🔴 Cluster 4: Young customers with low income — Target with digital ads."
}
for k, insight in cluster_insights.items():
    print(insight)
