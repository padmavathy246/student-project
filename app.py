from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        study = float(request.form['study'])
        attendance = float(request.form['attendance'])
        marks = float(request.form['marks'])

        data = np.array([[study, attendance, marks]])
        prediction = model.predict(data)

        output = "Pass" if prediction[0] == 1 else "Fail"

        return render_template("index.html", prediction_text=output)
    except:
        return "Error occurred. Check input!"

if __name__ == "__main__":
    app.run(debug=True)