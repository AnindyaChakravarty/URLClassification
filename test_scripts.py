from features_extraction import URLFeatureExtractor
from predictions import URLPrediction
import os
from dotenv import load_dotenv

load_dotenv()

api_keys = {
    "whois": os.getenv("WHO_IS"),
    "ahrefs": os.getenv("AHREFS"),
    "opr": os.getenv("OPR"),
    "google": os.getenv("GOOGLE"),
    "cse_id": os.getenv("CSE_ID")
}


url = "https://chriswayg.gitbook.io/opencore-visual-beginners-guide/alternatives/usb-mapping-on-windows"

# Extract Features

extractor = URLFeatureExtractor(api_keys=api_keys, url=url)
features_df = extractor.extract_features()

# Run Prediction

url_predictor = URLPrediction()  # Create an instance of the class
prediction = url_predictor.predict(features_df)  # Get the prediction

if prediction == 1:
    print("URL is Phishing!")
elif prediction == 0:
    print("URL is Benign!")
else:
    print("Error in prediction")

