from flask import Flask,render_template
import logging
logging.basicConfig(filemode="app.log", level= logging.INFO )

app = Flask("__main__")


@app.route('/')
def home():
   return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)