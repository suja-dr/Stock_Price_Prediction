from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open(r'C:\Users\praveen\Downloads\Stock_Price_Prediction\model\Stock_Price_Prediction.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form['Company_Name']
        ticker = request.form['Ticker_Symbol']

        features = [
            float(request.form['day']),
            float(request.form['month']),
            float(request.form['year']),
            float(request.form['Open']),
            float(request.form['High']),
            float(request.form['Low']),
            float(request.form['Volume'])
        ]

        input_array = np.array([features])

        prediction = model.predict(input_array)[0]

        return render_template('result.html',
                               prediction=round(prediction, 2),
                               company=company,
                               ticker=ticker)

    except KeyError as e:
        return f"Missing input: {e}", 400
    except Exception as e:
        return f"Error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
