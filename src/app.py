from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)


def load_model(model_path):
    model = joblib.load(model_path)
    return model


model_path = "../models/best_model.joblib"
model = load_model(model_path)


def preprocess_input(inputs):
    # Convert inputs into a DataFrame and preprocess accordingly
    input_data = pd.DataFrame(inputs, index=[0])

    # Perform any necessary preprocessing steps here (e.g., encoding categorical variables)

    return input_data


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inputs = request.form.to_dict()
        input_data = preprocess_input(inputs)
        prediction = model.predict(input_data)
        optimized_price = np.round(prediction[0], 2)
        return render_template("index.html", optimized_price=optimized_price)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)


def load_model(model_path):
    model = joblib.load(model_path)
    return model


model_path = "../models/best_model.joblib"
model = load_model(model_path)


def preprocess_input(inputs):
    input_data = pd.DataFrame(inputs, index=[0])

    # Perform any necessary preprocessing steps here (e.g., encoding categorical variables)

    return input_data


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        inputs = request.form.to_dict()
        input_data = preprocess_input(inputs)
        prediction = model.predict(input_data)
        optimized_price = np.round(prediction[0], 2)
        return render_template("index.html", optimized_price=optimized_price)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
