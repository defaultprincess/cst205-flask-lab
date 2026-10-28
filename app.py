# Could not ask two other classmates, so I added placeholders :(

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

acronyms = [
    ("Vanessa", "FOMO", "Fear of Missing Out"),
    ("Classmate Two", "IMO", "In My Opinion"),
    ("Classmate Three", "TBH", "To Be Honest"),
]


@app.route("/")
def home():
    html = ""
    for name, acronym, meaning in acronyms:
        html += f"<p>{name}: {acronym} ({meaning})</p>\n"
    return html


@app.route("/athena")
def athena():
    my_acronym = "LMFAO (Laughing My Fucking Ass off)"
    return render_template("template.html", acronym=my_acronym)


@app.route("/photo")
def photo():
    return render_template("photo.html")


if __name__ == "__main__":
    app.run(debug=True)
