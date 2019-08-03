import os
import base64

from flask import Flask, request, render_template
from model import Grade
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config["SECRET_KEY"] = os.urandom(32)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        g = Grade(
            student=request.form["student"],
            assignment=request.form["assignment"],
            grade=request.form["grade"],
        )
        # print("(" + request.form['grade'] + ")")
        g.save()

    results = [grade for grade in Grade.select().execute()]
    return render_template("template.jinja2", grades=results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6779))
    app.run(host="0.0.0.0", port=port)
