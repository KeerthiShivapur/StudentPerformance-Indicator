
# 🎓 Student Performance Prediction – ML End-to-End Project

This project predicts a student's **Math Score** based on features like gender, race/ethnicity, parental education, lunch type, test preparation, reading score, and writing score.

It includes:

✔ End-to-End Machine Learning Pipeline  
✔ Data Ingestion → Transformation → Model Training → Prediction  
✔ Flask Web App UI  
✔ Streamlit UI  
✔ Modular and production-ready project structure  
✔ Saved model + preprocessor for deployment  

---

# 📁 Project Structure
mlproject-main/
│
├── notebook/
│ └── data/stud.csv
│
├── artifacts/
│ ├── train.csv
│ ├── test.csv
│ ├── preprocessor.pkl
│ └── model.pkl
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline/
│ │ └── predict_pipeline.py
│ ├── utils.py
│ ├── logger.py
│ └── exception.py
│
├── templates/
│ ├── index.html
│ └── home.html
│
├── app.py # Flask App
├── app1.py # Streamlit App
├── requirements.txt
└── README.md
# 🚀 How to Run This Project

Make sure you have Python 3.8+ installed.

---

## 🔧 **1. Install Dependencies**

```bash
pip install -r requirements.txt
## 🌐 Running the Flask Web Application
python app.py
##You will see:
Running on http://127.0.0.1:5000
✔ Open the Website in Browser
🔹 Home Page :http://127.0.0.1:5000
🔹 Prediction Page : http://127.0.0.1:5000/predictdata
🎨 Running the Streamlit Application
streamlit run app1.py


🧠 Machine Learning Workflow

Data Ingestion: Load raw CSV → split train/test

Data Transformation:

Handle missing values

One-hot encode categorical features

Scale numerical features

Save preprocessor.pkl

Model Training:

Train multiple ML models

Choose best using R² Score

Save model.pkl

Prediction Pipeline:

Load model & preprocessor

Convert user input to DataFrame

Predict Math Score

