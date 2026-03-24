import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# STEP 2: Basic Cleaning (IMPORTANT)
# -------------------------------

# Remove missing cuisines
df = df.dropna(subset=['Cuisines'])

# Convert Yes/No to 1/0
binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']

for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# Remove unrated restaurants
df = df[df['Aggregate rating'] != 0]

# -------------------------------
# STEP 3: Percentage Calculation
# -------------------------------

total_restaurants = len(df)

table_booking_percent = (df['Has Table booking'].sum() / total_restaurants) * 100
online_delivery_percent = (df['Has Online delivery'].sum() / total_restaurants) * 100

print("\nPercentage of Restaurants with Table Booking:", round(table_booking_percent, 2), "%")
print("Percentage of Restaurants with Online Delivery:", round(online_delivery_percent, 2), "%")

# -------------------------------
# STEP 4: Rating Comparison
# -------------------------------

avg_rating_booking = df.groupby('Has Table booking')['Aggregate rating'].mean()

print("\nAverage Ratings based on Table Booking:")
print(avg_rating_booking)

# -------------------------------
# STEP 5: Online Delivery vs Price Range
# -------------------------------

delivery_price = df.groupby('Price range')['Has Online delivery'].mean() * 100

print("\nOnline Delivery Availability by Price Range (%):")
print(delivery_price)

# -------------------------------
# STEP 6: Visualizations
# -------------------------------

# Table Booking vs Rating
plt.figure()
avg_rating_booking.plot(kind='bar')
plt.title("Average Rating: Table Booking vs No Booking")
plt.xlabel("Table Booking (0 = No, 1 = Yes)")
plt.ylabel("Average Rating")
plt.show()

# Online Delivery vs Price Range
plt.figure()
delivery_price.plot(kind='bar')
plt.title("Online Delivery Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Percentage (%)")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# STEP 2: Basic Cleaning
# -------------------------------

# Remove missing cuisines
df = df.dropna(subset=['Cuisines'])

# Convert Yes/No to 1/0
binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']

for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# Remove unrated restaurants
df = df[df['Aggregate rating'] != 0]

# -------------------------------
# STEP 3: Most Common Price Range
# -------------------------------

most_common_price = df['Price range'].value_counts().idxmax()
print("\nMost Common Price Range:", most_common_price)

# -------------------------------
# STEP 4: Average Rating per Price Range
# -------------------------------

avg_rating_price = df.groupby('Price range')['Aggregate rating'].mean()
print("\nAverage Rating for Each Price Range:")
print(avg_rating_price)

# -------------------------------
# STEP 5: Color with Highest Rating
# -------------------------------

color_rating = df.groupby('Rating color')['Aggregate rating'].mean()

highest_color = color_rating.idxmax()
print("\nColor with Highest Average Rating:", highest_color)

# -------------------------------
# STEP 6: Visualization (Optional)
# -------------------------------

plt.figure()
avg_rating_price.plot(kind='bar')
plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.show()
import pandas as pd

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# STEP 2: Basic Cleaning
# -------------------------------

# Remove missing cuisines
df = df.dropna(subset=['Cuisines'])

# Remove unrated restaurants
df = df[df['Aggregate rating'] != 0]

# -------------------------------
# STEP 3: Feature Engineering
# -------------------------------

# 1. Length of Restaurant Name
df['Name_Length'] = df['Restaurant Name'].apply(len)

# 2. Length of Address
df['Address_Length'] = df['Address'].apply(len)

# 3. Number of Cuisines offered
df['Num_Cuisines'] = df['Cuisines'].apply(lambda x: len(x.split(',')))

# 4. Binary Encoding (Yes/No → 1/0)
binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']

for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# 5. Create combined feature (useful insight)
df['Service_Score'] = df['Has Table booking'] + df['Has Online delivery']

# -------------------------------
# STEP 4: Show New Features
# -------------------------------

print("\nNew Features Added:")
print(df[['Restaurant Name', 'Name_Length', 'Address_Length', 'Num_Cuisines', 'Service_Score']].head())

# Optional: Save new dataset
df.to_csv("engineered_dataset.csv", index=False)

print("\nFeature Engineering Completed. New dataset saved.")