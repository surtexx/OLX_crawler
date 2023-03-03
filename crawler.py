from flask import Flask, render_template
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/start/')
def my_link():
  # fac un request la site sa imi dea codu html, returneaza un obiect raspuns
  url = urllib2.urlopen("https://www.olx.ro/d/anunturi-agricole")

  # din raspuns generez codu html
  soup = BeautifulSoup(url, "html.parser")

  # face codu html frumos
  soup.prettify()

  nr_cereale, nr_fan, nr_porumb, nr_grau, nr_orez, nr_other_cereale = 0, 0, 0, 0, 0, 0

  nr_flori, nr_trandafiri, nr_panselute, nr_lavande, nr_ornamentale, nr_other_plante = 0, 0, 0, 0, 0, 0

  nr_utilajeagricole, nr_tractoare, nr_combine, nr_anvelope, nr_remorci = 0, 0, 0, 0, 0
  nr_motostivuitoare, nr_cositoare, nr_semanatoare, nr_other_utilaje = 0, 0, 0, 0

  nr_produseanimale, nr_lapte, nr_oua, nr_carne, nr_other_produseanimale = 0, 0, 0, 0, 0

  nr_fructe, nr_mere, nr_pere, nr_capsuni, nr_cirese, nr_other_fructe = 0, 0, 0, 0, 0, 0

  nr_legume, nr_rosii, nr_ardei, nr_castraveti, nr_morcovi, nr_other_legume = 0, 0, 0, 0, 0, 0

  nr_produsealimentare, nr_cafea, nr_dulceata, nr_nuci, nr_ulei, nr_other_produsealimentare = 0, 0, 0, 0, 0, 0

  nr_animale, nr_cai, nr_capre, nr_iepuri, nr_oi, nr_vaci, nr_gaini, nr_other_animale = 0, 0, 0, 0, 0, 0, 0, 0

  nr_echipamente, nr_tarcuri, nr_canistre, nr_racitoare, nr_stupi, nr_cantar, nr_colivii, nr_cuibare, nr_other_echipamente = 0, 0, 0, 0, 0, 0, 0, 0, 0

  nr_pomi, nr_meri, nr_peri, nr_ciresi, nr_visini, nr_gutui, nr_other_pomi = 0, 0, 0, 0, 0, 0, 0

  nr_seminte, nr_floarea_soarelui, nr_lucerna, nr_s_porumb, nr_dovleac, nr_fasole, nr_other_seminte = 0, 0, 0, 0, 0, 0, 0

  dimensiune200, dimensiune300, dimensiune400, dimensiunemore = 0, 0, 0, 0
  # caut in ultimul buton link-ul care contine parametrii page = numar
  linkpagini = soup.find_all('a', class_='css-1mi714g', href=True)[-1]['href']

  # scot numaru paginii din link
  nrpagini = int(linkpagini[linkpagini.index("=") + 1:])
  for pagina in range(1, nrpagini + 1):
    # fac un request la site sa imi dea codu html, returneaza un obiect raspuns
    url = urllib2.urlopen(f"https://www.olx.ro/d/anunturi-agricole/?page={pagina}")

    # din raspuns generez codu html
    soup = BeautifulSoup(url, "html.parser")

    # fac codu frumos
    soup.prettify()

    # textu din anunturi e scris cu h6, deci ma uit in toate <h6> urile din html
    for anunt in soup.find_all('h6'):
      if re.search(r"(semin[tț]e)|(s[aă]m[aâ]n[tț][aă])", str(anunt), re.IGNORECASE):
        nr_seminte += 1
        if re.search(r"floarea[ -]soarelui", str(anunt), re.IGNORECASE):
          nr_floarea_soarelui += 1
        if re.search(r"lucern[aă]", str(anunt), re.IGNORECASE):
          nr_lucerna += 1
        if re.search(r"poru[nm]b", str(anunt), re.IGNORECASE):
          nr_s_porumb += 1
        if re.search(r"dovleac", str(anunt), re.IGNORECASE):
          nr_dovleac += 1
        if re.search(r"fasole", str(anunt), re.IGNORECASE):
          nr_fasole += 1
        else:
          nr_other_seminte += 1
      if re.search(r"f[aâ]n", str(anunt), re.IGNORECASE):
        nr_fan += 1
        nr_cereale += 1
      if re.search(r"poru[mn]b", str(anunt), re.IGNORECASE):
        nr_porumb += 1
        nr_cereale += 1
      if re.search(r"gr[aâ]u", str(anunt), re.IGNORECASE):
        nr_grau += 1
        nr_cereale += 1
      if re.search(r"orez", str(anunt), re.IGNORECASE):
        nr_orez += 1
        nr_cereale += 1
      if re.search(r"secar[aă]", str(anunt), re.IGNORECASE) or re.search(r"ov[aă]z", str(anunt),
                                                                         re.IGNORECASE) or re.search(r"quinoa",
                                                                                                     str(anunt),
                                                                                                     re.IGNORECASE):
        nr_other_cereale += 1
        nr_cereale += 1
      if re.search(r"trandafiri?", str(anunt), re.IGNORECASE):
        nr_trandafiri += 1
        nr_flori += 1
      if re.search(r"panselu[tț][eè]", str(anunt), re.IGNORECASE):
        nr_panselute += 1
        nr_flori += 1
      if re.search(r"lavand[aă]|lev[aă]n[tț]ic[aă]", str(anunt), re.IGNORECASE):
        nr_lavande += 1
        nr_flori += 1
      if re.search(r"plante(le)? ornamentale", str(anunt), re.IGNORECASE):
        nr_ornamentale += 1
        nr_flori += 1
      if re.search(r"orhide[ei]", str(anunt), re.IGNORECASE) or re.search(r"petuni[iea]?", str(anunt),
                                                                          re.IGNORECASE) or re.search(r"lale((le)|a)",
                                                                                                      str(anunt),
                                                                                                      re.IGNORECASE):
        nr_other_plante += 1
        nr_flori += 1
      if re.search(r"(anvelope)|(cauciucuri)|(ro[tț]i)", str(anunt), re.IGNORECASE):
        nr_anvelope += 1
        nr_utilajeagricole += 1
        dimensiune = re.search(r"\d\d\d\/(?=\d\d)", str(anunt), re.IGNORECASE)
        if dimensiune:
            dimensiune = int(dimensiune.group(0)[:-1])
            if dimensiune < 200:
                dimensiune200 += 1
            elif dimensiune < 300:
                dimensiune300 += 1
            elif dimensiune400 < 400:
                dimensiune400 += 1
            else:
                dimensiunemore += 1
      if re.search(r"tractor", str(anunt), re.IGNORECASE):
        nr_tractoare += 1
        nr_utilajeagricole += 1
      if re.search(r"co[mn]bin[aă]", str(anunt), re.IGNORECASE):
        nr_combine += 1
        nr_utilajeagricole += 1
      if re.search(r"remorc[aăi]", str(anunt), re.IGNORECASE):
        nr_remorci += 1
        nr_utilajeagricole += 1
      if re.search(r"motostivuitor", str(anunt), re.IGNORECASE):
        nr_motostivuitoare += 1
        nr_utilajeagricole += 1
      if re.search(r"cositoare", str(anunt), re.IGNORECASE):
        nr_cositoare += 1
        nr_utilajeagricole += 1
      if re.search(r"sem[aă]n[aă]toare", str(anunt), re.IGNORECASE):
        nr_semanatoare += 1
        nr_utilajeagricole += 1
      if re.search(r"grebl[aăe]", str(anunt), re.IGNORECASE) or re.search(r"rulmen(t|[tț]i)", str(anunt),
                                                                          re.IGNORECASE) or (
              re.search(r"pomp[aă]", str(anunt), re.IGNORECASE) and re.search(r"alimentare", str(anunt),
                                                                              re.IGNORECASE)):
        nr_other_utilaje += 1
        nr_utilajeagricole += 1
      if re.search(r"lapte", str(anunt), re.IGNORECASE):
        nr_lapte += 1
        nr_produseanimale += 1
      if re.search(r"\bou[aă]?\b", str(anunt), re.IGNORECASE):
        nr_oua += 1
        nr_produseanimale += 1
      if re.search(r"carne", str(anunt), re.IGNORECASE):
        nr_carne += 1
        nr_produseanimale += 1
      if re.search(r"miere", str(anunt), re.IGNORECASE) or re.search(r"br[aâ]nz[aă]", str(anunt), re.IGNORECASE):
        nr_other_produseanimale += 1
        nr_produseanimale += 1
      if re.search(r"mere", str(anunt), re.IGNORECASE):
        nr_mere += 1
        nr_fructe += 1
      if re.search(r"pere", str(anunt), re.IGNORECASE):
        nr_pere += 1
        nr_fructe += 1
      if re.search(r"c[aă]p[sș]un[ie]", str(anunt), re.IGNORECASE):
        nr_capsuni += 1
        nr_fructe += 1
      if re.search(r"cire[sș]e", str(anunt), re.IGNORECASE):
        nr_cirese += 1
        nr_fructe += 1
      if re.search(r"fruct(ul)? pasiunii?", str(anunt), re.IGNORECASE) or re.search(r"goji", str(anunt),
                                                                                    re.IGNORECASE):
        nr_other_fructe += 1
        nr_fructe += 1
      if re.search(r"ro[sș]ii?", str(anunt), re.IGNORECASE):
        nr_rosii += 1
        nr_legume += 1
      if re.search(r"ardei", str(anunt), re.IGNORECASE):
        nr_ardei += 1
        nr_legume += 1
      if re.search(r"(castrave[tț]i)|(castraveciori)", str(anunt), re.IGNORECASE):
        nr_castraveti += 1
        nr_legume += 1
      if re.search(r"morcovi?", str(anunt), re.IGNORECASE):
        nr_morcovi += 1
        nr_legume += 1
      if re.search(r"ceap[aă]", str(anunt), re.IGNORECASE) or re.search(r"salat[aăe]", str(anunt),
                                                                        re.IGNORECASE) or re.search(
        r"(vinete)|(v[aâ]n[aă]t[aă])", str(anunt), re.IGNORECASE):
        nr_other_legume += 1
        nr_legume += 1
      if re.search(r"cafea", str(anunt), re.IGNORECASE):
        nr_cafea += 1
        nr_produsealimentare += 1
      if re.search(r"(dulcea[tț][aă])|(dulce[tț]uri)", str(anunt), re.IGNORECASE):
        nr_dulceata += 1
        nr_produsealimentare += 1
      if re.search(r"nuci", str(anunt), re.IGNORECASE):
        nr_nuci += 1
        nr_produsealimentare += 1
      if re.search(r"ulei", str(anunt), re.IGNORECASE):
        nr_ulei += 1
        nr_produsealimentare += 1
      if re.search(r"suc", str(anunt), re.IGNORECASE) or re.search(r"sirop(uri)?", str(anunt),
                                                                   re.IGNORECASE) or re.search(r"[sș]erbet",
                                                                                               str(anunt),
                                                                                               re.IGNORECASE):
        nr_other_produsealimentare += 1
        nr_produsealimentare += 1
      if re.search(r"( ca[li])|(ca[li] )", str(anunt), re.IGNORECASE):
        nr_cai += 1
        nr_animale += 1
      if re.search(r"capr[aăe]", str(anunt), re.IGNORECASE):
        nr_capre += 1
        nr_animale += 1
      if re.search(r"iepur([ie]|a[sș]i?)", str(anunt), re.IGNORECASE):
        nr_iepuri += 1
        nr_animale += 1
      if re.search(r"\b(oi([tț][aăe]?)?)\b|\b(oaie)\b", str(anunt), re.IGNORECASE):
        nr_oi += 1
        nr_animale += 1
      if re.search(r"(vac[aăi])|(v[aă]cu[tț][aă])", str(anunt), re.IGNORECASE):
        nr_vaci += 1
        nr_animale += 1
      if re.search(r"g[aă]in[aăi]", str(anunt), re.IGNORECASE):
        nr_gaini += 1
        nr_animale += 1
      if re.search(r"porumbe[li]", str(anunt), re.IGNORECASE) or re.search(r"albine", str(anunt),
                                                                           re.IGNORECASE) or re.search(r"melci?",
                                                                                                       str(anunt),
                                                                                                       re.IGNORECASE):
        nr_other_animale += 1
        nr_animale += 1
      if re.search(r"[tț]arc", str(anunt), re.IGNORECASE):
        nr_tarcuri += 1
        nr_echipamente += 1
      if re.search(r"canistr[aăe]", str(anunt), re.IGNORECASE):
        nr_canistre += 1
        nr_echipamente += 1
      if re.search(r"r[aă]citoare", str(anunt), re.IGNORECASE):
        nr_racitoare += 1
        nr_echipamente += 1
      if re.search(r"stupi?", str(anunt), re.IGNORECASE):
        nr_stupi += 1
        nr_echipamente += 1
      if re.search(r"c[aâ]ntar", str(anunt), re.IGNORECASE) and re.search(r"animale?", str(anunt), re.IGNORECASE):
        nr_cantar += 1
        nr_echipamente += 1
      if re.search(r"colivi[ie]?", str(anunt), re.IGNORECASE):
        nr_colivii += 1
        nr_echipamente += 1
      if re.search(r"cuibare?", str(anunt), re.IGNORECASE):
        nr_cuibare += 1
        nr_echipamente += 1
      if (re.search(r"colector", str(anunt), re.IGNORECASE) and re.search(r"polen", str(anunt), re.IGNORECASE)) or (
              re.search(r"ma[sș]in[aă]", str(anunt), re.IGNORECASE) and re.search(r"tuns", str(anunt), re.IGNORECASE)):
        nr_other_echipamente += 1
        nr_echipamente += 1
      if re.search(r"(m[aă]r)|(meri)", str(anunt), re.IGNORECASE):
        nr_meri += 1
        nr_pomi += 1
      if re.search(r"(p[aă]r)|(peri)", str(anunt), re.IGNORECASE):
        nr_peri += 1
        nr_pomi += 1
      if re.search(r"cire[sș]i?", str(anunt), re.IGNORECASE):
        nr_ciresi += 1
        nr_pomi += 1
      if re.search(r"vi[sș]ini?", str(anunt), re.IGNORECASE):
        nr_visini += 1
        nr_pomi += 1
      if re.search(r"gutui", str(anunt), re.IGNORECASE):
        nr_gutui += 1
        nr_pomi += 1
      if re.search(r"pruni?", str(anunt), re.IGNORECASE) or re.search(r"l[aă]m[aâ]i", str(anunt),
                                                                      re.IGNORECASE) or re.search(r"cai(s|[sș]i)",
                                                                                                  str(anunt),
                                                                                                  re.IGNORECASE) or re.search(
        r"piersici?", str(anunt), re.IGNORECASE):
        nr_other_pomi += 1
        nr_pomi += 1

  print(f"{dimensiune200}\n{dimensiune300}\n{dimensiune400}\n{dimensiunemore}")
  return f"""<!DOCTYPE html>

<html>

<head>
    <link rel="stylesheet" href="../static/style.css">
</head>


<body>

    <a href="/start/">
        <button class="cybr-btn">
            Start Crawler<span aria-hidden>_</span>
            <span aria-hidden class="cybr-btn__glitch">Start Crawler</span>
        </button>
    </a>


    <div class="box">
        <div class="divCategorie" id="cereale">
            <h1>Cereale: {nr_cereale}</h1>

            <div id="furaje"> Furaje, Fan: {nr_fan}</div>
            <div id="porumb"> Porumb: {nr_porumb} </div>
            <div id="grau"> Grau: {nr_grau}</div>
            <div id="orez"> Orez: {nr_orez}</div>
            <div id="othersCereale"> Others: {nr_other_cereale} </div>
        </div>

        <div class="divCategorie" id="plante">
            <h1>Plante: {nr_flori}</h1>
            <div id="trandafiri"> Trandafiri: {nr_trandafiri}</div>
            <div id="pasnelute"> Panselute: {nr_panselute} </div>
            <div id="lavanda"> Lavanda: {nr_lavande} </div>
            <div id="plante_ornamentale"> Plante ornamentale: {nr_ornamentale} </div>
            <div id="othersPlante"> Others: {nr_other_plante} </div>
        </div>


        <div class="divCategorie" id="pomi">
            <h1>Pomi: {nr_pomi}</h1>

            <div id="mar"> Mar: {nr_meri} </div>
            <div id="par"> Par: {nr_peri} </div>
            <div id="cires"> Cires: {nr_ciresi} </div>
            <div id="visin"> Visin: {nr_visini} </div>
            <div id="gutui"> Gutui: {nr_gutui} </div>
            <div id="othersPomi"> Others: {nr_other_pomi} </div>
        </div>


        <div class="divCategorie" id="seminte">
            <h1>Seminte: {nr_seminte}</h1>
            <div id="flaorea_soarelui"> Floarea Soarelui: {nr_floarea_soarelui} </div>
            <div id="lucerna"> Lucerna: {nr_lucerna} </div>
            <div id="porumb"> Porumb: {nr_s_porumb} </div>
            <div id="dovleac"> Dovleac: {nr_dovleac} </div>
            <div id="fasole"> Fasole: {nr_fasole} </div>
            <div id="othersSeminte"> Others: {nr_other_legume} </div>

        </div>


        <div class="divCategorie" id="utilaje">
            <h1>Utilaje agricole si industriale: {nr_utilajeagricole} </h1>
            <div id="tractoare"> Tractoare: {nr_tractoare} </div>
            <div id="combine"> Combine: {nr_combine} </div>
            <div id="remorci"> Remorci: {nr_remorci} </div>
            <div id="motostivuitoare"> Motostivuitoare: {nr_motostivuitoare} </div>
            <div id="cositoare"> Cositoare: {nr_cositoare} </div>
            <div id="semanatoare"> Semanatoare: {nr_semanatoare} </div>
            <div id="anvelope"> Anvelope: {nr_anvelope} </div>
            <div id="othersUtilaje"> Others: {nr_other_utilaje} </div>

        </div>

        <div class="divCategorie" id="produse_animale">
            <h1>Produse Animale: {nr_produseanimale} </h1>
            <div id="lapte"> Lapte: {nr_lapte} </div>
            <div id="oua"> Oua: {nr_oua} </div>
            <div id="carne"> Carne: {nr_carne} </div>
            <div id="othersAnimale"> Others: {nr_other_produseanimale} </div>


        </div>


        <div class="divCategorie" id="fructe">
            <h1>Fructe: {nr_fructe} </h1>
            <div id="mere"> Mere: {nr_mere} </div>
            <div id="pere"> Pere: {nr_pere} </div>
            <div id="capsune"> Capsune: {nr_capsuni} </div>
            <div id="cirese"> Cirese: {nr_cirese} </div>
            <div id="othersFructe"> Others: {nr_other_fructe} </div>

        </div>


        <div class="divCategorie" id="legume">
            <h1>Legume: {nr_legume} </h1>
            <div id="rosii"> Rosii: {nr_rosii} </div>
            <div id="ardei"> Ardei: {nr_ardei} </div>
            <div id="castraveti"> Castraveti: {nr_castraveti} </div>
            <div id="morcovi"> Morcovi: {nr_morcovi} </div>
            <div id="othersLegume"> Others: {nr_other_legume} </div>
        </div>
        <div class="divCategorie" id="alte_produse_alimentare">
            <h1>Produse alimentare: {nr_produsealimentare} </h1>
            <div id="cafea"> Cafea: {nr_cafea} </div>
            <div id="dulceata"> Dulceata: {nr_dulceata} </div>
            <div id="nuci"> Nuci: {nr_nuci} </div>
            <div id="ulei"> Ulei: {nr_ulei} </div>
            <div id="othersAlteProduseAlimentare"> Others: {nr_other_produsealimentare} </div>
        </div>
        <div class="divCategorie" id="animale">
            <h1>Animale domestice: {nr_animale}</h1>
            <div id="cai"> Cai: {nr_cai} </div>
            <div id="capre"> Capre: {nr_capre} </div>
            <div id="iepuri"> Iepuri: {nr_iepuri} </div>
            <div id="oi"> Oi: {nr_oi} </div>
            <div id="gaini"> Gaini: {nr_gaini} </div>
            <div id="vaci"> Vaci: {nr_vaci} </div>
            <div id="othersAnimale"> Others: {nr_other_animale} </div>
        </div>
        <div class="divCategorie" id="echipamente">
            <h1>Echipamente zootehnice: {nr_echipamente} </h1>
            <div id="tarcuri"> Tarcuri: {nr_tarcuri} </div>
            <div id="canistre"> Canistre: {nr_canistre} </div>
            <div id="racitoare"> Racitoare: {nr_racitoare} </div>
            <div id="stupi"> Stupi: {nr_stupi} </div>
            <div id="cantar_animale"> Cantare pentru animale: {nr_cantar} </div>
            <div id="colivii"> Colivii de pasari: {nr_colivii} </div>
            <div id="cuibare_porumbei"> Cuibare porumbei: {nr_cuibare} </div>
            <div id="othersEchipamente"> Others: {nr_other_echipamente} </div>
        </div>
    </div>
    <script src="code.js">
    </script>
</body>

</html>"""


if __name__ == '__main__':
  app.run(debug=True)
