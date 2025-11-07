# Import all necessary libraries
from flask import Flask, render_template, request  # Flask web framework
import joblib       # for loading your saved ML model
import json         # for reading the locations file
import numpy as np  # for numerical operations (not heavily used here)
import pandas as pd # for creating DataFrame input to the model
import os           # for file path checking

# Initialize Flask app
app = Flask(__name__)

# -------------------------------------------
# Load the trained ML model (saved as .pkl)
# -------------------------------------------
# Make sure 'house_price_model.pkl' is in the same directory as this file
model = joblib.load("house_price_model.pkl")

# -------------------------------------------
# Load the list of locations (for dropdown menu)
# -------------------------------------------
# We previously saved this as a JSON file from our dataset
if os.path.exists("locations.json"):
    with open("locations.json", "r") as f:
        locations = json.load(f)  # Load the list of unique locations
else:
    locations = []  # Empty list fallback
    print("⚠️ Warning: 'locations.json' not found — dropdown will be empty.")

# -------------------------------------------
# Route 1: Home Page
# -------------------------------------------
# When a user visits '/', Flask will render 'index.html'
# and pass the locations list to populate the dropdown menu.
@app.route('/')
def home():
    return render_template("index.html", locations=locations)

# -------------------------------------------
# Route 2: Prediction
# -------------------------------------------
# When the user submits the form, the data is sent via POST request to '/predict'
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from the form
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    sqft = float(request.form['sqft'])
    
    # -------------------------------------------
    # Convert input values into a pandas DataFrame
    # -------------------------------------------
    # The model pipeline expects a DataFrame with these specific column names
    input_df = pd.DataFrame(
        [[location, sqft, bath, bhk]],
        columns=['location', 'total_sqft', 'bath', 'bhk']
    )
    
    # Make the price prediction using the model
    prediction = model.predict(input_df)[0]
    
    # -------------------------------------------
    # Render the same HTML page with the prediction result displayed
    # -------------------------------------------
    return render_template(
        "index.html",
        locations=locations,
        result=f"Predicted Price: ₹{round(prediction, 2)} Lakhs"
    )

# -------------------------------------------
# Run the Flask app
# -------------------------------------------
# debug=True enables live reload during development
if __name__ == "__main__":
    app.run(debug=True)
