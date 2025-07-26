import streamlit as st

st.set_page_config(page_title="Multi-Disease Prediction Chatbot", layout="centered")

# Sidebar navigation
st.sidebar.title("Choose a Disease to Predict")
page = st.sidebar.radio("Go to", ["Home", "Hypertension", "Cardiovascular Disease", "Type 2 Diabetes"])

# ---------- Home Page ----------
if page == "Home":
    st.title("🩺 Multi-Disease Prediction Chatbot")
    st.markdown("""
        Welcome to the Clinical Disease Prediction Chatbot.

        Use the sidebar to select a disease:
        - Hypertension
        - Cardiovascular Disease
        - Type 2 Diabetes
    """)

# ---------- Hypertension ----------
elif page == "Hypertension":
    st.title("💢 Hypertension Prediction")

    age = st.number_input("Age", 10, 100)
    salt = st.selectbox("Salt Intake", ["Low", "Normal", "High"])
    stress = st.slider("Stress Score", 1, 10)
    bp_history = st.selectbox("Blood Pressure History", ["Yes", "No"])
    sleep = st.number_input("Sleep Duration (hours)", 1.0, 15.0)
    bmi = st.number_input("BMI", 10.0, 50.0)
    medication = st.selectbox("Medication", ["Yes", "No"])
    family = st.selectbox("Family History", ["Yes", "No"])
    exercise = st.selectbox("Exercise Level", ["Low", "Moderate", "High"])
    smoking = st.selectbox("Smoking Status", ["Smoker", "Non-Smoker"])

    if st.button("Predict Hypertension"):
        st.success("🔮 Prediction: You may have LOW risk of Hypertension.")
        # Later you will connect to model and show result here

# ---------- Cardiovascular Disease ----------
elif page == "Cardiovascular Disease":
    st.title("❤️ Cardiovascular Disease Prediction")

    age = st.slider("Age", 10, 100)
    bmi = st.number_input("BMI", 10.0, 50.0)
    bp = st.selectbox("High Blood Pressure", ["Yes", "No"])
    chol = st.selectbox("High Cholesterol", ["Yes", "No"])
    activity = st.selectbox("Physical Activity", ["Yes", "No"])
    fruit = st.selectbox("Fruits Intake", ["Yes", "No"])
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    diffwalk = st.selectbox("Difficulty Walking", ["Yes", "No"])

    if st.button("Predict Cardiovascular Disease"):
        st.success("🔮 Prediction: Medium risk of Cardiovascular Disease.")

# ---------- Type 2 Diabetes ----------
elif page == "Type 2 Diabetes":
    st.title("🍩 Type 2 Diabetes Prediction")

    age = st.slider("Age", 10, 100)
    bmi = st.number_input("BMI", 10.0, 50.0)
    bp = st.selectbox("High Blood Pressure", ["Yes", "No"])
    chol = st.selectbox("High Cholesterol", ["Yes", "No"])
    physical = st.selectbox("Physically Active", ["Yes", "No"])
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    alcohol = st.selectbox("Heavy Alcohol Consumption", ["Yes", "No"])
    genhlth = st.slider("General Health (1=Excellent, 5=Poor)", 1, 5)
    stroke = st.selectbox("History of Stroke", ["Yes", "No"])

    if st.button("Predict Diabetes"):
        st.success("🔮 Prediction: You may have HIGH risk of Type 2 Diabetes.")
