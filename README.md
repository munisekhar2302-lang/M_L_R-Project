# 🎓 Student Performance Prediction Using Multiple Linear Regression

## 📌 Project Overview

This project predicts a student's Performance Index using Multiple Linear Regression Machine Learning techniques. The model analyzes various academic and lifestyle factors such as study hours, previous scores, extracurricular activities, sleep hours, and practice papers to estimate student performance accurately.

The project is developed using Python, Machine Learning, Object-Oriented Programming (OOP), and deployed as a web application using Render.

---

## 🚀 Features

* Predicts student performance using Multiple Linear Regression.
* Object-Oriented Programming (OOP) implementation.
* Data preprocessing and feature engineering.
* Model evaluation using R² Score and RMSE.
* Model persistence using Pickle.
* Interactive frontend for user input.
* Backend prediction API.
* Cloud deployment using Render.
* Public web access for end users.

---

## 📊 Dataset Information

The dataset was obtained from Kaggle and contains the following features:

| Feature                          | Description                                 |
| -------------------------------- | ------------------------------------------- |
| Hours Studied                    | Number of hours studied per day             |
| Previous Scores                  | Student's previous academic scores          |
| Extracurricular Activities       | Participation in extracurricular activities |
| Sleep Hours                      | Average sleep hours                         |
| Sample Question Papers Practiced | Number of sample papers practiced           |
| Performance Index                | Target variable                             |

---

## 🔧 Data Preprocessing

Before training the model:

1. Dataset loaded using Pandas.
2. Missing values checked.
3. Categorical values converted into numerical format.
4. Extracurricular Activities encoded as:

* Yes = 1
* No = 0

5. Independent and dependent variables separated.

---

## 🤖 Machine Learning Model

This project uses Multiple Linear Regression.

Model Equation:

y = b₀ + b₁x₁ + b₂x₂ + b₃x₃ + b₄x₄ + b₅x₅

Where:

* y = Performance Index
* x₁ = Hours Studied
* x₂ = Previous Scores
* x₃ = Extracurricular Activities
* x₄ = Sleep Hours
* x₅ = Sample Question Papers Practiced

---

## 🏗️ OOP Architecture

The entire project is designed using Object-Oriented Programming concepts.

### Constructor (**init**)

The constructor performs:

* Dataset loading
* Feature selection
* Target variable selection
* Train-test splitting

### Training Method

* Trains Multiple Linear Regression model
* Learns relationships between features and target

### Prediction Method

* Generates predictions for training and testing datasets

### Evaluation Method

Calculates:

* R² Score
* Root Mean Squared Error (RMSE)

### Save Model Method

Stores the trained model using Pickle.

### Load Model Method

Loads the saved model and performs predictions on new data.

---

## 📈 Model Evaluation

Performance metrics used:

### R² Score

Measures how well the model explains the variation in student performance.

### RMSE

Measures prediction error between actual and predicted values.

Lower RMSE indicates better model performance.

---

## 📊 Visualization

Matplotlib was used to visualize:

* Actual values
* Predicted values
* Model fitting performance

This helps understand how closely the predictions match real-world data.

---

## 💾 Model Serialization

The trained model is saved using Pickle.

Benefits:

* Faster deployment
* No need for retraining
* Easy model reuse

Functions used:

* pickle.dump()
* pickle.load()

---

## 🌐 Web Application Development

After training the model:

### Backend

Developed using Python.

Responsibilities:

* Load trained model
* Accept user input
* Generate predictions
* Return prediction results

### Frontend

Created using HTML and CSS.

Features:

* User-friendly interface
* Student data input fields
* Prediction output display

---

## ☁️ Deployment Process

Deployment Steps:

1. Complete model development.
2. Save trained model using Pickle.
3. Create frontend and backend files.
4. Create Procfile.
5. Upload project to GitHub repository.
6. Connect GitHub repository to Render.
7. Deploy application on Render.
8. Generate public URL for users.

The deployed application allows users to predict student performance directly through a web browser.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Pickle
* HTML
* CSS
* Git
* GitHub
* Render

---

## 🎯 Project Outcome

The model successfully predicts student performance using academic and lifestyle factors. The project demonstrates:

* Data preprocessing
* Feature engineering
* Machine Learning model development
* Object-Oriented Programming
* Model serialization
* Web development
* Cloud deployment

This project showcases end-to-end Machine Learning development from data preprocessing to production deployment.

---

## 👨‍💻 Developed By

M. Munisekhar

Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer

This project was independently designed, developed, trained, tested, and deployed as a complete end-to-end Machine Learning solution.
