import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Health Risk Checker",
    page_icon="❤️",
    layout="wide"
)

# Title
st.title("❤️ AI Health Risk Checker")
st.write("Analyze your health and lifestyle factors to get a general health-risk assessment.")

st.warning(
    "This application is for educational purposes only and is not a medical diagnostic tool."
)

# Sidebar
st.sidebar.header("Personal Information")

age = st.sidebar.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

# Main health information
st.header("🩺 Health Information")

col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=165.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=10.0,
        max_value=250.0,
        value=60.0
    )

    systolic_bp = st.number_input(
        "Systolic Blood Pressure",
        min_value=70,
        max_value=250,
        value=120
    )

    glucose = st.number_input(
        "Glucose Level",
        min_value=50,
        max_value=400,
        value=100
    )

with col2:
    sleep = st.slider(
        "Sleep Hours per Day",
        min_value=0.0,
        max_value=15.0,
        value=7.0
    )

    exercise = st.slider(
        "Exercise Hours per Week",
        min_value=0.0,
        max_value=20.0,
        value=3.0
    )

    water = st.slider(
        "Water Intake (Litres/Day)",
        min_value=0.0,
        max_value=8.0,
        value=2.0
    )

    stress = st.slider(
        "Stress Level",
        min_value=1,
        max_value=10,
        value=5
    )

smoking = st.selectbox(
    "Smoking",
    ["No", "Occasionally", "Regularly"]
)

alcohol = st.selectbox(
    "Alcohol Consumption",
    ["No", "Occasionally", "Regularly"]
)

# BMI calculation
if height > 0:
    bmi = weight / ((height / 100) ** 2)
else:
    bmi = 0

st.header("📊 Health Information")

metric1, metric2, metric3 = st.columns(3)

metric1.metric("BMI", f"{bmi:.1f}")
metric2.metric("Age", age)
metric3.metric("Blood Pressure", f"{systolic_bp} mmHg")

# BMI category
if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

st.info(f"**BMI Category:** {bmi_category}")

# Assessment button
if st.button("🔍 Check My Health Risk", use_container_width=True):

    # Temporary health score
    score = 100

    if bmi < 18.5 or bmi >= 30:
        score -= 15
    elif bmi >= 25:
        score -= 8

    if systolic_bp >= 140:
        score -= 20
    elif systolic_bp >= 130:
        score -= 10

    if glucose >= 126:
        score -= 20
    elif glucose >= 100:
        score -= 10

    if sleep < 6:
        score -= 10

    if exercise < 2:
        score -= 10

    if water < 1.5:
        score -= 5

    if stress >= 8:
        score -= 10

    if smoking == "Regularly":
        score -= 10
    elif smoking == "Occasionally":
        score -= 5

    if alcohol == "Regularly":
        score -= 5

    score = max(0, score)

    risk_percentage = 100 - score

    if score >= 75:
        risk_level = "Low Risk"
    elif score >= 50:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    st.success("Health assessment completed!")

    result1, result2, result3 = st.columns(3)

    result1.metric(
        "Health Score",
        f"{score}/100"
    )

    result2.metric(
        "Risk Percentage",
        f"{risk_percentage}%"
    )

    result3.metric(
        "Risk Level",
        risk_level
    )

    st.subheader("💡 Recommendations")

    recommendations = []

    if bmi >= 25:
        recommendations.append("Focus on a balanced diet and regular physical activity.")

    if bmi < 18.5:
        recommendations.append("Consider a nutritious calorie-rich diet and consult a professional if needed.")

    if systolic_bp >= 130:
        recommendations.append("Monitor your blood pressure regularly and reduce excessive salt intake.")

    if glucose >= 100:
        recommendations.append("Pay attention to your sugar intake and maintain regular physical activity.")

    if sleep < 7:
        recommendations.append("Try to maintain a consistent sleep schedule and aim for adequate sleep.")

    if exercise < 3:
        recommendations.append("Try to include regular physical activity during the week.")

    if water < 2:
        recommendations.append("Increase your daily water intake according to your personal needs.")

    if stress >= 7:
        recommendations.append("Consider relaxation activities such as walking, meditation, or breathing exercises.")

    if smoking != "No":
        recommendations.append("Reducing or avoiding smoking can improve overall health.")

    if alcohol != "No":
        recommendations.append("Limiting alcohol consumption can support better health.")

    if not recommendations:
        recommendations.append("Continue maintaining your current healthy lifestyle.")

    for recommendation in recommendations:
        st.write("•", recommendation)
