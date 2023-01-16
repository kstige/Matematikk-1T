#!/usr/bin/env python
# coding: utf-8

# # Polynomfunksjoner
# 
# Et polynom er et uttrykk med flere ledd. I en polynomfunksjon med $x$ som variabel skal alle leddene inneholde potenser av $x$ opphøyd i et heltall større eller lik 0. Det kan vi skrive matematisk som:
# 
# ```{admonition} Definisjon: Polynomfunksjoner
# :class: def
# Alle ledd i en polynomfunksjon er på formen $ax^n$ der $a\in \mathbf{R}$ og $n\in \mathbf{N}\cup \{0\}$. \
# Den høyeste verdien av $n$ kaller vi graden til funksjonen.
# ```
# 
# ## Andregradsfunksjoner
# Andregradsfunksjoner er etter de lineære funksjonene de enkleste polynomfunksjonene. Alle andregradsfunksjoner kan skrives på formen $f(x)=ax^2+bx+c$. Grafen til en andregradsfunksjoner har form som en parabel med et ekstremalpunkt (toppunkt hvis $a<0$ og bunnpunkt hvis $a>0$). I tillegg vil grafen være symmetrisk om ei loddrett linje gjennom ekstremalpunktet
# 
# ```{admonition} Symmetrilinje
# :class: def
# Om vi tegner grafen til en andregradsunksjon $f(x)=ax^2+bx+c$, så vil den være symmetrisk om ei loddrett linje gjennom ekstremalpunktet. Symmetrilinja er gitt ved:
# 
# $$x=-\frac{b}{2a}$$
# 
# (som man muligens kjenner igjen som delen før $\pm$ i abc-formelen)
# 
# At grafen er symmetrisk om denne $x$-verdien betyr at $f(-\frac{b}{2a}+x)=f(-\frac{b}{2a}-x)$
# ```
# 
# `````{admonition} Eksempel: Symmetrilinje og ekstremalpunkt
# :class: eksempel, dropdown
# 
# Under er grafen til andregradsfunksjonen $f(x)=x^2-2x-3$.
# 
# ```{figure} ./bilder/andregradsfunksjon.png
# ---
# scale: 30%
# align: right
# ---
# ```
# 
# Siden $a=1>0$ har grafen et bunnpunkt. $x$-verdien til bunnpunktet er på symmetrilinja som vi finner ved $x=-\frac{-2}{2\cdot 1}=1$.
# 
# $y$-verdien er gitt ved $f(1)=1^2-2\cdot 1-3 = -4.
# 
# Bunnpunktet er altså $(1, -4)$. 
# 
# Som vi ser er grafen symmetrisk om linja $x=1$. Det vil si at om vi for eksempel øker/minker $x$ med 3 vil funksjonen ha samme verdi. $f(1+3)=f(4)=5$ og $f(1-3)=f(-2)=5$.
# `````
# 
# Ofte kan det være nyttig å skrive om andregradsuttrykket for å finne andre typer informasjon om funksjonen. Det kan vi gjøre med mange av teknikkene vi har lært oss om faktorisering, algebra og likninger.
# 
# ```{admonition} Skriveformer for andregradsfunksjoner
# :class: def
# Den vanligste formen for en andregradsfunksjon er:
# 
# $$f(x)=ax^2+bx+c$$
# 
# Vi kan finne nullpunktene $x_1$ og $x_2$ til funksjonen ved å løse andregradslikningen $f(x)=0$. Ved hjelp av nullpunktene kan vi skrive andregradsfunksjonen på faktorisert form:
# 
# $$f(x)=a(x-x_1)(x-x_2)$$
# 
# En tredje (og mindre vanlig) måte å skrive andregradsfunksjoner på er ved å bruke fullstendige kvadrat:
# 
# $$f(x)=a(x-x_e)^2+y_e$$
# 
# Siden kvadratet $(x-x_e)^2$ aldri kan bli mindre enn 0 må $y_e$ være den største/minste verdien til funksjonen. Punktet $(x_e, y_e)$ vil her være ekstremalpunktet til andregradsfunksjonen. Om det er et toppunkt eller et bunnpunkt avhenger av om $a$ er positiv eller negativ.
# ```
# 
# `````{admonition} Eksempel: Nullpunkt og ekstremalpunkt
# :class: eksempel, dropdown
# 
# Under er grafen til andregradsfunksjonen $f(x)=-2x^2+4x+6$.
# 
# ```{figure} ./bilder/andregradsfunksjon2.png
# ---
# scale: 30%
# align: right
# ---
# ```
# 
# Vi kan finne nullpunktene til funksjonen ved å løse $f(x)=-2x^2+4x+6=0$. Det kan vi gjøre med abc-formelen eller en annen metode. Vi får nullpunktene $x=-1$ og $x=3$. Vi kan derfor skrive funksjonen på faktorisert form som:
# 
# $$f(x)=-2(x+1)(x-3)$$
# 
# Hvis vi starter fra det opprinnelige uttrykket kan vi også prøve å lage oss et fullstendig kvadrat. Da starter vi med å trekke ut faktoren -2 for så å legge til og trekke fra 1 inne i parentesen. Så tar vi det leddet som ikke gir et fullstendig kvadrat utenfor parentesen.
# 
# $$f(x)=-2x^2+4x+6=-2(x^2-2x-3)=-2(x^2-2x+1-1-3)\\=-2(x^2-2x+1)+8=-2(x-1)^2+8$$
# 
# Da ser vi at toppunktet ($a=-2<0$) må være $(1,8)$ siden $-2(x-1)^2 \leq 0$.
# `````

