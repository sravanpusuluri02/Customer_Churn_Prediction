# Customer Churn Prediction

## Live Demo
🌐 [Click here to try the app](https://customer-churn-prediction-anxp.onrender.com)

## Overview
A machine learning web application that predicts whether an e-commerce customer is likely to churn or stay, based on their behaviour and account details.

## Models Trained
| Model | Accuracy |
|-------|----------|
| Logistic Regression | 89.17% |
| Decision Tree | 96.36% |
| Random Forest | 98.31% |
| XGBoost | 98.05% |

## Best Model
Random Forest with 98.31% accuracy

## Tech Stack
- Python
- Pandas, Numpy
- Scikit-learn, XGBoost
- Flask
- HTML, CSS

## How to Run
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install libraries: `pip install -r requirements.txt`
5. Run the app: `python app.py`
6. Open browser at `https://customer-churn-prediction-anxp.onrender.com`

## Dataset
E-commerce customer dataset with 5,630 customers and 18 features.