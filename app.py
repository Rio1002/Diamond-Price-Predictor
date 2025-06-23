from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Constants
EXCHANGE_RATE = 83

# Load the model and preprocessor
model_path = "artifacts/model.pkl"
preprocessor_path = "artifacts/preprocessor.pkl"

model = pickle.load(open(model_path, "rb"))
preprocessor = pickle.load(open(preprocessor_path, "rb"))

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Collect data from the form
        data = {
            "carat": float(request.form.get('carat')),
            "depth": float(request.form.get('depth')),
            "table": float(request.form.get('table')),
            "x": float(request.form.get('x')),
            "y": float(request.form.get('y')),
            "z": float(request.form.get('z')),
            "cut": request.form.get('cut'),
            "color": request.form.get('color'),
            "clarity": request.form.get('clarity')
        }

        # Convert data to DataFrame
        input_df = pd.DataFrame([data])

        # Preprocess the data
        transformed_data = preprocessor.transform(input_df)

        # Predict the result
        pred = model.predict(transformed_data)
        result = round(pred[0], 2)

        # Convert result to INR
        final_result = round(result * EXCHANGE_RATE, 2)

        # Determine background color and image based on the result
        if final_result <= 951 * EXCHANGE_RATE:
            bg_color = "red"
            image_path = "images/red-icon.jpg"
        elif final_result > 951 * EXCHANGE_RATE and final_result <= 2401 * EXCHANGE_RATE:
            bg_color = "green"
            image_path = "images/green-icon.jpg"
        elif final_result > 2401 * EXCHANGE_RATE and final_result <= 5408 * EXCHANGE_RATE:
            bg_color = "blue"
            image_path = "images/blue-icon.jpg"
        else:
            bg_color = "grey"
            image_path = "images/grey-icon.jpg"

        # Render the result page
        return render_template(
            "result.html",
            final_result=final_result,
            bg_color=bg_color,
            image_path=image_path
        )

if __name__ == '__main__':
    app.run(debug=True)
