# 🔋 EV Battery Risk Analyzer

This project uses a machine learning model to predict a battery's risk level ('Low', 'Medium', or 'High') based on real-time sensor data. The interactive web app is built with Streamlit.

---

## 🛠️ Setup Instructions

**1. Create a Virtual Environment (Recommended)**
It's best to create a dedicated environment for this project.

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**2. Install Dependencies**
Install the required libraries from the `requirements.txt` file in this folder.
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

Follow these steps in order from within the `battery_risk` directory.

**1. Generate Sample Data (Run once)**
This script creates the `battery_data.csv` file used for training.
```bash
python generate_data.py
```

**2. Train the Model (Run once)**
This script trains the classifier and saves it as `battery_risk_model.pkl`.
```bash
python train.py
```

**3. Launch the Application**
Start the interactive Streamlit dashboard.
```bash
python -m streamlit run app.py
```