# ## Nullpunktfaktorisering
# 
# Vi har sett at andregradsuttrykk kan nullpunktfaktoriseres. Det gjelder for alle polynomfunksjoner. I neste eksempel skal vi se på en viktig sammenheng mellom graden til polynomet og det maksimale antall nullpunkt.
# 
# ```{admonition} Eksempel: Nullpunkt og grad
# :class: eksempel, dropdown
# 
# Vi ser på en polynomfunksjon på faktorisert form $f(x)=(x-2)(x-1)(x+2)(x+3)$. Hvilken grad har polynomet?
# 
# Hvis vi multipliserer ut parentesene ser vi at høyeste eksponent av $x$ er $x^4$. Polynomet har derfor grad 4. Dersom vi hadde hatt flere nullpunkt ville vi fått en ekstra faktor som inneholder $x$ og graden av polynomet ville blitt høyere. En polynomfunksjon med grad 4 kan derfor ikke ha flere enn 4 nullpunkt.
# 
# ```
# 
# Resultatet fra forrige eksempel kan generaliseres til:
# 
# ```{admonition} Nullpunkt og grad
# :class: def
# Et polynom med grad $n$ kan ha
#  - mellom 1 og n nullpunkt dersom n er et oddetall
#  - mellom 0 og n nullpunkt dersom n er et partall
# ```
# 
# For en tredjegradsfunksjon vil vi derfor ha følgende faktorisering:
# 
# ```{admonition} Nullpunktsfaktorisering av tredjegradsfunksjoner
# :class: def
# Om nullpunktene til tredjegradsfunksjonen $f(x)=ax^3+bx^2+cx+d$ er $x_1$, $x_2$ og $x_3$, så vil faktoriseringen bli
# 
# $$f(x)=a(x-x_1)(x-x_2)(x-x_3)$$
# 
# Om $x_3$ er lik for eksempel $x_2$ vil faktoriseringen bli $f(x)=a(x-x_1)(x-x_2)^2$. Da har vi et såkalt dobbelt nullpunkt. Der vil grafen ha et topp- eller bunnpunkt for $x=x_2$.
# ```
# 
# Til slutt tar vi for oss et eksempel som viser hvordan vi kan utnytte nullpunktfaktorisering til å finne funksjonsuttrykket til en polynomfunksjon fra grafen.
# 
# `````{admonition} Eksempel: Ukjent funksjonsuttrykk 
# :class: eksempel, dropdown
# 
# Under er grafen til en tredjegradsfunksjon $f(x)$ med ukjent funksjonsuttrykk. Vi ser at den har nullpunkt i -2, 1 og 3.
# 
# ```{figure} ./bilder/tredjegradsfunksjon.png
# ---
# scale: 30%
# align: center
# ---
# ```
# 
# Nullpunktfaktoriseringen av uttrykket vil være
# 
# $$f(x)=a(x+2)(x-1)(x-3)$$
# 
# Vi ser også at funksjonen går gjennom punktet $(0,12)$. Det kan vi bruke til å finne den ukjente koeffisienten $a$. Vi setter inn $x=0$ og bruker at funksjonen da skal få verdien 12. 
# 
# $$f(0)=a\cdot 2\cdot (-1)\cdot(-3)=6a=12$$
# 
# Da må vi ha $a=2$.
# 
# Funksjonsuttrykket blir da $f(x)=2(x+2)(x-1)(x-3)=2x^3 -4x^2-10x+12$.
# `````

# ## Oppgaver
# 
# `````{admonition} Oppgave 1: Polynomfunksjoner
# :class: oppgave
# 
# Hvilke av funksjonene under er polynomfunksjoner
# 
# **a)** $f(x)=3x+2$\
# **b)** $g(x)=2x^2+3$\
# **c)** $h(x)=2x^{-3}-x^2+3x+1$\
# **d)** $i(x)=2$\
# **e)** $j(x)=\frac{2}{x}+x+1$\
# **f)** $k(x)=x^{2,3}-x^2+2x-5$
# 
# ```{admonition} Løsningsforslag
# :class: losning, dropdown
# 
# **a)** $f(x)=3x+2$ - en polynomfunksjon av første grad \
# **b)** $g(x)=2x^2+3$ - en polynomfunksjon av andre grad \
# **c)** $h(x)=2x^{-3}-x^2+3x+1$ - ikke en polynomfunksjon siden vi har en negativ eksponent \
# **d)** $i(x)=2$ - en polynomfunksjon av grad 0 \
# **e)** $j(x)=\frac{2}{x}+x+1$ - ikke en polymofunksjon siden $\frac{2}{x} = 2x^{-1}$ \
# **f)** $k(x)=x^{2,3}-x^2+2x-5$ - ikke en polynomfunksjon siden vi har en eksponent med desimaler
# ```
# `````

# ## Utforsk
# 
# Endre på koeffisientene $a$, $b$ og $c$ for å undersøke hvordan de påvirker utseendet og formen til en andregradsfunksjon.
# 
# Prøv om du kan svare på:
# 
#  * Hva skjer om $a=0$ og hvorfor?
#  * Hva er forskjellen på $a>0$ og $a<0$?
#  * Hva skjer når $a$ blir større?
#  * Hva skjer når du endrer på $c$?
#  * Hvor er symmetriaksen om $b=0$? Hvorfor må den være der?
#  * Hva skjer når du endrer på $b$?

# In[2]:


get_ipython().run_cell_magic('html', '', '\n<script src="https://www.geogebra.org/apps/deployggb.js"></script>\n\n<script>  \n    var params = {\n        "material_id": "bzznhhwc", \n        "appName": "graphing", \n        "width": 800, "height": 600, \n        "showToolBar": false, \n        "showAlgebraInput": false, \n        "showMenuBar": false,\n        "showResetIcon": true \n        };\n    var applet = new GGBApplet(params, false);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')

