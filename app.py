from flask import Flask, render_template
app = Flask(__name__)

@app.route("/saurabh")
def hello():
    return render_template('./index.html')

app.run(debug=True)