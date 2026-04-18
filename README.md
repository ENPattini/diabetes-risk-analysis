# Diabetes Risk Analysis & Public Health Insights

**US BRFSS 2023 • SQL • Clustering • Streamlit Dashboard • Latin America Context**

*Available in: 🇬🇧 English (this file) | 🇪🇸 Español → [README.es.md](README.es.md) | 🇮🇹 Italiano → [README.it.md](README.it.md)*

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![DuckDB](https://img.shields.io/badge/DuckDB-SQL-8A2BE2?logo=duckdb&logoColor=white)](https://duckdb.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B.svg)](https://streamlit.io/)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


### 📋 Project Overview

This portfolio project analyzes diabetes risk using the **Behavioral Risk Factor Surveillance System (BRFSS 2023)** dataset (261,589 records). 

It includes:
- Strong **SQL** data preparation and feature engineering (DuckDB)
- Binary classification modeling for diabetes risk
- Population segmentation using K-Means clustering
- An interactive **Streamlit dashboard**
- Regional context and 2050 projections for South & Central America

---

### 🚀 Interactive Dashboard & Report

- **Streamlit Dashboard** (with interactive risk predictor):

    [🔗 Open Live Dashboard](https://diabetes-risk-analysis-dashboard.streamlit.app/)  

- **Interactive HTML Report**: 

    [View Diabetes Risk Analysis Report (HTML)](https://emilionahuelpattini.com/en/data/data-analysis/projects/diabetes-report/diabetes-risk-analysis.html)  

- **Download PDF Version** (print-friendly – English): 

    [Download Diabetes Risk Analysis Report – PDF](reports/Diabetes_Risk_Analysis-EN.pdf)

---

### 🛠️ Tech Stack

- **Python** • **DuckDB** (Heavy SQL usage)
- **Pandas** • **Scikit-learn**
- **Plotly** • **Streamlit** (Interactive Dashboard)
- **K-Means Clustering**

---

### 📊 Key Features

- **Strong SQL Focus**: Extensive data preparation, cleaning, and feature engineering using DuckDB
- **Interactive Risk Predictor**: Real-time diabetes risk estimation using a trained Logistic Regression model
- **Population Segmentation**: K-Means clustering to identify 4 distinct risk groups
- **Model Explainability**: Feature importance analysis and cluster interpretation
- **Latin America Context**: Integration of IDF and PAHO data with 2050 projections
- **Professional Dashboard**: Fully interactive Streamlit application

---

### 📈 Main Insights

- Age, BMI, general health, and hypertension are the strongest predictors of diabetes risk
- Four clear population segments were identified, with diabetes prevalence ranging from **10%** (Low Risk) to **64%** (Very High Risk)
- Obesity combined with older age creates particularly high-risk groups
- Latin America is projected to see a substantial increase in diabetes cases, rising from 35.4 million in 2024 to 51.5 million by 2050
- Significant opportunity for targeted prevention programs focused on high-risk clusters

---

### 📁 Project Structure
```
Diabetes_Risk_Analysis/
├── streamlit_app.py
├── Diabetes_Risk_Analysis-EN.ipynb
├── Diabetes_Risk_Analysis-ES.ipynb
├── Diabetes_Risk_Analysis-IT.ipynb
├── requirements.txt
├── environment/environment.yml
├── LICENSE
├── README.md
│
├── data/
│   ├── raw/
│   │   └── diabetes_012_health_indicators_BRFSS2023.csv     # Original raw file (25MB)
│   └── diabetes_model_ready.parquet
│
├── models/
│   ├── logistic_regression_model.pkl
│   └── model_columns.json
│
├── reports/                                   
│   ├── Diabetes_Risk_Analysis_Report_EN.pdf
│   ├── Diabetes_Risk_Analysis_Report_ES.pdf
│   └── Diabetes_Risk_Analysis_Report_IT.pdf
│
└── images/

```

---

### 🏃‍♂️ How to Explore the Project

#### 1. Open the Main Notebook (Recommended)

- Open `Diabetes_Risk_Analysis-EN.ipynb` in **JupyterLab** or **VS Code**

- The notebook contains the full end-to-end analysis:
  - Data preparation & cleaning (with SQL)
  - Exploratory Data Analysis
  - Feature engineering
  - Modeling and evaluation
  - Clustering
  - Conclusions and insights

#### 2. Run the Interactive Dashboard

You can also explore the live web application:

```bash
# Using conda (recommended)
conda env create -f environment.yml
conda activate diabetes_project
streamlit run app.py

# Or using pip
pip install -r requirements.txt
streamlit run app.py
```

---

### Screenshots

![Risk Predictor](images/diabetes_risk_predictor.jpg)

![Clusters](images/diabetes_clusters.jpg)

---

### 👤 Contact

- 📧 contact@emilionahuelpattini.com

- 💼 https://www.linkedin.com/in/emilionahuelpattini

- 🐙 https://github.com/ENPattini


Thank you for checking out this project! 

Feel free to reach out if you have any questions or suggestions.

© Emilio Nahuel Pattini - April 2026 - Buenos Aires, Argentina

---

### 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.