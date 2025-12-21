from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        return "<h2>Дякуємо! Ви додані до раннього доступу 🚀</h2>"

    return open("index.html", encoding="utf-8").read()

app.run(debug=True)
