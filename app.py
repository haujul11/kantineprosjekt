from flask import Flask, render_template, url_for

app = Flask(__name__)

ukesmeny = {
    "Mandag": [
        {"navn": "Tomatsuppe", "beskrivelse": "Serveres med makaroni og brød", "pris": 35},
        {"navn": "Pasta bolognese", "beskrivelse": "Med kjøttsaus og revet parmesan", "pris": 49}
    ],
    "Tirsdag": [
        {"navn": "Kyllingwrap", "beskrivelse": "Med salat og dressing", "pris": 45}
    ],
    "Onsdag": [
        {"navn": "Taco-tallerken", "beskrivelse": "Kjøttdeig, bønner og salsa", "pris": 55}
    ],
    "Torsdag": [
        {"navn": "Fiskekaker", "beskrivelse": "Serveres med potetmos og gulrøtter", "pris": 49}
    ],
    "Fredag": [
        {"navn": "Pizza-slice", "beskrivelse": "Med ost og skinke", "pris": 35},
        {"navn": "Burger", "beskrivelse": "150g burger med ost og salat", "pris": 59}
    ]
}

varer = [
    {"navn": "Bagett med ost og skinke", "pris": 35},
    {"navn": "Smoothie", "pris": 30},
    {"navn": "Kaffe", "pris": 15},
    {"navn": "Kanelbolle", "pris": 25}
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
        "adresse": "Pilestredet 1, 0981 Oslo"
    }
    return render_template("kontakt.html", kontakt=kontaktinfo)

if __name__ == "__main__":
    app.run(debug=True)
