# 🏠 House Price Prediction Web App

A **Machine Learning + Flask** web application that predicts house prices based on **location**, **BHK**, **bathrooms**, and **square footage**.  
This project demonstrates the complete pipeline — from data cleaning and feature engineering to model training and web deployment.

---

## 📘 Project Overview

The app allows users to enter house details and get an estimated price instantly.  
It uses a trained regression model built with **scikit-learn**, deployed via **Flask**, and styled with HTML & CSS.

---

## 📊 About the Dataset

The dataset (sourced from **Kaggle - Bangalore House Price Data**) includes:
- Location  
- Size (BHK)  
- Total area in square feet  
- Number of bathrooms  
- Price (target)

---

## 🧹 Data Cleaning & Preprocessing

- Removed missing and inconsistent values  
- Extracted numeric values from “BHK” and “total_sqft”  
- Removed outliers using mean ± 1 standard deviation rule for each location  
- Encoded categorical `location` using OneHotEncoding  
- Scaled numerical features with StandardScaler  

---

## 🧠 Model Development

Multiple regression models were trained and compared:

| Model | Description | R² Score |
|--------|--------------|----------|
| Linear Regression | Baseline model | 0.85 |
| Ridge Regression | L2 regularization | **0.86** |
| Lasso Regression | L1 regularization | 0.83 |

**Final Model:** Ridge Regression (R² = 0.86)  
It gave the best accuracy and stability for unseen data.

---

## 🧰 Technologies Used

| Category | Tools |
|-----------|-------|
| Programming | Python |
| ML Libraries | Pandas, NumPy, Scikit-learn, Joblib |
| Web Framework | Flask |
| Frontend | HTML, CSS |

---

## 🌐 Web App Features

- Dropdown for **locations** (auto-loaded from dataset)  
- Input fields for **BHK**, **Bath**, and **Sqft**  
- Displays predicted price instantly after form submission  

---

## 📦 Project Structure
```
HousePrice_Predictor/
│
├── app.py
├── house_price_model.pkl
├── locations.json
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md
```
## ⚙️ How to Run

1️⃣ Clone the repository  
2️⃣ Run the Flask app (`python app.py`)  
3️⃣ Open **http://127.0.0.1:5000/** in your browser  

---
