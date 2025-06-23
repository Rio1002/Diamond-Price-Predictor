# 💎 Diamond Price Predictor

This project develops a machine learning model to predict diamond prices based on key characteristics like carat, cut, color, and clarity. It aims to provide transparent and data-driven price estimations for buyers, sellers, and jewelers.

---

## ✨ Project Overview

Accurate diamond pricing is crucial. This tool addresses that need by predicting prices using various diamond attributes.

---

## 🚀 Features

- **💡 Intelligent Price Prediction**: Uses ML models for accurate diamond price estimation.  
- **🔍 Key Attribute Consideration**: Accounts for the "4 Cs" (Carat, Cut, Color, Clarity) plus dimensions, depth, and table.  
- **🖥️ User Interface (Conceptual)**: Designed to integrate with a simple web interface for ease of use.  
- **📈 Reliable Evaluation**: Assessed using standard metrics like MAE, RMSE, and R-squared.  

---

## 📊 Dataset Description

The model is trained on a comprehensive dataset of diamond attributes and their corresponding prices. Each entry in the dataset includes the following key features:

| Attribute   | Description |
|-------------|-------------|
| **carat**   | Weight of the diamond, measured in carats. This is a primary determinant of a diamond's value. |
| **cut**     | The quality of the diamond's cut, influencing its brilliance and fire. Categories range from *Fair* to *Ideal*, with *Ideal* representing the highest quality. |
| **color**   | The diamond's color grade, assessed on a scale from **J** (light yellow or brown tint) to **D** (colorless and rarest). |
| **clarity** | The clarity rating, which measures the absence of inclusions (internal flaws) and blemishes (external imperfections). Grades range from **I1** (Included) to **IF** (Internally Flawless). |
| **x, y, z** | The physical dimensions of the diamond in millimeters, representing its length (**x**), width (**y**), and depth (**z**). |
| **depth**   | The total depth percentage of the diamond, calculated as the ratio of the depth (**z**) to the average of length and width: **z / mean(x, y)**. This affects how light reflects within the stone. |
| **table**   | The width of the top flat facet (table) of the diamond relative to its widest point, expressed as a percentage. |
| **price**   | 🎯 **Target Variable**: The price of the diamond in US dollars. This is the value the machine learning model aims to predict. |

---

## 🧠 Model Development

The development process includes the following steps:

- **🔧 Data Preprocessing**: Handling missing values, feature engineering, categorical encoding, and feature scaling.  
- **📊 Model Selection**: Exploring models like Linear Regression, Random Forest, and Gradient Boosting.  
- **🏋️ Model Training**: Training the selected model on split data (training and testing sets).  
- **🧪 Model Evaluation**: Assessing performance using metrics such as MAE, RMSE, and R-squared.  

---

## 🛠️ Environment Setup & Usage

To run the project locally:

### ✅ Prerequisites

- Python 3.8+  
- `pip` package manager

### 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/Rio1002/Diamond-Price-Predictor.git
cd Diamond-Price-Predictor
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure `requirements.txt` lists all necessary dependencies.

### ▶️ Running the Application

```bash
python app.py
```

If a web interface is integrated, access the application at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🤝 Contributing

Contributions are welcome!
Please feel free to fork the repo, open issues, or submit pull requests.

---

⭐️ If you find this project useful, don’t forget to give it a star!

```
