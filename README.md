# Kantineprosjekt

Dette er et lite prosjekt jeg har laget med Flask. Det er en nettside for kantina som viser meny, varer og kontaktinformasjon. Jeg har brukt HTML og CSS til utseendet, og Flask til å vise sidene.

## Innhold

kantineprosjekt/
├── static/
│   ├── kantine.jpeg
│   ├── smoothie.jpeg
│   └── style.css
├── templates/
│   ├── base.html
│   ├── footer.html
│   ├── index.html
│   ├── kontakt.html
│   ├── meny.html
│   ├── navbar.html
│   └── varer.html
├── app.py
└── README.md

## Om prosjektet

Når man kjører app.py starter det en Flask-server som viser nettsiden.  
Hver HTML-fil er en del av siden:
- index.html er forsiden  
- meny.html viser maten i kantina  
- varer.html viser produkter  
- kontakt.html har kontaktinfo  
- navbar.html og footer.html er navigasjon og bunntekst  
- base.html er hovedmalen som alt bruker  
- style.css styrer designet  

## Hvordan starte prosjektet

1. Åpne prosjektet i terminal eller VS Code  
2. Installer Flask hvis du ikke har det:
   pip install flask  
3. Kjør prosjektet:
   python app.py  
4. Gå inn på:
   http://127.0.0.1:5000  

## Videre planer

Jeg kan senere legge til en database for meny og varer, gjøre designet mer responsivt og lage et enkelt adminpanel for å endre innholdet.

## Kort oppsummert

Et enkelt Flask-prosjekt som viser hvordan man kan lage en nettside med flere sider og en felles layout.
