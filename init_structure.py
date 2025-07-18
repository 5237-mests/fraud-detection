import os

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "reports",
    "figures",
    "utils"
]

files = {
    "README.md": "# Fraud Detection Project (KAIM Week 8&9)\n\nDetecting fraud in e-commerce and bank transactions using ML.",
    ".gitignore": "data/\n__pycache__/\n.ipynb_checkpoints/\n.env\n*.pyc",
    "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\nxgboost\nshap\nimbalanced-learn\n",
    "src/__init__.py": "",
    "src/data_preprocessing.py": "# Data cleaning and preprocessing functions",
    "src/feature_engineering.py": "# Feature engineering logic (time, IP mapping, etc.)",
    "src/model_training.py": "# Training and evaluating models",
    "src/explainability.py": "# SHAP explainability functions",
    "utils/ip_conversion.py": "# Convert IP to integer",
    "notebooks/01_data_cleaning.ipynb": "",
    "notebooks/02_eda.ipynb": "",
    "notebooks/03_feature_engineering.ipynb": "",
    "notebooks/04_modeling_explainability.ipynb": "",
    "reports/interim1_report.md": "",
    "reports/interim2_report.md": "",
    "reports/final_report.md": "",
    "environment.yml": "name: fraud_env\ndependencies:\n  - python=3.10\n  - pip\n  - pip:\n    - -r requirements.txt"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    dir_name = os.path.dirname(filepath)
    if dir_name:  # Only create folder if not in root
        os.makedirs(dir_name, exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)

print("✅ Project structure initialized in current directory.")
