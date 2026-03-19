import os
from flask import Flask, request, render_template
import pickle
import numpy as np

app=Flask(__name__)

with open('churn_model.pkl','rb') as f:
    model=pickle.load(f)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features=[
        int(request.form['tenure']),
        int(request.form['preferred_login_device']),
        int(request.form['city_tier']),
        float(request.form['warehouse_to_home']),
        int(request.form['preferred_payment_mode']),
        int(request.form['gender']),
        float(request.form['hour_spend_on_app']),
        int(request.form['number_of_device_registered']),
        int(request.form['prefered_order_cat']),
        int(request.form['satisfaction_score']),
        int(request.form['marital_status']),
        int(request.form['number_of_address']),
        int(request.form['complain']),
        float(request.form['order_amount_hike']),
        float(request.form['coupon_used']),
        float(request.form['order_count']),
        float(request.form['day_since_last_order']),
        float(request.form['cashback_amount'])
    ]
    
    prediction=model.predict([features])[0]
    
    if prediction==1:
        result="This customer is likely to CHURN! "
    else:
        result="This customer is likely to STAY! "
    
    return render_template('index.html',prediction=result)

if __name__=='__main__':
    port=int(os.environ.get('PORT',5001))
    app.run(debug=False,host='0.0.0.0', port=port)