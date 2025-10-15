🌟 Multi Disease Prediction Using Machine Learning
📌 Overview

The Multi Disease Prediction System is a machine learning project designed to predict multiple diseases using different ML and Deep Learning models. The system supports structured/tabular medical data as well as image-based diagnosis. It focuses on early prediction to assist patients and healthcare professionals.

The diseases included in this version are:

✅ Heart Disease

✅ Diabetes

✅ Breast Cancer

✅ Kidney Disease

✅ Liver Disease

✅ Pneumonia (Image-based)

✅ Malaria (Image-based)

🎯 Objective

The main objective of this project is to build an integrated prediction platform where multiple diseases can be analyzed using separate ML models with high accuracy. Instead of building different apps for each disease, this system combines them into one.

⚙️ Technologies Used

Programming Language

Python

Frameworks/Libraries

Flask (for deployment)

Scikit-learn

TensorFlow / Keras

Pandas

NumPy

Matplotlib

OpenCV

PIL

Frontend

HTML

CSS

Bootstrap

Database

SQLite / MySQL (for login & registration)

Tools

Jupyter Notebook

VS Code / PyCharm

Anaconda

🧠 Models Used
Disease	Dataset Type	Algorithms Used
Heart Disease	Tabular	Logistic Regression, SVM, Random Forest
Diabetes	Tabular	KNN, Decision Tree, Logistic Regression
Breast Cancer	Tabular	SVM, Random Forest, Naive Bayes
Kidney Disease	Tabular	Logistic Regression, SVM
Liver Disease	Tabular	Random Forest, Decision Tree
Pneumonia	Image	CNN / Transfer Learning
Malaria	Image	CNN / VGG16

Models were trained separately and saved using .pkl or .h5 formats.

📂 Project Structure (Suggested Layout)
Multi-Disease-Prediction-ML/
│
├── models/
│   ├── heart.pkl
│   ├── diabetes.pkl
│   ├── breast_cancer.pkl
│   ├── kidney.pkl
│   ├── liver.pkl
│   ├── pneumonia.h5
│   └── malaria.h5
│
├── notebooks/
│   ├── heart_model.ipynb
│   ├── diabetes_model.ipynb
│   ├── liver_model.ipynb
│   └── ...
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── heart.html
│   └── ...
│
├── app.py
├── requirements.txt
└── README.md

🔍 Features

✅ Multiple Disease Prediction in One Platform
✅ Tabular & Image-Based Disease Support
✅ Flask-based Web Interface
✅ User Login & Registration
✅ Probability-based Outputs
✅ Modular and Scalable Design
✅ Real-time Input Handling
