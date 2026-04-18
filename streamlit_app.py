import streamlit as st
import duckdb
import pandas as pd
import joblib
import json
import plotly.express as px

# ======================
# Page Configuration
# ======================
st.set_page_config(
    page_title="Diabetes Risk Analyzer",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Diabetes Risk Prediction & Insights")
st.markdown("### US Data with Latin America Context")

# ======================
# Load Data and Model
# ======================
@st.cache_data
def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * FROM read_parquet('data/diabetes_model_ready.parquet')").fetchdf()
    return df

@st.cache_resource
def load_model():
    model = joblib.load("models/logistic_regression_model.pkl")
    with open("models/model_columns.json", "r") as f:
        columns = json.load(f)
    return model, columns

df = load_data()
model_lr, model_columns = load_model()

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", 
    ["🏠 Home", "🔮 Risk Predictor", "📊 Cluster Explorer", "🌎 Latam Insights", "ℹ️ About the Project"])

# ======================
# HOME PAGE
# ======================
if page == "🏠 Home":
    st.title("Welcome to Diabetes Risk Analyzer")
    st.markdown("### US BRFSS 2023 Analysis + Latin America Context")

    st.write("""
    This interactive dashboard explores diabetes risk factors using the **BRFSS 2023** survey (261,589 respondents) 
    and provides regional context from South & Central America using IDF and PAHO data.
    """)

    # Metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="US Diabetes Rate (BRFSS 2023)",
            value="14.6%",
            delta="Includes pre-diabetes + diabetes"
        )
    
    with col2:
        st.metric(
            label="Latin America Prevalence (2024)",
            value="10.1%"
        )
    
    with col3:
        st.metric(
            label="Latin America Projected 2050",
            value="11.5%",
            delta="+1.4 pp"
        )

    st.subheader("What You Can Explore")
    st.markdown("""
    - **🔮 Risk Predictor** — Estimate your personal diabetes risk  
    - **📊 Cluster Explorer** — Discover the 4 main population segments in the US  
    - **🌎 Latam Insights** — Trends and future projections for Latin America
    """)

