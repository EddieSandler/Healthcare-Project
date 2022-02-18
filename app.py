import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from cs50 import SQL
db = SQL("sqlite:///pricing.db")
# be sure to run export FLASK_APP=checkbox in terminal

app = Flask(__name__)
results = 0

# db.execute("""CREATE TABLE procedures (
#             hospital_id INTEGER,
#             hospital_Name text,
#             procedure_Code text,
#             Procedure_Name text,
#             Procedure_Price numeric,
#             FOREIGN KEY(hospital_id) REFERENCES hospitals(id)

#              )""")


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        option=request.form.getlist('myradio')


        if option[0] == "59400":
            print('You selected Delivery')
            results=db.execute("SELECT * FROM procedures WHERE procedure_Code='59400' ")

            return render_template("index.html",results=results,usd=usd)

            # return redirect("/")


        if option[0] == "55858":
            print('You selected Hysteroscopy')
            results=db.execute("SELECT * FROM procedures WHERE procedure_Code='58558' ")

            return render_template("index.html",results=results, usd=usd)

        if option[0] == "58100":

            results=db.execute("SELECT * FROM procedures WHERE procedure_Code='58100' ")
            return render_template("index.html",results=results, usd=usd)

        if option[0] == "76830":

            results=db.execute("SELECT * FROM procedures WHERE procedure_Code='76830' ")
            return render_template("index.html",results=results, usd=usd)

        if option[0] == "76818":

            results=db.execute("SELECT * FROM procedures WHERE procedure_Code='76818' ")
            return render_template("index.html",results=results,usd=usd)


    else:
       return render_template("index.html")









