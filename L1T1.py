import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")  # use full path if needed

print("Shape of dataset:", df.shape)

print("\nBasic Info:")
print(df.info())

# -------------------------------
# STEP 2: Missing Values
# -------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df = df.dropna(subset=['Cuisines'])

# -------------------------------
# STEP 3: Data Type Conversion
# -------------------------------
binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']

for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# -------------------------------
# STEP 4: Target Variable Analysis
# -------------------------------
print("\nAggregate Rating Distribution:")
print(df['Aggregate rating'].value_counts())

# Plot distribution
plt.figure()
df['Aggregate rating'].hist(bins=20)
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# Remove 0 ratings (Not Rated)
df = df[df['Aggregate rating'] != 0]

print("\nShape after removing 0 ratings:", df.shape)

# -------------------------------
# STEP 5: Descriptive Statistics
# -------------------------------
print("\nStatistical Summary:")
print(df.describe())

print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))

# -------------------------------
# STEP 6: Categorical Analysis
# -------------------------------

# Country Code
print("\nCountry Code Distribution:")
print(df['Country Code'].value_counts())

# City
print("\nTop 10 Cities:")
top_cities = df['City'].value_counts().head(10)
print(top_cities)

# Cuisines (raw)
print("\nTop 10 Cuisines (raw):")
print(df['Cuisines'].value_counts().head(10))

# Split cuisines for better analysis
cuisine_series = df['Cuisines'].str.split(', ').explode()

print("\nTop 10 Individual Cuisines:")
top_cuisines = cuisine_series.value_counts().head(10)
print(top_cuisines)

# -------------------------------
# STEP 7: Visualizations
# -------------------------------

# Top Cities Graph
plt.figure()
top_cities.plot(kind='bar')
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Top Cuisines Graph
plt.figure()
top_cuisines.plot(kind='bar')
plt.title("Top 10 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
# -------------------------------
# STEP 8: Geospatial Analysis
# -------------------------------

import pandas as pd
import folium

# Load dataset
df = pd.read_csv("Dataset.csv")

# Take small sample
sample_df = df.sample(50)

# Create map (center India for safety)
restaurant_map = folium.Map(location=[20.59, 78.96], zoom_start=5)

# Add markers
for _, row in sample_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name']
    ).add_to(restaurant_map)

# Save file
restaurant_map.save("restaurant_map.html")

print("Map created successfully!")