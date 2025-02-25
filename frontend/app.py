import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

# Set MODEL_PATH to use the shared volume
MODEL_PATH = os.environ.get("MODEL_PATH", "/shared/model.pkl")

def load_model():
    """Loads the recommendation model from disk and validates it."""
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        
        if isinstance(model, pd.DataFrame) and not model.empty:
            print(f"✅ Model loaded with {len(model)} rows")
            return model
        else:
            print("⚠️ Model is empty or incorrect format!")
            return None
    except Exception as e:
        print("❌ Error loading model:", e)
        return None

# Load the model at startup
app.model = load_model()

@app.route("/")
def home():
    """Serve the web-based frontend."""
    return render_template("index.html")

@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json(force=True)
    input_songs = data.get("songs", [])
    
    if app.model is None or app.model.empty:
        return jsonify({"error": "Model not loaded or empty"}), 500

    recommendations = set()
    
    for song in input_songs:
        matching_rules = app.model[app.model["antecedents"].apply(lambda x: song in x)]
        for _, row in matching_rules.iterrows():
            recommendations.update(row["consequents"])
    
    rec_list = list(recommendations)

    if len(rec_list) < 3:
        all_recs = set()
        for _, row in app.model.iterrows():
            all_recs.update(row["consequents"])
        supplement = list(all_recs - recommendations)
        needed = 3 - len(rec_list)
        rec_list.extend(supplement[:needed])

    rec_list = rec_list[:10]

    response = {
        "songs": rec_list,
        "version": "0.1",
        "model_date": "2025-02-22"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=52002, debug=True)
