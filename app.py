from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # print the user input data to console
    print(data)
    # build df
    df = pd.DataFrame([data])
    # print df to console
    print(df)
    # output df to web
    return jsonify(df["carbs"].values[0])
