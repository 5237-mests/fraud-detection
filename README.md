## 🛡️ Fraud Detection – KAIM Week 8–9 Project

### 🔍 Overview

This project tackles **fraud detection** using real-world transactional and geolocation data. It is part of the 10 Academy KAIM Week 8–9 sprint challenge. The aim is to analyze fraud patterns, engineer useful features, handle data imbalances, and build predictive models for fraud classification.

---

### 📁 Project Structure

```
fraud-detection/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_training.ipynb
│
├── src/
│   └── __init__.py
│   └── data_preprocessing.py
│   └── feature_engineering.py
│   └── model_training.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

### 📊 Task 1 – Data Preparation & Transformation

#### 1. Data Loading & Cleaning

- Loaded `Fraud_Data.csv`, `IpAddress_to_Country.csv`, and `creditcard.csv`.
- Confirmed no missing values.
- Removed duplicates:

  - Credit card dataset had 1081 duplicates.

#### 2. Merging IP Info

- Converted IP addresses to integers and merged with geolocation data.
- Generated `country` column for fraud data.

#### 3. Exploratory Data Analysis (EDA)

- Univariate analysis of user behavior: age, purchase value, time features.
- Bivariate comparisons: Fraud rate by source, browser, country, etc.

#### 4. Data Transformation

- Addressed **class imbalance** using **SMOTE** (oversampling minority class).
- Performed **One-Hot Encoding** on categorical features.
- Applied **StandardScaler** to numeric columns.

---

### 🤖 Task 2 – Model Building & Evaluation

We trained and evaluated two models on both datasets:

- **Logistic Regression** (baseline, interpretable)
- **Random Forest** (powerful ensemble method)

#### 📌 Model Evaluation Metrics

Used metrics suitable for **imbalanced classification**, including:

- F1 Score
- AUC-PR (Area Under the Precision-Recall Curve)
- Confusion Matrix

---

#### 🧾 Fraud_Data Dataset Results

| Model               | F1 Score | AUC-PR | Precision (fraud) | Recall (fraud) |
| ------------------- | -------- | ------ | ----------------- | -------------- |
| Logistic Regression | 0.267    | 0.498  | 0.17              | 0.70           |
| Random Forest       | 0.546    | 0.617  | 0.55              | 0.55           |

- 📌 **Random Forest** outperformed Logistic Regression in both precision and F1.

---

#### 💳 Credit Card Dataset Results

| Model               | F1 Score | AUC-PR | Precision (fraud) | Recall (fraud) |
| ------------------- | -------- | ------ | ----------------- | -------------- |
| Logistic Regression | 0.106    | 0.672  | 0.06              | 0.87           |
| Random Forest       | 0.831    | 0.788  | 0.97              | 0.73           |

- 📌 **Random Forest** achieved outstanding performance, with high F1 and precision for fraud cases.

---

### 🧠 Task 3 – Model Explainability with SHAP

Used **SHAP (SHapley Additive exPlanations)** to interpret the Random Forest model.

#### ✅ Global Interpretability (SHAP Summary Plot)

- Computed SHAP values for a sample of training data.
- Plotted summary showing top features driving fraud predictions:

  - `purchase_value`
  - `time_since_signup`
  - `hour_of_day` and `day_of_week` features
  - User/browser attributes

#### 🔎 Local Interpretability (SHAP Force Plot)

- Visualized how individual features influenced a specific prediction.
- Helps in explaining **why a transaction was marked as fraud** — critical for audit/compliance.

---

### ✅ Completed Tasks

- ✅ Task 1: Data Cleaning, EDA, Feature Engineering
- ✅ Task 2: Model Training, Evaluation, Export
- ✅ Task 3: Model Explainability (SHAP)

---
