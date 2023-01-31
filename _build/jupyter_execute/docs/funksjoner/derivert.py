#!/usr/bin/env python
# coding: utf-8

# # Den deriverte
# 
# Den momentane vekstfarten er en viktig størrelse fordi den leder oss mot en av de viktigste størrelsene i matematikken. Vi ser først på et eksempel.
# 
# ```{admonition} Eksempel: Momentan vekstfart
# :class: eksempel, dropdown
# Bruker GeoGebra-under eksempelet til å finne den momentane vekstfarten (MV) til $f(x)=x^2$ for $x\in\{-4,-3,-2,-1,0,1,2,3,4\}$. Verdiene fyller vi inn i en tabell.
# | **x**    | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
# |----------|---|---|---|----|---|---|---|---|---|
# | **MV**| -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8 |
# 
# ```

# 
# I eksempelet over ser vi at for hver verdi vi har av $x$, så får vi en verdi for den momentane vekstfarten. Det vil si at den momentane vekstfarten oppfyller kravet til å være en funksjon. Denne funksjonen gir vi et eget navn: Vi kaller den for "den deriverte av $f(x)$", og vi bruker skrivemåten $f'(x)$.
# 
# ```{admonition} Definisjon: Den deriverte
# :class: def
# 
# $f'(x)$ (leses "f derivert av x") er en funksjon som har funksjonsverdi lik stigningstallet til tangenten til $f(x)$ i punktet $(x, f(x))$.
# 
# Den deriverte i et punkt har samme verdi som den momentane vekstfarten i punktet.
# ```
# 
# Vi kommer nå til å bruke for eksempel $f'(2)$ i stedet for å snakke om den momentane vekstfarten til $f(x)$ i punktet $(2, f(2))$. Det er allikevel viktig å huske på at den deriverte er en funksjon som gir oss den momentane vekstfarten.

# ## Uttrykk for den deriverte
# I 1T kommer vi ikke til å ha arbeide med å finne funksjonsuttrykket for den deriverte (det kommer i R1/S1). Fokuset kommer til å være på forståelsen av hva den deriverte sier oss. Det kan allikevel være greit å se at den deriverte også vil være gitt ved et funksjonsuttrykk.
# 
# `````{admonition} Eksempel: Funksjonsuttrykk for den deriverte
# :class: eksempel, dropdown
# Vi ser på tabellen fra forrige eksempel en gang til, me kaller nå verdiene for den momentane vekstfarten for $f'(x)$.
# 
# | **x**    | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
# |----------|---|---|---|----|---|---|---|---|---|
# | **f'(x)**| -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8 |
# 
# Vi ser at $f'(x)$ har den doble verdien av $x$. Det må bety at funksjonsuttrykket for $f'(x)$ må være
# 
# $$
# f'(x)=2x
# $$
# 
# ```{figure} ./bilder/derivertuttrykk.png
# ---
# scale: 80%
# align: right
# ---
# ```
# Vi kan bruke CAS for å undersøke om dette stemmer. Vi definerer funksjonen ved $f(x):=x^2$ før vi i linje 2 skriver inn $f'(x)$ slik vi ser i figuren til høyre.
# 
# `````