# ======================
# RISK PREDICTOR PAGE - MODEL BASED
# ======================
elif page == "🔮 Risk Predictor":
    st.header("🔮 Individual Diabetes Risk Predictor")
    st.write("Fill in the patient information below to get a risk assessment.")

    col1, col2 = st.columns(2)

    with col1:
        age_group = st.selectbox("Age Group", 
            ["Young Adult (18-44)", "Middle Aged (45-59)", "Senior (60-74)", "Elderly (75+)"])
        bmi = st.slider("BMI", 15.0, 50.0, 28.0, step=0.1)
        genhlth = st.slider("General Health (1=Excellent — 5=Poor)", 1, 5, 3)
        highbp = st.radio("High Blood Pressure", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        highchol = st.radio("High Cholesterol", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

    with col2:
        physactivity = st.radio("Physically Active", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        comorbidity_count = st.slider("Number of Comorbidities", 0, 10, 2)
        income = st.slider("Income Level (1=Low — 8=High)", 1, 8, 4)
        sex = st.radio("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")

    if st.button("Predict Risk", type="primary"):
        # Base dict
        input_dict = {
            "bmi": bmi,
            "genhlth": genhlth,
            "highbp": highbp,
            "highchol": highchol,
            "physactivity": physactivity,
            "income": income,
            "comorbidity_count": comorbidity_count,
            "sex": sex,
            # engineered features default
            "diffwalk": 0,
            "diabetes_risk_score": 0,
            "lifestyle_score": 0,
            "obese_class_iii": 1 if bmi >= 40 else 0,
            "has_metabolic_risk": 1 if (highbp == 1 and bmi >= 30) else 0,
        }

        # Age group dummies (no senior_or_elderly)
        input_dict.update({
            "age_group_cat_Young Adult (18-44)": 1 if age_group == "Young Adult (18-44)" else 0,
            "age_group_cat_Middle Aged (45-59)": 1 if age_group == "Middle Aged (45-59)" else 0,
            "age_group_cat_Senior (60-74)": 1 if age_group in ["Senior (60-74)", "Elderly (75+)"] else 0,
        })

        # BMI categories
        input_dict.update({
            "bmi_category_Underweight": 1 if bmi < 18.5 else 0,
            "bmi_category_Overweight": 1 if 25 <= bmi < 30 else 0,
            "bmi_category_Obese Class I": 1 if 30 <= bmi < 35 else 0,
            "bmi_category_Obese Class II": 1 if 35 <= bmi < 40 else 0,
            "bmi_category_Obese Class III": 1 if bmi >= 40 else 0,
        })

        # Age + BMI risk group
        if age_group in ["Middle Aged (45-59)", "Senior (60-74)", "Elderly (75+)"] and bmi >= 30:
            input_dict["age_bmi_risk_group_Moderate Risk: Middle-age + Obese"] = 1
            input_dict["age_bmi_risk_group_Standard Risk"] = 0
        else:
            input_dict["age_bmi_risk_group_Moderate Risk: Middle-age + Obese"] = 0
            input_dict["age_bmi_risk_group_Standard Risk"] = 1

        # Build DataFrame aligned with model columns
        X_input = pd.DataFrame([[input_dict.get(col, 0) for col in model_columns]], columns=model_columns)

        # Predict probability
        probability = model_lr.predict_proba(X_input)[0][1] * 100

        # Elderly adjustment (since model groups them with Seniors)
        if age_group == "Elderly (75+)":
            probability = min(probability + 5, 100)

        # Risk level
        if probability > 50:
            risk_level = "High Risk"
        elif probability > 30:
            risk_level = "Moderate Risk"
        else:
            risk_level = "Low Risk"

        st.success("✅ Prediction Complete")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Estimated Diabetes Risk Probability", f"{probability:.1f}%")
        with col2:
            st.metric("Risk Level", risk_level)

        if probability > 70:
            st.error("⚠️ Very High Risk — Strong recommendation to consult a doctor")
        elif probability > 40:
            st.warning("⚠️ Moderate to High Risk — Consider medical evaluation")
        else:
            st.info("🟢 Low Risk — Maintain healthy lifestyle")



# ======================
# CLUSTER EXPLORER PAGE
# ======================
elif page == "📊 Cluster Explorer":
    st.header("📊 Cluster Explorer")
    st.markdown("**Population segmentation** based on health and demographic profiles from the BRFSS 2023 data.")

    # Cluster profiles with percentages
    cluster_data = pd.DataFrame({
        "Cluster": ["0: Low Risk", "1: Very High Risk", "2: High Risk", "3: Moderate Risk"],
        "Main Characteristics": [
            "Younger age, normal weight, good health, low comorbidities",
            "Older age, high BMI, hypertension, many comorbidities",
            "Middle-aged to older, obese, poor general health",
            "Older age, moderate BMI, some comorbidities"
        ],
        "Diabetes Prevalence (%)": [10.0, 64.0, 39.0, 26.0],
        "Share of Population (%)": [36.4, 25.2, 14.5, 23.9]
    })

    st.subheader("The 4 Population Segments")

    # Nice formatted table
    st.dataframe(
        cluster_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Diabetes Prevalence (%)": st.column_config.NumberColumn(format="%.1f%%"),
            "Share of Population (%)": st.column_config.NumberColumn(format="%.1f%%")
        }
    )

    # Bar chart - Diabetes Prevalence by Cluster
    fig = px.bar(
        cluster_data,
        x="Cluster",
        y="Diabetes Prevalence (%)",
        text="Diabetes Prevalence (%)",
        title="Diabetes Prevalence by Population Segment",
        color="Cluster",
        color_discrete_sequence=['#2ca02c', '#d62728', '#ff7f0e', '#1f77b4']
    )
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(
        yaxis_title="Diabetes Prevalence (%)",
        showlegend=False,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Key Insights")
    st.markdown("""
    - **Cluster 0 (Low Risk)** — 36.4% of the population: Mostly young and healthy individuals (lowest diabetes rate).
    - **Cluster 1 (Very High Risk)** — 25.2% of the population: The highest-risk group (64% diabetes rate).
    - **Cluster 2 (High Risk)** — 14.5% of the population: Obese individuals with poor self-reported health.
    - **Cluster 3 (Moderate Risk)** — 23.9% of the population: Older adults with moderate risk factors.

    These segments can help design **targeted prevention programs** for public health authorities and healthcare providers.
    """)

# ======================
# LATAM INSIGHTS PAGE
# ======================
elif page == "🌎 Latam Insights":
    st.header("🌎 Latam Insights")
    st.markdown("**Diabetes situation in South and Central America** (IDF & PAHO data)")

    # Key metrics from IDF South & Central America
    st.subheader("Key Statistics (South & Central America)")

    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

    with metrics_col1:
        st.metric("People with Diabetes (2024)", "35.4 million", "↑ from 25.1M in 2011")
    with metrics_col2:
        st.metric("Prevalence (20-79 years)", "10.1%", "↑ from 9.2% in 2011")
    with metrics_col3:
        st.metric("Projected 2050", "51.5 million", "45% increase")

    st.subheader("Trend in Diabetes Prevalence")

    # Trend data
    trend_data = pd.DataFrame({
        "Year": [2000, 2011, 2024, 2050],
        "Prevalence (%)": [3.7, 9.2, 10.1, 11.5]
    })

    fig_trend = px.line(
        trend_data,
        x="Year",
        y="Prevalence (%)",
        markers=True,
        title="Diabetes Prevalence Trend in South & Central America",
        line_shape="linear"
    )
    fig_trend.update_layout(yaxis_title="Prevalence (%)", height=450)
    st.plotly_chart(fig_trend, use_container_width=True)

    st.subheader("Main Takeaways for Latin America")
    st.markdown("""
    - Diabetes prevalence has **more than doubled** since 2000.
    - The number of people with diabetes is expected to rise from **35.4 million** in 2024 to **51.5 million** by 2050.
    - **Undiagnosed cases** and rising obesity are major concerns in the region.
    - Older adults and people with high BMI are the most affected groups — similar patterns seen in the US BRFSS clusters.

    **Recommendation**: Public health strategies should focus on prevention in middle-aged adults and early screening in high-risk clusters.
    """)

# ======================
# ABOUT THE PROJECT PAGE
# ======================
elif page == "ℹ️ About the Project":
    st.header("ℹ️ About the Project")

    st.markdown("""
    ### Project Goal
    This is my **third data analysis portfolio project**, created to demonstrate strong SQL skills, feature engineering, 
    unsupervised learning (clustering), and building an interactive Streamlit dashboard.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Data Sources")
        st.markdown("""
        - **BRFSS 2023** — 261,589 US respondents (main dataset)
        - **IDF Diabetes Atlas** — South & Central America estimates and 2050 projections
        - **PAHO** — Burden of disease and prevalence trends in the Americas
        """)

    with col2:
        st.subheader("Technical Stack")
        st.markdown("""
        - **SQL**: DuckDB (heavy usage for data prep and feature engineering)
        - **Modeling**: Logistic Regression (scikit-learn)
        - **Clustering**: K-Means (4 clusters)
        - **Frontend**: Streamlit + Plotly
        - **Data format**: Parquet for fast loading
        """)

    st.subheader("What I Focused On")
    st.markdown("""
    - Strong emphasis on **SQL** for data cleaning, feature engineering and aggregations
    - Handling class imbalance and moving from multi-class to binary classification
    - Creating meaningful population segments (clustering)
    - Building an intuitive and informative interactive dashboard
    - Combining US individual-level analysis with Latin America regional context
    """)

# ======================
# FOOTER 
# ======================
st.divider()

col1, col2, col3 = st.columns([2, 3, 2])

with col1:
    st.caption("**Diabetes Risk Analyzer**")

with col2:
    st.caption("Built using Python • DuckDB • Scikit-learn • Streamlit")

with col3:
    st.caption("Emilio Nahuel Pattini • Buenos Aires, Argentina • April 2026")