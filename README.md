# 📊 Online Retail — Data Cleaning Project

**Author:** Bruna Martins  
**Role:** Data Analyst  

---

## 📌 Project Objective

Clean and standardize a real-world retail dataset to prepare it for:

- Business Intelligence analysis
- Feature engineering
- Price normalization (price per gram)
- Brand-level aggregation
- Future modeling tasks

---

## 🧹 Cleaning Pipeline

### 1️⃣ Date Treatment
- Converted `OrderDate` to datetime
- Created `Year` and `Month` features

### 2️⃣ Unit Price Treatment
- Removed products without valid prices
- Imputed missing prices using product-level median
- Removed residual null values

### 3️⃣ Weight Treatment
- Extracted numeric weight values from raw text
- Extracted weight units
- Normalized units (g, kg, mg, oz, lb)
- Converted all mass units to grams
- Standardized mass units to `"g"`

### 4️⃣ Text Standardization
- Cleaned `ProductName`
- Cleaned `Brand`
- Removed special characters
- Lowercased text
- Standardized spacing

---------

## 🗂 Project Structure

