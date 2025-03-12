import os
from flask import Flask, render_template, request, jsonify
from predictions import URLPrediction
from features_extraction import URLFeatureExtractor
from predictions import URLPrediction
from dotenv import load_dotenv

load_dotenv()

api_keys = {
    "whois": os.getenv("WHO_IS"),
    "ahrefs": os.getenv("AHREFS"),
    "opr": os.getenv("OPR"),
    "google": os.getenv("GOOGLE"),
    "cse_id": os.getenv("CSE_ID")
}


app = Flask(__name__)

# Dummy function simulating the URL classification script
def classify_url(url, api_keys):
    # Extract Features
    extractor = URLFeatureExtractor(api_keys=api_keys, url=url)
    features_df = extractor.extract_features()

    # Run Prediction
    url_predictor = URLPrediction()  # Create an instance of the class
    prediction = url_predictor.predict(features_df)  # Get the prediction

    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    
    result = classify_url(url, api_keys)  # Feed the URL to the script
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
