# Fraud Detection Project (KAIM Week 8&9)

Detecting fraud in e-commerce and bank transactions using ML.

Perfect! Here's a **README** draft for your `fraud-detection-kaim` project, covering everything up to **Task 2**.

---

## 🛡️ Fraud Detection – KAIM Week 8–9 Project

### 🔍 Overview

This project tackles **fraud detection** using real-world transactional and geolocation data. It is part of the 10 Academy KAIM Week 8–9 sprint challenge. The aim is to analyze fraud patterns, engineer useful features, handle data imbalances, and build a predictive model for fraud classification.

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
│   ├── 02_data_transformation.ipynb
│
├── src/
│   └── __init__.py
|   └── data_preprocessing.py
|   └── feature_engineering.py
|   └── model_training.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

### 📊 Task 1 – Data Preparation & Transformation

#### 1. Data Loading & Cleaning

- Loaded `Fraud_Data.csv`, `IpAddress_to_Country.csv`, and `creditcard.csv`.
- Checked and confirmed: no missing values.
- Duplicates:

  - Fraud_Data: 0
  - Credit Card Data: 1081
  - IP Data: 0

#### 2. Merging IP Info

- Converted IP addresses to integer format.
- Merged IP country info using IP range logic.

#### 3. Exploratory Data Analysis (EDA)

- **Univariate analysis**: Age, sign-up and purchase times, purchase value.
- **Bivariate analysis**: Fraud vs. country, browser, device, etc.
- Found significant imbalance in fraud class.

#### 4. Data Transformation

#### 🔹 Class Imbalance Handling

- Used **SMOTE** on training data to balance classes.
- Resampled only training set to prevent data leakage.

#### 🔹 Encoding

- Applied **One-Hot Encoding** to categorical features (source, browser, sex, country).
- Handled unknown categories gracefully using `handle_unknown="ignore"`.

#### 🔹 Scaling

- Applied **StandardScaler** to numerical features.
- Ensured feature consistency and reduced model bias.

---

### 📦 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

### 📌 Tasks Completed

- ✅ Task 1: Data Cleaning, EDA, IP merge
- ✅ Task 2: SMOTE, Encoding, Scaling

---

### 🚧 To Do (Upcoming Tasks)

- 📈 Model training and evaluation (Logistic Regression, XGBoost, etc.)
- 🧪 Hyperparameter tuning and model selection
- 🧾 Final report and performance metrics
