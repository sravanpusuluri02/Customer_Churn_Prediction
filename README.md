# 🛒 Customer Churn Prediction Web Application

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-3.2-red)
![Render](https://img.shields.io/badge/Deployed-Render-purple)

> An end-to-end machine learning web application that predicts whether an e-commerce customer is likely to **churn or stay**, enabling businesses to launch targeted retention campaigns before losing the customer.

---

## 🌐 Live Demo
**👉 [Try the app here](https://customer-churn-prediction-anxp.onrender.com)**

> ⚠️ Hosted on Render free tier — may take 30-60 seconds to wake up on first load.

---

## 📊 EDA Report
**👉 [View full data analysis report](https://htmlpreview.github.io/?https://github.com/sravanpusuluri02/Customer_Churn_Prediction/blob/main/churn_report.html)**

---

## 🎯 Project Overview

E-commerce businesses lose significant revenue when customers churn. This project builds a machine learning model trained on real customer behavioral data to predict churn with **98.31% accuracy**, and deploys it as a live web application where business users can get instant predictions without any technical knowledge.

---

## 📈 Model Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 89.17% | 0.76 | 0.89 | 0.89 |
| Decision Tree | 96.36% | 0.96 | 0.98 | 0.96 |
| **Random Forest** ✅ | **98.31%** | **1.00** | **0.90** | **0.95** |
| XGBoost | 98.05% | 0.98 | 0.98 | 0.98 |

**Best Model: Random Forest** — correctly identifies 9 out of 10 customers about to churn.

---

## 🗂️ Project Structure
customer-churn-prediction/
├── churn_prediction.ipynb
├── app.py
├── churn_model.pkl
├── churn_report.html
├── E Commerce Dataset.xlsx
├── templates/
│   └── index.html
├── requirements.txt
└── Procfile

## ⚙️ Tech Stack

- **Python 3.12** — core language
- **Pandas & NumPy** — data manipulation
- **Scikit-learn** — ML models and evaluation
- **XGBoost** — gradient boosting
- **Matplotlib & Seaborn** — data visualization
- **ydata-profiling** — automated EDA
- **Flask** — web framework
- **Pickle** — model serialization
- **Git & GitHub** — version control
- **Render** — cloud deployment

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/sravanpusuluri02/Customer_Churn_Prediction.git

# 2. Navigate into the folder
cd Customer_Churn_Prediction

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate it
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the app
python app.py

# 7. Open in browser
http://127.0.0.1:5001
```

---

## 👨‍💻 Author

**Sravan Pusuluri**
- GitHub: [@sravanpusuluri02](https://github.com/sravanpusuluri02)