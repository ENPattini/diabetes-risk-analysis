# Analisi del Rischio Diabete e Insights di Sanità Pubblica

**USA BRFSS 2023 • SQL • Clustering • Dashboard Streamlit • Contesto Latinoamericano**

*Disponibile in: 🇬🇧 English → [README.md](README.md) | 🇪🇸 Español → [README.es.md](README.es.md) | 🇮🇹 Italiano (questo file)*

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![DuckDB](https://img.shields.io/badge/DuckDB-SQL-8A2BE2?logo=duckdb&logoColor=white)](https://duckdb.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B.svg)](https://streamlit.io/)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Dati USA con Contesto Latinoamericano**  
*Analisi BRFSS 2023 + Insights Regionali IDF/PAHO*

### 📋 Sintesi del Progetto

Questo progetto di portfolio analizza il rischio di diabete utilizzando il dataset **Behavioral Risk Factor Surveillance System (BRFSS 2023)** (261,589 record).

Include:
- Preparazione dei dati e feature engineering con **SQL** (DuckDB)
- Modellazione di classificazione binaria per rischio diabete
- Segmentazione della popolazione con clustering K-Means
- Una **dashboard interattiva in Streamlit**
- Contesto regionale e proiezioni al 2050 per Sud e Centro America

---

### 🚀 Dashboard Interattiva e Report

- **Dashboard Streamlit** (con predittore di rischio interattivo):

    [🔗 Apri Dashboard Live](https://diabetes-risk-analysis-dashboard.streamlit.app/)  

- **Report HTML Interattivo**: 

    [Visualizza Report Analisi Rischio Diabete (HTML)](https://emilionahuelpattini.com/it/data/data-analysis/projects/diabetes-report/diabetes-risk-analysis.html)  

- **Scarica Versione PDF** (stampabile – Italiano): 

    [Scarica Report Analisi Rischio Diabete – PDF](reports/Diabetes_Risk_Analysis-IT.pdf)


---

### 🛠️ Stack Tecnologico

- **Python** • **DuckDB** (Uso intensivo di SQL)
- **Pandas** • **Scikit-learn**
- **Plotly** • **Streamlit** (Dashboard Interattiva)
- **Clustering K-Means**

---

### 📊 Funzionalità Principali

- **Focus su SQL**: Preparazione dati, pulizia e feature engineering estensiva con DuckDB
- **Predictor di Rischio Interattivo**: Stima in tempo reale del rischio diabete con un modello di Regressione Logistica addestrato
- **Segmentazione della Popolazione**: Clustering K-Means per identificare 4 gruppi di rischio distinti
- **Spiegabilità del Modello**: Analisi dell’importanza delle feature e interpretazione dei cluster
- **Contesto Latinoamericano**: Integrazione di dati IDF e PAHO con proiezioni al 2050
- **Dashboard Professionale**: Applicazione Streamlit completamente interattiva

---

### 📈 Principali Insights

- Età, BMI, salute generale e ipertensione sono i predittori più forti del rischio diabete
- Sono stati identificati quattro segmenti di popolazione chiari, con prevalenza del diabete tra **10%** (Basso Rischio) e **64%** (Rischio Molto Alto)
- L’obesità combinata con età avanzata crea gruppi particolarmente ad alto rischio
- In America Latina si prevede un aumento sostanziale dei casi di diabete, da 35.4 milioni nel 2024 a 51.5 milioni entro il 2050
- Opportunità significativa per programmi di prevenzione mirati ai cluster ad alto rischio

---

### 📁 Struttura del Progetto

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

### 🏃‍♂️ Come Esplorare il Progetto

#### 1. Aprire il Notebook Principale (Consigliato)

- Apri `Diabetes_Risk_Analysis-EN.ipynb` in **JupyterLab** o **VS Code**

- Il notebook contiene l’analisi completa end-to-end:
  - Preparazione e pulizia dei dati (con SQL)
  - Analisi Esplorativa dei Dati
  - Feature engineering
  - Modellazione e valutazione
  - Clustering
  - Conclusioni e insights

#### 2. Eseguire la Dashboard Interattiva

Puoi anche esplorare l’applicazione web live:

```bash
# Usando conda (consigliato)
conda env create -f environment.yml
conda activate diabetes_project
streamlit run app.py

# Oppure usando pip
pip install -r requirements.txt
streamlit run app.py
```

---

### Screenshot

![Predictor di Rischio](images/diabetes_risk_predictor.jpg)

![Clusters](images/diabetes_clusters.jpg)

---

### 👤 Contatto

- 📧 contact@emilionahuelpattini.com

- 💼 https://www.linkedin.com/in/emilionahuelpattini

- 🐙 https://github.com/ENPattini


Grazie per aver visionato questo progetto!  

Sentiti libero di contattarmi per domande o suggerimenti.

© Emilio Nahuel Pattini - Aprile 2026 - Buenos Aires, Argentina

---

### 📄 Licenza

Questo progetto è rilasciato sotto la MIT License - vedi il file [LICENSE](LICENSE) per maggiori dettagli.