
# 6. Working with Time Series Data
import pandas as pd
import numpy as np

# Creating a time series dataset
date_rng = pd.date_range(start='2020-01-01', end='2020-01-10', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(date_rng)))

# Converting 'date' column to DateTime object
df['date'] = pd.to_datetime(df['date'])

# Set 'date' as index
df.set_index('date', inplace=True)

# Resample data by day and compute sum
daily_data = df.resample('D').sum()

# Resample data by month and compute mean
monthly_data = df.resample('M').mean()

print("Daily data resampled:\n", daily_data)
print("Monthly data resampled:\n", monthly_data)


# 7. Data Normalization
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample dataset
data = np.array([[100, 0.001],
                 [200, 0.005],
                 [300, 0.004],
                 [400, 0.002]])

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("Normalized Data:\n", scaled_data)


# 8. Handling Missing Data
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, 8, 10],
    'C': [10, 11, 12, np.nan, 15]
})

# Handling missing values
# Fill missing values with the mean
df_filled = df.fillna(df.mean())

# Drop rows with missing values
df_dropped = df.dropna()

print("Original DataFrame:\n", df)
print("\nFilled Missing Values (with mean):\n", df_filled)
print("\nRows Dropped with Missing Values:\n", df_dropped)


# 9. Principal Component Analysis (PCA)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([[2.5, 2.4],
              [0.5, 0.7],
              [2.2, 2.9],
              [1.9, 2.2],
              [3.1, 3.0],
              [2.3, 2.7],
              [2.0, 1.6],
              [1.0, 1.1],
              [1.5, 1.6],
              [1.1, 0.9]])

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Original Data:\n", X)
print("\nPCA Transformed Data:\n", X_pca)


# 10. K-Means Clustering
from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

# Initialize KMeans
kmeans = KMeans(n_clusters=2)

# Fit the model
kmeans.fit(X)

# Get cluster centers and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print("Cluster Centers:\n", centroids)
print("Labels:\n", labels)