# ## Fortegn til den deriverte
# 
# Siden den deriverte er stigningstallet til tangenten i et punkt på grafen, så vil fortegnet til den deriverte vise oss om grafen stiger eller synker. Bruk GeoGebra-appen over til å kontrollere at den deriverte (den momentane vekstfarten) er positiv når grafen stiger og negativ når grafen synker.
# 
# På samme måte som vi er interessert i punktene der $f(x)=0$ (nullpunktene til funksjonen), så har også punkt der $f'(x)=0$ spesiell interesse. At den deriverte er 0 i et punkt må bety at tangenten til grafen er vannrett i punktet. Hvis vi ser for oss en graf, så ser vi at det skjer i topp- og bunnpunkt. Ved å finne nullpunktene til $f'(x)$ kan vi altså finne topp- og bunnpunkt for $f(x)$.
# 
# ```{admonition} Fortegnet til den deriverte
# :class: def
# 
# For en funksjon $f(x)$ gjelder det at:
# 
#  * $f'(x)>0$ når grafen stiger mot høyre
#  * $f'(x)<0$ når grafen synker mot høyre
#  * $f'(x)=0$ og skifter fortegn når grafen har topp- eller bunnpunkt
# 
# Det siste punktet gjelder ikke for eventuelle topp- og bunnpunkt som er endepunkter i definisjonsmengden til funksjonen.
# 
# ```
# 
# Når vi skal analysere en funksjon og finne ut hvordan den oppfører seg ønsker vi ofte å bare se på fortegnene til funksjonen og den deriverte. Til det bruker vi det vi kaller ei fortegnslinje. Vi bruker hel linje for å markere at funksjonen (eller den deriverte) er positiv, stipla linje om den er negativ, og en $0$ om det er nullpunkt.
# 
# `````{admonition} Eksempel: Fortegnslinje
# :class: eksempel, dropdown
# 
# Ei fortegnslinje kan se ut som på figuren under
# 
# ```{figure} ./bilder/eksempelfortegnslinje.png
# ---
# scale: 50%
# ---
# ```
# 
# Denne fortegnslinja viser at funksjonen har nullpunkt for $x=-2$ og $x=2$. For $x<-2$ og $x>2$ er funksjonen positiv. For $-2<x<2$ er funksjonsverdien negativ. Fortegnslinja for den deriverte viser et nullpunkt for $x=0$ og at den deriverte er negativ før $x=0$ og positiv etter. Det betyr at $x=0$ må være et bunnpunkt for funksjonen.
# 
# Det kan være flere funksjoner som passer med dette, men et eksempel er:
# 
# ```{figure} ./bilder/fortegnslinjemedgraf.png
# ---
# scale: 20%
# ---
# ```
# `````
# 
# Under kan skrive inn funksjonsuttrykk for polynomfunksjoner og få fram fortegnslinje for $f(x)$ og $f'(x)$ (og for den andrederiverte $f''(x)$, men den ser vi ikke på i 1T). Prøv deg fram med ulike funksjonsuttrykk og se hvordan fortegnslinja for $f(x)$ viser hvor funksjonen er positiv/negativ og hvordan fortegnslinja $f'(x)$ viser hvor funksjonen stiger/synker. Du kan også tegne inn grafen til $f'(x)$ dersom du vil se den.

# In[5]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 1,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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"\n   };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# `````{admonition} Eksempel: Fra graf til fortegnslinje
# :class: eksempel, dropdown
# 
# Vi skal tegne fortegnslinje for funksjonen $f(x)=\frac{1}{2}x^{3} - 3x^{2} + \frac{3}{2}x + 5$ som er tegnet i grafen under. Ved å ta utgangspunkt i grafen skal vi tegne fortegnslinje for funksjonen og den deriverte til funksjonen.
# 
# ```{figure} ./bilder/graftilfortegnslinje.png
# ---
# scale: 20%
# ---
# ```
# 
# Når vi skal tegne fortegnslinje for selve funksjonen, så ser vi på hvor den er positiv og hvor den er negativ. Vi ser da at 
# 
#  * $f(x)>0$ for $x\in\langle -1, 2\rangle \cup \langle 5, \rightarrow\rangle$.
#  * $f(x)<0$ for $x\in\langle \leftarrow, -1\rangle \cup \langle 2, 5\rangle$.
#  * $f(x)=0$ for $x\in\{-1, 2, 5\}$.
# 
# Når vi skal tegne fortegnslinje for den deriverte, så ser vi på hvor funksjonen stiger og synker. Det er litt vanskelig å se nøyaktig, men om vi finner $x$-verdiene til topp- og bunnpunkt ved hjelp av CAS, så ser vi at
# 
#  * $f(x)$ stiger slik at $f'(x)>0$ for $x\in\langle\leftarrow, 2-\sqrt{3}\rangle \cup \langle 2+\sqrt{3}, \rightarrow\rangle$.
#  * $f(x)$ synker slik at $f'(x)<0$ for $x\in\langle 2-\sqrt{3}, 2+\sqrt{3}\rangle$.
#  * $f(x)$ er flat slik at $f'(x)=0$ for $x\in \{2-\sqrt{3}, 2+\sqrt{3}\}$.
# 
# ```{figure} ./bilder/fortegnslinjeeksempel.png
# ---
# scale: 35%
# ---
# ```
# `````
