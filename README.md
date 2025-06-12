# 🧠 K-Means Clustering for Customer Segmentation

This project applies **K-Means Clustering** to the popular **Mall Customers dataset** to identify unique customer segments based on their annual income and spending score. It's ideal for marketing teams, analysts, and data science learners looking to understand customer behavior.

---

## 📌 Project Highlights

- Uses **scikit-learn's KMeans** to segment customers
- Applies **Elbow Method** to find optimal number of clusters
- Visualizes clusters using `matplotlib`
- Saves outputs as CSV and PNG images
- Provides **actionable insights** per cluster
- Fully compatible with **Python 3.13 and Windows 11**

---

## 📂 Dataset Used

- File: `Mall_Customers.csv`
- Columns:
  - `CustomerID`
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/kmeans-customer-segmentation.git
cd kmeans-customer-segmentation
pip install pandas matplotlib scikit-learn
python kmeans_customer_segmentation.py
| File Name                      | Description                            |
| ------------------------------ | -------------------------------------- |
| `elbow_plot.png`               | Visual of optimal cluster number       |
| `customer_clusters.png`        | Cluster segmentation scatter plot      |
| `Mall_Customers_Clustered.csv` | Clustered dataset with insights        |
| `Console Output`               | Cluster-wise stats and marketing ideas |
🔍 Sample Cluster Insights
Cluster 0: Moderate income, high spending – Offer loyalty rewards

Cluster 1: High income, low spending – Push luxury campaigns

Cluster 3: High income, high spending – VIP or elite programs

Cluster 4: Young, low income – Target via social media ads

🛠 Technologies Used
Python 3.13

Pandas

Matplotlib

Scikit-learn

