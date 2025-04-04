from flask import Flask, render_template, request
from app import detect_emotion  # Updated detect_emotion function import

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Form se input text lena
        text = request.form.get("text")

        # Emotion detect karna
        result = detect_emotion(text)

    # Result ko HTML mein pass karna
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
