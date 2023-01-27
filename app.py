from flask import Flask, redirect, url_for, render_template, request
from person import Person
from studentdebt import StudentDebt

app = Flask(__name__)


@app.route("/")
@app.route("/start-here")
def home():
    return render_template("index.html", content="Testing")


@app.route("/form1")
def form():
    return render_template("form1.html")


@app.route("/data/", methods=['POST', "GET"])
def data():
    if request.method == "GET":
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == "POST":
        form_data = request.form
        person = Person(float(form_data['Salary']))
        person.add_debt('Student debt', StudentDebt(float(form_data['Student debt'])))
        person.wipe_debt('Student debt')
        return render_template("data.html", form_data=form_data, person=person)


if __name__ == "__main__":
    app.run(debug=True)
