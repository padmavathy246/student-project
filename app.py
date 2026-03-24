from flask import Flask, render_template, request
import pickle
import numpy as np

# Create app
app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    amount = float(request.form['amount'])
    time = float(request.form['time'])

    # Prediction
    prediction = model.predict([[amount, time]])

    if prediction[0] == -1:
        result = "⚠️ Fraud Detected"
    else:
        result = "✅ Normal Transaction"

    return render_template('index.html', prediction_text=result)

# Run app
if __name__ == "__main__":
    app.run(debug=True)