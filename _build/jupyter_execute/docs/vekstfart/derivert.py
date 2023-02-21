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

# In[4]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 1,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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",\n    };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


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
