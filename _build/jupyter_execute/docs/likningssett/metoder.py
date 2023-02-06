#!/usr/bin/env python
# coding: utf-8

# # Metoder for løsning av likningssett
# 
# 
# ## Introduksjon
# 
# Fram til nå har vi sett på likninger med en variabel. Eksempler på det er 
# 
#  * $3x+6=0$
#  * $x^2+x=6$
# 
# og tilsvarende. 
# 
# Nå skal vi se på likninger med flere ukjente størrelser. Et eksempel kan være $2x - y = 4$. For å løse denne likningen må vi finne verdier både for $x$ og $y$ som gjør at høyre side blir lik venstre side. Vi kan tenke oss at vi prøver å løse for $y$ først. Da ender vi opp med $y=2x-4$. Det her er likningen for ei rett linje, og vi ser at det er mange (faktisk uendelig mange) løsninger. Lar vi $x=1$ får vi $y=-2$. Dersom $x=2,5$ får vi $y=1$, og slik kunne vi fortsatt. Alle par av verdier for $x$ og $y$ som passer i likningen er løsninger. Vi kan også tegne likningen som en graf i et koordinatsystem.
# 
# ```{figure} ./bilder/enlikning.png
# ---
# scale: 20%
# ---
# ```
# 
# Det her viser oss at en likning ikke er nok for å kunne bestemme verdiene av $x$ og $y$. For å kunne finne en bestemt verdi for de to ukjente størrelsene trenger vi to likninger. Generelt trenger vi like mange likninger som vi har ukjente størrelser for å kunne avgjøre en bestemt verdi for alle størrelsene.
# 
# Vi skal her i innledningen se på metoder for å løse lineære likningssett med to ukjente. Det er et sett med to likninger der begge varibalene er av første grad. Metodene vi bruker her kan enkelt overføres til likningssett som er ikke-lineære eller som har flere variabler.
# 
# I alle eksemplene under skal vi se på likningssettet
# 
# $$
# 2x - y = 4 \\
# x + y = 5
# $$
# 
# Når vi skal løse likningssett må vi finne et par av verdier for $x$ og $y$ som passer med begge likningene. Løsningen av dette likningssettet viser seg å være $x=3 \land y=2$. Symbolet $\land$ kalles konjunksjon og betryr "og".
# 
# ```{admonition} Antall løsninger
# :class: dropdown
# Et likningssett med to likninger og to ukjente kan ha
#  * ingen løsning
#  * en løsning
#  * uendelig mange løsninger
# Andre muligheter finnes ikke
# ```

# ## Grafisk metode
# 
# I innledningen tegnet vi opp likningen $2x-y=4$ i et koordinatsystem. Den grafiske metoden går ut på å tegne inn begge likningene i det samme koordinatystemet og finne skjæringspunktet mellom dem.
# 
# `````{admonition} Grafisk metode
# :class: eksempel
# Skriver inn begge likningene i GeoGebra. Vi ser at begge likningene hver for seg har uendelig mange løsninger, men en av løsningene passer i begge likningene. Det er den vi er ute etter. Vi bruker "Skjæring mellom to objekt" for å finne skjæringspunktet $(3,2)$.
# 
# ```{figure} ./bilder/grafiskmetode.png
# ---
# scale: 20%
# ---
# ```
# 
# Det betyr at løsningen av likningssettet er $x=3 \wedge y = 2$. Siden løsningen er et par av verdier som tilsvarer et punkt i et koordinatsystem kan vi også skrive løsningen som $L=\{(3,2)\}$.
# `````
# 
# ```{admonition} Sammenheng med vanlige likninger
# :class: dropdown
# Vanlige likninger som $2x-4=x-5$ har vi sett kan løses på en tilsvarende måte grafisk. Da setter vi opp hver side som en rett linje (eller funksjon):
# 
# $$
# y=2x-4\\
# y=5-x
# $$
# 
# Så tegner vi grafene og finner skjæringspunktet. Likningssett med to ukjente og vanlige likninger har derfor en nær sammenheng.
# ```

# ## Løsning med CAS
# Med CAS har vi den enkleste metoden for å løse likningssett.
# 
# `````{admonition} Løsning med CAS
# :class: eksempel
# Vi skriver inn likningene i hver sin linje i CAS. Så merker vi begge linjene og trykker på løs-knappen.
# 
# ```{figure} ./bilder/CASmetode.png
# ---
# scale: 60%
# ---
# ```
# Løsningen av likningssettet er $x=3 \wedge y = 2$, eller $L=\{(3,2)\}$.
# `````

# ## Innsettingsmetoden
# Den neste metoden kommer vi fram til ved å ta utgangspunkt i vanlig likningsløsning. Vi starter med å løse den ene likningen for en av variablene. Så setter vi denne inn den andre likninge for å ende opp med en likning i en variabel.
# 
# ```{admonition} Innsettingsmetoden
# :class: eksempel
# Skriver den andre likningen som $y=5-x$ og setter det inn i den første likningen.
# 
# $$
# 2x-y=4 \\
# 2x-(5-x)= 4\\
# 3x-5=4\\
# 3x=9\\
# x=3
# $$
# 
# Så setter vi det tilbake i den andre likninge og får
# 
# $$
# y=5-x=5-3=2
# $$
# 
# Løsningen av likningssettet er $x=3 \wedge y = 2$, eller $L=\{(3,2)\}$.
# ```

