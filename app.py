from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/home")
def start_page():
    return render_template("index.html")


@app.route("/potential")
def potential():
    return render_template("potential.html")


@app.route("/thermal_energy")
def thermal_energy():
    return render_template("thermal_energy.html")


@app.route("/transport")
def transport():
    return render_template("transport.html")


if __name__=='__main__':
    app.run(debug=True)






