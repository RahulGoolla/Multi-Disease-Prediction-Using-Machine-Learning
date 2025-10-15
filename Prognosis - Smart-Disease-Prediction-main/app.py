cd ..
from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

init_db()

# Load Models
def load_pickle_model(path):
    try:
        return pickle.load(open(path, 'rb'))
    except Exception as e:
        print(f"Error loading model from {path}:\n{e}")
        return None

heart_model = load_pickle_model(r'C:\Users\Acer\OneDrive\Desktop\My Projects\Prognosis - Smart-Disease-Prediction-main\notebooks\heart_disease_model.sav')
diabetes_model = load_pickle_model(r'C:\Users\Acer\OneDrive\Desktop\My Projects\Prognosis - Smart-Disease-Prediction-main\notebooks\diabetes_model.sav')
kidney_model = load_pickle_model(r'C:\Users\Acer\OneDrive\Desktop\My Projects\Prognosis - Smart-Disease-Prediction-main\notebooks\kidney_model.sav')
liver_model = load_pickle_model(r'C:\Users\Acer\OneDrive\Desktop\My Projects\Prognosis - Smart-Disease-Prediction-main\notebooks\liver_model.sav')
parkinsons_model = load_pickle_model(r'C:\Users\Acer\OneDrive\Desktop\My Projects\Prognosis - Smart-Disease-Prediction-main\notebooks\parkinsons_model.sav')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (uname, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            conn.close()
            return render_template('register.html', error="Username already exists.")
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user'] = uname
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials!'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    result = advice = None
    if request.method == 'POST' and heart_model:
        features = [float(request.form[key]) for key in request.form]
        prediction = heart_model.predict([features])[0]
        if prediction == 1:
            result = "Heart Disease Detected"
            advice = "Consult a cardiologist and maintain a healthy lifestyle."
        else:
            result = "No Heart Disease"
            advice = "Maintain regular checkups and a heart-healthy lifestyle."
    return render_template('heart.html', result=result, advice=advice)

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    result = advice = None
    if request.method == 'POST' and diabetes_model:
        features = [float(request.form[key]) for key in request.form]
        prediction = diabetes_model.predict([features])[0]
        if prediction == 1:
            result = "Diabetic"
            advice = "Monitor blood sugar regularly, maintain a healthy diet, and consult your doctor."
        else:
            result = "Not Diabetic"
            advice = "Maintain a healthy lifestyle to prevent diabetes."
    return render_template('diabetes.html', result=result, advice=advice)

@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    result = advice = None
    if request.method == 'POST' and parkinsons_model:
        features = [float(request.form[key]) for key in request.form]
        prediction = parkinsons_model.predict([features])[0]
        if prediction == 1:
            result = "Parkinson's Disease Detected"
            advice = "Please consult a neurologist for further evaluation and treatment."
        else:
            result = "No Parkinson's Disease"
            advice = "Stay healthy and continue regular monitoring."
    return render_template('parkinsons.html', result=result, advice=advice)

@app.route('/kidney', methods=['GET', 'POST'])
def kidney():
    result = advice = None
    if request.method == 'POST' and kidney_model:
        features = []
        for key in request.form:
            val = request.form[key]
            try:
                features.append(float(val) if val.lower() not in ['yes', 'no'] else (1.0 if val.lower() == 'yes' else 0.0))
            except:
                features.append(0.0)
        prediction = kidney_model.predict([features])[0]
        if prediction == 1:
            result = "Chronic Kidney Disease"
            advice = "Consult a nephrologist and manage your health actively."
        else:
            result = "No Kidney Disease"
            advice = "Keep up the good health practices."
    return render_template('kidney.html', result=result, advice=advice)

@app.route('/liver', methods=['GET', 'POST'])
def liver():
    result = advice = None
    if request.method == 'POST' and liver_model:
        features = []
        for key in request.form:
            val = request.form[key]
            try:
                features.append(float(val) if val not in ['Male', 'Female'] else (1.0 if val == 'Male' else 0.0))
            except:
                features.append(0.0)
        prediction = liver_model.predict([features])[0]
        if prediction == 1:
            result = "Liver Disease Detected"
            advice = "Avoid alcohol, follow liver-friendly practices, and consult a specialist."
        else:
            result = "No Liver Disease"
            advice = "Continue with a healthy lifestyle."
    return render_template('liver.html', result=result, advice=advice)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
