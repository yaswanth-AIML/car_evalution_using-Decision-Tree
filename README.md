# car_evalution_using-Decision-Tree
# 🚗 Car Evaluation Prediction App

A Machine Learning web application that predicts the evaluation of a car (unacceptable, acceptable, good, very good) based on user inputs such as buying price, maintenance cost, safety, and more.

---

## 🔥 Project Overview

This project uses a **Decision Tree Classifier** to classify cars into different categories based on multiple features. The model is trained on the Car Evaluation dataset and deployed using Streamlit.

---

## ⚙️ Features

* Predict car evaluation in real-time
* Interactive user interface using Streamlit
* Decision Tree model for interpretable predictions
* Deployed as a web application

---

## 🧠 Machine Learning Workflow

1. Data Preprocessing

   * Converted categorical features into numerical values using ordinal encoding

2. Model Training

   * Used DecisionTreeClassifier with entropy criterion

3. Model Optimization

   * Tuned model using depth variation and pruning (ccp_alpha)
   * Selected model based on best generalization performance

4. Evaluation

   * Accuracy, confusion matrix, and classification report

5. Deployment

   * Model saved using pickle
   * Frontend built using Streamlit
   * Hosted on Render

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---
## 🌐 Live Demo
https://car-evalution-using-decision-tree.onrender.com
---

## 📂 Project Structure

```
app.py                  # Streamlit frontend
decisio_tree_car_classifier.pkl   # Trained model
requirements.txt        # Dependencies
Procfile               # Deployment config
runtime.txt            # Python version
.gitignore             # Ignore unnecessary files
```

---

## 🧪 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 🎯 Key Learning Outcomes

* Understanding Decision Tree algorithm (Entropy & Information Gain)
* Handling categorical data using encoding techniques
* Model evaluation and overfitting control
* Deploying ML models using Streamlit and Render

---

## 👨‍💻 Author

**Yaswanth Vanacharla**

---
