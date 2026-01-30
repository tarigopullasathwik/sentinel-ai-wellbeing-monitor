from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    mood = None
    if request.method == "POST":
        user_text = request.form["user_text"]
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            mood = "Happy <span class='emoji'>😊</span>"
        elif polarity < 0:
            mood = "Sad <span class='emoji'>😔</span>"
        else:
            mood = "Neutral <span class='emoji'>😐</span>"

    return render_template("index.html", mood=mood)

if __name__ == "__main__":
    app.run(debug=True)
