# 🍽️ Restaurant Data Analysis Project

## 📌 Overview
This project involves data exploration, preprocessing, descriptive analysis, and geospatial visualization of a restaurant dataset. The goal is to extract meaningful insights about restaurant distribution, ratings, and cuisines.

---

## 📊 Dataset Description
The dataset contains **9551 rows and 21 columns**, including:
- Restaurant details (Name, City, Address)
- Location (Latitude, Longitude)
- Services (Table booking, Online delivery)
- Cost and pricing
- Ratings and votes

---

## 🔧 Tasks Performed

### 1️⃣ Data Exploration & Preprocessing
- Checked dataset structure and data types
- Identified and handled missing values
- Converted categorical variables into numerical format
- Removed zero-rated (unrated) entries to avoid bias

---

### 2️⃣ Descriptive Analysis
- Calculated statistical measures:
  - Mean, Median, Standard Deviation
- Analyzed categorical variables:
  - Country Code
  - City
  - Cuisines
- Identified:
  - Top cities with most restaurants
  - Most popular cuisines

---

### 3️⃣ Geospatial Analysis 🌍
- Visualized restaurant locations using **Folium**
- Created an interactive map (`restaurant_map.html`)
- Observed clustering of restaurants in urban areas
- Analyzed correlation between location and ratings

---

## 📈 Key Insights
- A large number of restaurants were **unrated (rating = 0)**, which required cleaning
- Restaurants are **highly concentrated in major cities**
- Popular cuisines include **North Indian, Chinese, Fast Food**
- **Location does not significantly affect ratings**
- Ratings depend more on quality, service, and cost

---

## 🛠️ Technologies Used
- Python 🐍
- Pandas
- Matplotlib
- Folium

---

## 📁 Project Structure
