
from flask import Flask, render_template, url_for

app = Flask(__name__)


ukesmeny = {
    "Mandag": [
        {"navn": "Tomatsuppe", "beskrivelse": "Med makaroni og brød", "pris": 35},
        {"navn": "Pasta bolognese", "beskrivelse": "Riv parmesan", "pris": 49},
    ],
    "Tirsdag": [
        {"navn": "Kyllingwrap", "beskrivelse": "Salat + dressing", "pris": 45},
    ],
    "Onsdag": [
        {"navn": "Taco-tallerken", "beskrivelse": "Kjøttdeig/bønner, salsa", "pris": 55},
    ],
    "Torsdag": [
        {"navn": "Fiskekaker", "beskrivelse": "Potetmos og gulrøtter", "pris": 49},
    ],
    "Fredag": [
        {"navn": "Pizza-slice", "beskrivelse": "Ost & skinke", "pris": 35},
        {"navn": "Burger", "beskrivelse": "150g, ost", "pris": 59},
    ],
}

varer = [
    {"navn": "Bagett ost & skinke", "pris": 35},
    {"navn": "Smoothie", "pris": 30},
    {"navn": "Kaffe", "pris": 15},
    {"navn": "Kanelbolle", "pris": 25},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    return render_template("meny.html", ukesmeny=ukesmeny)

@app.route("/varer")
def varer_side():
    return render_template("varer.html", varer=varer)

@app.route("/kontakt")
def kontakt():
    kontaktinfo = {
        "telefon": "92 11 17 44",
        "epost": "julian@akademiet.no",
        "adresse": "pilestredet 1, 0981 Oslo"
    }
    return render_template("kontakt.html", kontakt=kontaktinfo)

if __name__ == "__main__":
    app.run(debug=True)