# ## Addisjonsmetoden
# 
# Addisjonsmetoden er en effektiv metode for løsning av likningssett, men den kan være noe vanskeligere å forstå. Hovedessensen i løsningsmetoden er å legge sammen likningene på en "lur" måte slik at den ene ukjente forsvinner.
# 
# ```{admonition} Addisjonsmetoden 1
# :class: eksempel
# 
# Vi legger sammen likningene våre. Det vil si at vi legger sammen alt på venstre side for seg og alt på høyre side for seg. Likningen vi ender opp med må fortsatt stemme.
# 
# VS: $(2x-y)+(x+y)=3x$
# 
# HS: $4+5=9$
# 
# Vi ender da opp med likningen $3x=9$ som vi løser og får $x=3$. Vi setter $x=3$ inn i den andre likningen og får $3+y=5$ som gir $y=2$.
# 
# Løsningen av likningssettet er $x=3 \wedge y = 2$, eller $L=\{(3,2)\}$.
# ```
# 
# I eksempelet over viste vi den enkleste varianten av addisjonsmetoden der den ene variabelen forsvinner bare ved å legge sammen likningene. Det er ikke alltid det er mulig og derfor skal vi løse likningssettet på nytt ved å prøve å få vekk $x$ i stedet for $y$.
# 
# ```{admonition} Addisjonsmetoden 2
# Vi ser at vi har $2x$ i den første likningen og $1x$ i den andre, så det vil ikke fungere å bare legge dem sammen. Men om vi ganger den andre likningen med -2 før vi legger sammen, så får vi:
# 
# VS: $(2x+y)-2(x+y)=-y$
# 
# HS: $4+(-2)\cdot 5= -2$
# 
# Vi ender altså opp med likningen $-y=-2$ som gir $y=2$. Vi setter inn i den andre likningen og får $2x+(-2)=4$ som gir $x=3$.
# 
# Løsningen av likningssettet er $x=3 \wedge y = 2$, eller $L=\{(3,2)\}$.
# ```

# ## Løsning med programmering
# 
# Det er mange metoder som kan brukes for å løse med programmering. For å forstå disse metodene er det stort sett nødvendig med kunnskap innenfor et område av matematikk som kalles "Lineær algebra". Her nøyer vi oss med å vise hvordan vi kan bruke en ferdig implementert løsningsmetode for lineære likningssett i python. 
# 
# Vi ser fortsatt på likningssettet
# 
# $$
# 2x - y = 4 \\
# x + y = 5
# $$
# 
# Datamaskinen vil se på problemet på formen $Ax=b$, der $A$ består av koeffisientene (tallene foran de ukjente) på venstre side, mens $b$ er tallene på høyre side.
# 
# $$
# A=
# \begin{bmatrix}
#     2& -1\\
#     1 & 1 \\
# \end{bmatrix}
# ,\quad
# x=
# \begin{bmatrix}
#     x \\
#     y \\
# \end{bmatrix}
# ,\quad
# b=\begin{bmatrix}
#     4 \\
#     5 \\
# \end{bmatrix}
# $$
# 
# Dette er noe som kalles matriser, men det trenger vi ikke bry oss om før på matematikk på universitetet. Det viktige er at første linje i $A$ er tallene foran henholdsvis $x$ og $y$ i den første likningen, mens den andre linjen er tallene fra den andre likningen. Vi må skrive inn $A$ og $b$ i programmet vårt som noe som kalles "array" i python-språket.
# 
# ```{code-block} text
# A = array([[2,-1],[1,1]])
# b = array([4,5])
# ```
# Videre bruker vi en kommando som løser likningssystemet for oss.
# 
# ```{code-block} text
# x =linalg.solve(A,b)
# ```
# 
# Det fullstendige programmet blir

# In[1]:


from pylab import *

A = array([[2,-1],[1,1]])
b = array([4,5])

x = linalg.solve(A,b)
print(x)


# Vi ser at vi får ut en løsning som betyr at $x=3$ og $y=2$ som vi forventet.
# 
# Under kan du kjøre programmet og prøve å endre på det for å løse andre likningssett. Hva tror du at du må gjøre for å løse et likningssett med tre ukjente?
# 
# <iframe src="https://trinket.io/embed/python3/8878d4ed7a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# 

# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Grafisk metode
# <iframe width="680" height="350" src="https://www.youtube.com/embed/K__ldC6Ke2M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ```{tab-item} Løsning i CAS
# <iframe width="680" height="350" src="https://www.youtube.com/embed/g1pBbdRCYC0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ```{tab-item} Innsettingsmetoden
# <iframe width="680" height="350" src="https://www.youtube.com/embed/hkXs5epJI6g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ```{tab-item} Addisjonsmetoden
# <iframe width="680" height="350" src="https://www.youtube.com/embed/U72cdCNRT2k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
