# 📉 Customer Churn Prediction System in a Telecomunications Company
End-to-end machine learning solution to predict customer churn for a telecommunications company, featuring optimized modeling, API deployment, and an interactive business-facing web application.

**🌐Live APP:** _https://telco-customer-churn-prediction-krzfmpebgtschnu7fy6yrr.streamlit.app/_

**🚀 Project Overview**

Customer churn is a major challenge for telecom companies, directly impacting revenue and growth.
This project delivers a production-ready churn prediction system that enables businesses to proactively identify at-risk customers and take targeted retention actions.

The solution includes:

* A high-performance ML model optimized for recall

* A RESTful FastAPI service for scalable inference

* An interactive Streamlit app for non-technical stakeholders

**🧠 Key Highlights**
**Model:** XGBoost Classifier

**Optimization: **Optuna hyperparameter tuning

**Performance Gain:** Recall improved from **0.83 → 0.95**, maximizing recall to ensure most churn-prone customers are correctly identified.

**Deployment:** 

FastAPI backend for predictions

Streamlit frontend for business users

**Tech Stack:** Python, scikit-learn, pandas, XGBoost, Optuna, FastAPI, Streamlit

**📊 Problem Statement**

Telecom customers can leave at any time due to pricing, service quality, or competition.
The objective is to **predict whether a customer is likely to churn**, allowing the company to intervene before losing them.

**🧪 Machine Learning Pipeline**

**1️⃣ Data Processing**

* Cleaned and preprocessed structured customer data

* Encoded categorical variables

* Handled class imbalance

* Feature scaling where required

**2️⃣ Model Selection**

* Tested baseline classifiers

* Selected XGBoost for:

 * Strong performance on tabular data

 * Robust handling of non-linear relationships

**3️⃣ Hyperparameter Optimization**

* Used Optuna for automated tuning

* Optimized specifically for recall

* Resulted in a +12% recall improvement

**4️⃣ Model Evaluation**

* Evaluated using:

  * Recall (primary metric)

  * Precision

  * F1- score

  * Confusion Matrix

**🌐 Streamlit Application**

The Streamlit app allows business teams to:

* Enter customer details via a simple UI

* Instantly receive churn predictions

* Make data-driven retention decisions without ML knowledge

This bridges the gap between machine learning models and real business usage.

**🧩 FastAPI Service**

* Exposes a /predict endpoint

* Accepts JSON customer data

* Returns real-time churn predictions

**📈 Results**

* **Recall**- 0.95

* **Precision**-	High

* **F1-Score**-	Balanced

* **Business Impact**-	Early churn detection
  
Prioritizing recall ensures **fewer high-risk customers** are missed, maximizing retention opportunities.

**🛠️ How to Run Locally**

**Install dependencies**

_pip install -r requirements.txt_

**Run FastAPI**

_uvicorn api.main:app --reload_

**Run Streamlit App**

_streamlit run app/streamlit_app.py_


**👩‍💻 Author**

_Graduate AI / Machine Learning Engineer_

_Passionate about building production-ready ML systems that solve real business problems._
