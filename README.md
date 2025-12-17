# 😊 Sentiment Analysis API (Machine Learning Project)

## 🔍 Project Overview

This project is a **Sentiment Analysis REST API** built with **Python**, **Natural Language Processing (NLP)**, and **Machine Learning**. It analyzes input text and predicts whether the sentiment is **Positive** or **Negative**.

The project demonstrates how to:

* Build and train an NLP model
* Expose machine learning functionality through a REST API
* Structure a clean and simple backend project

This repository is ideal for **junior developers**, **students**, and anyone interested in **ML-powered APIs**.

---

## 🚀 Features

* Text sentiment classification (Positive / Negative)
* REST API built with Flask
* Machine Learning model using TF-IDF and Logistic Regression
* Easy to run and extend

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NLP (TF-IDF)**

---

## 📂 Project Structure

```text
sentiment-analysis-api/
├── app.py            # Flask API entry point
├── model.py          # Sentiment analysis ML model
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Andreask9905/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## 🔗 API Usage

### Endpoint

```
POST /predict
```

### Request Body (JSON)

```json
{
  "text": "I really like this product"
}
```

### Response

```json
{
  "sentiment": "Positive"
}
```

---

## 📊 Model Description

The sentiment classifier uses:

* **TF-IDF Vectorization** for text feature extraction
* **Logistic Regression** for classification

The model is trained on sample labeled data and can be extended with larger datasets for improved accuracy.

---

## 📈 Possible Improvements

* Add support for **Neutral** sentiment
* Train on a larger real-world dataset
* Save and load trained models
* Add authentication
* Deploy online (Render, Railway, Hugging Face Spaces)

---

## 👨‍💻 Author

**Andreas K.**
Computer Science Student | Python & Machine Learning Enthusiast

🔗 GitHub: [https://github.com/Andreask9905](https://github.com/Andreask9905)

---

## 📄 License

This project is open-source and available for educational purposes.
