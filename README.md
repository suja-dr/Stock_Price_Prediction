# 📈 Stock Price Prediction

A web-based machine learning application to predict stock prices using historical financial data. This project integrates a trained ML model with a Flask-powered front-end and includes a dynamic Power BI dashboard for detailed visual analytics.


## 🔍 Project Overview

This project predicts the stock price based on inputs like company name, ticker symbol, date, and market features such as open, high, low, and volume prices. Users interact with the app through a clean web interface, and the backend uses a `.pkl` model for inference. A Power BI dashboard helps visualize stock trends, volatility, and performance.


## 🛠️ Technologies Used

- **Python** (Flask, Pandas, Pickle)
- **HTML, CSS** (for frontend styling)
- **Power BI** (for analytics dashboard)
- **Machine Learning**: Trained model stored as `Stock_Price_Prediction.pkl`


## 📁 Project Structure
Stock_Price_Prediction/
│

├── dataset/

│ └── EW-MAX.csv # Dataset used for training/visualization

│

├── model/
│ └── Stock_Price_Prediction.pkl # Trained machine learning model
│
├── templates/
│ ├── index.html # Input form for user
│ └── result.html # Result display page
│
├── app.py # Flask web application
├── Stock_Price_Prediction.ipynb # Google colab (model training)
└── README.md # Project documentation

## 🧪 Input Fields
            -->Company Name
            -->Ticker Symbol
            -->Day / Month / Year (Date)
            -->Open Price
            -->High Price
            -->Low Price
            -->Volume
**Output:** Displays the predicted stock price based on user inputs.

