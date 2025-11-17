import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page settings
st.set_page_config(page_title="Student Performance Predictor", page_icon="📘", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4e73df;'>🎓 Student Performance Predictor</h1>
    <p style='text-align: center;'>Predict the math score of a student based on various input features.</p>
""", unsafe_allow_html=True)

# UI Card
with st.container():
    st.markdown("<h3>Enter Student Details</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["male", "female"])
        ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])

    with col2:
        parental_level_of_education = st.selectbox(
            "Parental Level of Education",
            ["high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
        )
        test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
        writing_score = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

# Predict button
if st.button("Predict Math Score"):
    try:
        # Create input data object
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score,
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_data_frame()

        # Prediction pipeline
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        st.success(f"📊 Predicted Math Score: **{result[0]:.2f}**")

    except Exception as e:
        st.error(f"❌ Error: {e}")
