from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/",methods=['POST','GET'])
def index():
    return render_template("home_1.html")

@app.route("/about_car",methods=['POST','GET'])
def about_car():
    return render_template("about_car.html")

@app.route("/about_races",methods=['POST','GET'])
def about_races():
    return render_template("about_races.html")

@app.route("/aboutus",methods=['POST','GET'])
def aboutus():
    return render_template("aboutus.html")

@app.route("/select_continent",methods=['POST','GET'])
def select_continent():
    return render_template("select_continent.html")

@app.route("/usa",methods=['POST','GET'])
def usa():
    return render_template("usa.html")

@app.route("/europe",methods=['POST','GET'])
def europe():
    return render_template("europe.html")

@app.route("/austria",methods=['POST','GET'])
def austria():
    return render_template("austria.html")

@app.route("/france",methods=['POST','GET'])
def france():
    return render_template("france.html")

@app.route("/germany",methods=['POST','GET'])
def germany():
    return render_template("germany.html")

@app.route("/italy",methods=['POST','GET'])
def italy():
    return render_template("italy.html")

@app.route("/uk",methods=['POST','GET'])
def uk():
    return render_template("uk.html")

@app.route("/asia_pacific",methods=['POST','GET'])
def asia_pacific():
    return render_template("asia_pacific.html")

@app.route("/japan",methods=['POST','GET'])
def japan():
    return render_template("japan.html")

@app.route("/korea",methods=['POST','GET'])
def korea():
    return render_template("korea.html")

@app.route("/ford",methods=['POST','GET'])
def ford():
    return render_template("ford.html")

@app.route("/cheverolet",methods=['POST','GET'])
def cheverolet():
    return render_template("cheverolet.html")

@app.route("/pontiac",methods=['POST','GET'])
def pontiac():
    return render_template("pontiac.html")

@app.route("/shelby",methods=['POST','GET'])
def shelby():
    return render_template("shelby.html")

@app.route("/dodge",methods=['POST','GET'])
def dodge():
    return render_template("dodge.html")

@app.route("/tesla",methods=['POST','GET'])
def tesla():
    return render_template("tesla.html")

@app.route("/ktm",methods=['POST','GET'])
def ktm():
    return render_template("ktm.html")

@app.route("/citroen",methods=['POST','GET'])
def citroen():
    return render_template("citroen.html")

@app.route("/renault_sport",methods=['POST','GET'])
def renault_sport():
    return render_template("renault_sport.html")

@app.route("/peugeot",methods=['POST','GET'])
def peugeot():
    return render_template("peugeot.html")

@app.route("/alpine",methods=['POST','GET'])
def alpine():
    return render_template("alpine.html")

@app.route("/bugatti",methods=['POST','GET'])
def bugatti():
    return render_template("bugatti.html")

@app.route("/volkswagen",methods=['POST','GET'])
def volkswagen():
    return render_template("volkswagen.html")

@app.route("/benz",methods=['POST','GET'])
def benz():
    return render_template("benz.html")

@app.route("/bmw",methods=['POST','GET'])
def bmw():
    return render_template("bmw.html")

@app.route("/audi",methods=['POST','GET'])
def audi():
    return render_template("audi.html")

@app.route("/mini",methods=['POST','GET'])
def mini():
    return render_template("mini.html")

@app.route("/porsche",methods=['POST','GET'])
def porsche():
    return render_template("porsche.html")

@app.route("/ruf",methods=['POST','GET'])
def ruf():
    return render_template("ruf.html")

@app.route("/alfa_romeo",methods=['POST','GET'])
def alfa_romeo():
    return render_template("alfa_romeo.html")

@app.route("/ferrari",methods=['POST','GET'])
def ferrari():
    return render_template("ferrari.html")

@app.route("/lamborghini",methods=['POST','GET'])
def lamborghini():
    return render_template("lamborghini.html")

@app.route("/abarth",methods=['POST','GET'])
def abarth():
    return render_template("abarth.html")

@app.route("/detomaso",methods=['POST','GET'])
def detomaso():
    return render_template("detomaso.html")

@app.route("/fiat",methods=['POST','GET'])
def fiat():
    return render_template("fiat.html")

@app.route("/maserati",methods=['POST','GET'])
def maserati():
    return render_template("maserati.html")

@app.route("/lancia",methods=['POST','GET'])
def lancia():
    return render_template("lancia.html")

@app.route("/pagani",methods=['POST','GET'])
def pagani():
    return render_template("pagani.html")

@app.route("/jaguar",methods=['POST','GET'])
def jaguar():
    return render_template("jaguar.html")

@app.route("/aston_martin",methods=['POST','GET'])
def aston_martin():
    return render_template("aston_martin.html")

@app.route("/mclaren",methods=['POST','GET'])
def mclaren():
    return render_template("mclaren.html")

@app.route("/toyota",methods=['POST','GET'])
def toyota():
    return render_template("toyota.html")

@app.route("/nissan",methods=['POST','GET'])
def nissan():
    return render_template("nissan.html")

@app.route("/honda",methods=['POST','GET'])
def honda():
    return render_template("honda.html")

@app.route("/mazda",methods=['POST','GET'])
def mazda():
    return render_template("mazda.html")

@app.route("/subaru",methods=['POST','GET'])
def subaru():
    return render_template("subaru.html")

@app.route("/mitsubishi",methods=['POST','GET'])
def mitsubishi():
    return render_template("mitsubishi.html")

@app.route("/daihatsu",methods=['POST','GET'])
def daihatsu():
    return render_template("daihatsu.html")

@app.route("/lexus",methods=['POST','GET'])
def lexus():
    return render_template("lexus.html")

@app.route("/suzuki",methods=['POST','GET'])
def suzuki():
    return render_template("suzuki.html")

@app.route("/hyundai",methods=['POST','GET'])
def hyundai():
    return render_template("hyundai.html")



