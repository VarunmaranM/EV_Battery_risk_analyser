import streamlit as st
import pandas as pd
import joblib

# Load the trained model and label encoder
# Make sure 'battery_risk_model.pkl' and 'label_encoder.pkl' are in the same folder
try:
    model = joblib.load('battery_risk_model.pkl')
    le = joblib.load('label_encoder.pkl')
except FileNotFoundError:
    st.error("Model files not found. Please run the `train.py` script first.")
    st.stop()


# --- Streamlit App Interface ---
st.set_page_config(layout="wide")
st.title('🔋 Interactive EV Battery Risk Analyzer')
st.write("Use the sliders and input fields in the sidebar to enter the battery's metrics and get an instant risk prediction.")

# --- Sidebar for User Input ---
st.sidebar.header('Input Battery Metrics')

def user_input_features():
    """Creates sidebar widgets and returns a DataFrame of the inputs."""
    temperature = st.sidebar.slider('Temperature (°C)', -10.0, 65.0, 35.0, 0.5)
    voltage = st.sidebar.slider('Voltage (V)', 3.00, 4.50, 3.90, 0.01)
    current = st.sidebar.slider('Current (A)', -15.0, 40.0, 15.0, 0.5)
    charge_cycles = st.sidebar.number_input('Charge Cycles', min_value=0, max_value=2000, value=450)
    health_score = st.sidebar.slider('State of Health (SoH %)', 0, 100, 92)

    data = {
        'temperature': temperature,
        'voltage': voltage,
        'current': current,
        'charge_cycles': charge_cycles,
        'health_score': health_score
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# --- Main Panel for Displaying Results ---
col1, col2 = st.columns([1, 1.5])

# Display user input
with col1:
    st.header("Current Metrics")
    st.dataframe(input_df.style.format("{:.2f}"))

# Make and display prediction
with col2:
    st.header("Prediction")
    
    # Predict using the loaded model
    prediction_encoded = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    # Decode the prediction
    prediction = le.inverse_transform(prediction_encoded)[0]

    # Display the result with color and an icon
    if prediction == 'High':
        st.error(f'Predicted Risk Level: **{prediction}** 🚨')
        st.warning("Immediate attention required. Check for overheating, cell imbalance, or critical degradation.")
    elif prediction == 'Medium':
        st.warning(f'Predicted Risk Level: **{prediction}** ⚠️')
        st.info("Monitor the battery closely. Performance may be degraded; consider scheduling a check-up.")
    else:
        st.success(f'Predicted Risk Level: **{prediction}** ✅')
        st.info("Battery is operating under normal and safe conditions.")

    # Display prediction probabilities
    st.write("### Confidence Score")
    proba_df = pd.DataFrame(prediction_proba, columns=le.classes_, index=['Probability'])
    st.dataframe(proba_df.style.format("{:.2%}"))