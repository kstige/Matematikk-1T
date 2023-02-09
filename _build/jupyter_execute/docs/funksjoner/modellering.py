#!/usr/bin/env python
# coding: utf-8

# # Modellering
# 
# Matematikken vi bruker på skolen vil ofte føles virkelighetsfjern. Den skal imidlertid gi oss et grunnlag for å beskrive noe virkelig. For at matematikken skal bli nyttig for en lege, ingeniør, arkitekt eller en annen yrkesgruppe trengs det matematiske modeller som kan beskrive virkeligheten. En matematisk modell gir en forenklet beskrivelse av virkeligheten ved hjelp av matematikk. Modellene kan for eksempel være formler, funksjoner grafer eller tabeller. Her skal vi fokusere på funksjoner som matematiske modeller.
# 
# Fram til nå har vi sett på mange vilkårlige funksjoner for å undersøke egenskaper til de ulike funksjonstypene. Når vi arbeider med funksjoner i "det virkelige liv" skal funksjonene være en modell for noe reellt. Det kan være en funksjon som beskriver innbyggertallet i en kommune, posisjonen til en bil, havnivå, inntjening for en bedrift, eller noe helt annet.
# 
# Først tar vi for oss noen viktige ord. Ordene og forklaringene vil gi mer mening etter at vi har tatt noen eksempler. Gå derfor tilbake til disse definisjonene når du møter ord du ikke forstår.
# 
# ```{admonition} Gyldighetsområde
# :class: dropdown
# Dersom modellen vår er gitt ved en funksjon, så vil gyldighetsområdet være verdiene av variabelen som modellen gjelder for. Det her henger tett sammen med begrepet definisjonsmengde.
# ```
# 
# ```{admonition} Regresjon
# :class: dropdown
# Regresjon er en matematisk metode for å lage den funksjonen som passer best til målinger vi har gjort.
# ```
# 
# ```{admonition} Parametre
# :class: dropdown
# Antall størrelser som bestemmes for å tilpasse målte data til en gitt modell.
# 
#  * Til en lineær modell $ax+b$ må vi bestemme to parametre $a$ og $b$.
#  * Til en andregradsmodell $ax^2+bx+c$ må vi bestemme tre parametre $ax^2+bx+c$.
# 
# Vi renger minst like mange målepunkt som vi har parametre for å kunne lage en modell. Om vi har flere målepunkt enn antall parametre vil vi se at funksjonen vår ikke går nøyaktig gjennom alle målepunktene.
# ```
# 
# ```{admonition} Interpolere og ekstrapolere
# :class: dropdown
# Interpolasjon betyr å bruke en modell til å anslå verdier innenfor området til målepunktene.
# 
# Ekstrapolasjon betyr å bruke en modell til å anslå verdier utenfor området til målepunktene.
# ```

# ## Matematiske modeller for hånd
# 
# I prinsippet kan vi lage de fleste matematiske modeller for hånd. Vi har også gjort det tidligere når vi har funnet funksjonsuttrykk for rette linjer gjennom to punkt eller andre funksjonstyper gjennom et gitt antall punkt.
# 
# ```{admonition} Eksempel: Modell - eksponentiell modell
# :class: eksempel
# Innbyggertallet i en kommune er 5000 i 2010. 10 år senere har innbyggertallet økt til 6400.
# 
# Dersom innbyggertallet følger en lineær modell, så vil antall innbyggere stige med $\frac{6400-5000}{10}=140$ personer i året. Dette tilsvarer stigningstallet til den lineære modellen. For enkelthetsskyld setter vi 2010 til å være $x=0$. Da vil konstantleddet være 5000.
# 
# En lineær modell vil være $l(x)=140x+5000$, der $x$ er antall år etter 2010 og gyldighetsområdet er $x\in [0,10]$.
# 
# For å sette opp den lineære modellen brukte vi to punkt: $(0,5000)$ og $(10,6400)$. Det stemmer med at det er to parametre $a$ og $b$ i en lineær modell $ax+b$.
# ```
# 
# ```{admonition} Eksempel: Modell - eksponentiell modell
# :class: eksempel
# Innbyggertallet i en kommune er 5000 i 2010. 10 år senere har innbyggertallet økt til 6400.
# 
# Dersom innbyggertallet følger en eksponentiell modell, så vil antall innbyggere stige med en fast prosent i året. Den eksponentielle modellen er generelt gitt ved $e(x)=a\cdot b^x$. Vi må altså bestemme de to parametrene $a$ og $b$ ved hjelp av punktene $(0,5000)$ og $(10,6400)$.
# 
# Med det første punktet får vi at $e(0)=a=5000$ som bestemmer parameteren $a$.
# 
# Med det andre punktet får vi at $l(10)=5000\cdot b^10=6400$. Vi løser likningen med CAS og får at $b=1,025$.
# 
# En eksponentiell modell blir da $e(x)=5000\cdot 1,025^x$, er $x$ er antall år etter 2010 og gyldighetsområdet er $x\in [0,10]$. Modellen tilsier at innbyggertallet øker med $2,5\%$ i året.
# ```
# 
# Over ser vi at det går an å lage ulike modeller for de samme målingene.
# 
# ```{admonition} Valg av modell
# Ved valg av modell er det flere ting vi bør ta hensyn til, og det kan være flere modeller som passer med det vi skal beskrive. Noen punkt vi bør ta hensyn til er:
# 
#  * Modellen må ligge nær til målepunktene
#  * Hvis flere modeller passer, så velger vi den enkleste (færrest parametre)
#  * Vil modellen kunne gi fornuftige anslag utenfor målepunktene
#  * Om modellen beskriver naturen bør vi se om den stemmer med naturlover
# 
# Forventer vi at det vi måler skal ha jevn endring, så velger vi en lineær modell. Forventer vi en jevn prosentvis endring, så velger vi en eksponentiell modell.
# ```
# 
# Før vi går over på å lage modeller digitalt, så tar vi et eksempel som krever at vi har vært gjennom likningssett.
# 
# `````{admonition} Andregradsmodell
# :class: eksempel, dropdown
# Finn en andregradsfunksjon som går gjennom punktene $(1,0)$, $(3,8)$ og $(4,18)$.
# 
# Vi vet at andregradsfunksjoner er på formen $f(x)=ax^2+bx+c$. Det vil si at vi har tre parametre som vi kan finne ved hjelp av de tre punktene.
# 
# $
# \begin{align}
# f(1) &=a+b+c &=& 0 \\
# f(3) &=9a+3b+c &=& 8 \\
# f(4) &=16a+4b+c &=& 18
# \end{align}
# $
# 
# Løser likningssettet med CAS på følgende måte
# 
# ```{figure} ./bilder/andregradsmodellCAS.png
# ---
# scale: 70%
# ---
# ```
# 
# Det vil si at den andregradsfunksjonen som går gjennom punktene er $f(x)=2x^2-4x+2$.
# `````

# ## Regresjon med GeoGebra
# 
# Vanligvis bruker vi digitale verktøy for å finne matematiske modeller. Metoden som brukes kalles for regresjon. Vi skal ikke gå i detalj på hva som skjer, men essensen er at datamaskinen prøver mange funksjoner av valgt type og finner den som totalt sett har minst avvik fra målepunktene.
# 
# Vi kommer stort sett til å bruke GeoGebra til å utføre regresjon, men viser også hvordan det kan gjøres ved programmering. I GeoGebra er det enkelt å utføre regresjon, men gjennom programmering har vi flere muligheter til å tilpasse modellene våre. 
# 
# Regresjon i GeoGebra viser vi enklest ved et eksempel.
# 
# `````{admonition} Eksempel: regresjon
# :class: eksempel
# I tabellen under vise statistikk fra ssb.no over antall elbiler som ble solgt i Molde i perioden 2013-2017. Vi skal lage en eksponentialmodell som passer med dette. Vi lar $x$ være antall år etter 2013.
# 
# ```{figure} ./bilder/elbiltabell.png
# ---
# scale: 70%
# ---
# ```
# 
# Det første vi gjør er å legge tallene fra tabellen inn i regnearket i GeoGebra.
# 
# ```{figure} ./bilder/elbilregneark.png
# ---
# scale: 70%
# ---
# ```
# 
# Så markerer vi tallene og velger "Regresjonsanalyse" i menyen.
# 
# ```{figure} ./bilder/regresjonsmeny.png
# ---
# scale: 70%
# ---
# ```
# 
# Da får vi bildet under der vi har valgt "Eksponentiell" under menyen for regresjonsmodell.
# 
# ```{figure} ./bilder/elbilregresjon.png
# ---
# scale: 50%
# ---
# ```
# 
# Vi ser at den eksponentialmodellen som passer best er $f(x)=54\cdot 1,63^x$. Det vil si at elbilsalget vokser med omtrent $63\%$ i året.
# 
# Dersom vi ønsker å jobbe videre med funksjonen vil det være praktisk å overføre den til grafikkfeltet. Det gjør vi ved å trykke på knappen på bildet under.
# 
# ```{figure} ./bilder/kopiertilgrafikkfelt.png
# ---
# scale: 70%
# ---
# ```
# `````
# 
# `````{admonition} Eksempel: Interpolasjon og ekstrapolasjon
# :class: eksempel
# 
# Vi skal jobbe litt videre med eksempelet for å se på begrepene interpolasjon og ekstrapolasjon. Dersom vi henter ut flere tall fra ssb.no finner vi at antall solgte elbiler i Molde i 2015 og 2019 var:
# 
# ```{figure} ./bilder/elbiltabell2.png
# ---
# scale: 30%
# ---
# ```
# 
# Vi vil undersøke hvordan dette passer med modellen vi har funnet.
# 
# **Interpolasjon**
# Interpolasjon betyr å bruke modellen innenfor området begrenset av målepunktene. Når vi skal bruke modellen for 2015 ($x=2$), så interpoler vi. Vi kan overføre funksjonen til grafikkfeltet og lese av den der, men det enkleste er å bruke feltet for "Symbolsk inntasting". Der skriver vi inn $x=2$ og får ut verdien til funksjonen.
# 
# ```{figure} ./bilder/symbolskutregning1.png
# ---
# scale: 70%
# ---
# ```
# Vi får $143$ solgte elbiler som ligger noe under, men ikke så langt under den riktige verdien. At vi får en for lav verdi betyr at den virkelige veksten i starten av perioden var prosentvis større enn den var senere i perioden.
# 
# **Ekstrapolasjon**
# Ekstrapolasjon betyr å bruke modellen utenfor området begrenset av målepunktene. Når vi skal bruke modellen for 2019 ($x=6$), så ekstrapolerer vi. 
# 
# ```{figure} ./bilder/symbolskutregning2.png
# ---
# scale: 70%
# ---
# ```
# 
# Vi får $1008$ solgte elbiler som ligger langt over den riktige verdien.
# 
# Det vi ser over stemmer med det vi vanligvis observerer. Verdier funnet ved interpolasjon vil passe bedre med modellen enn verdier funnet ved ekstrapolasjon.
# `````
# 

# ## Regresjon med programmering
# 
# Under er det gitt et program som utfører lineær regresjon på listene med $x$- og $y$-verdier. Programmet er delt opp med korte forklaringer før hele programmet (med mulighet for å endre) er gitt til slutt.
# 
# Vi starter med å importere ekstra bibliotek som vi trenger.

# In[8]:


from pylab import *
from scipy.optimize import curve_fit


# Så skriver vi inn listene med $x$- og $y$-verdier som vi skal utføre regresjonen på. Disse listene kommer fra datapunktene våre (målinger).

# In[9]:


x = [1, 2, 3, 4, 5]
y = [1.9, 4.1, 6.3, 7.2, 10.8]


# Videre lager vi en funksjon som viser hvilken modell vi ønsker å bruke. I dette eksempelet er det en lineær modell med variabel $x$ og parametre $a$ og $b$. Her kan vi lage akkurat den funksjonstypen vi ønsker, eller sette opp en kombinasjon av flere funksjonstyper. Under definisjonen av modellen bruker vi kommandoen curve_fit som utfører selve regresjonen og finner parametrene. De skrives så ut med to desimaler.

# In[11]:


def modell(x, a, b):
    return a*x+b

[a, b] = curve_fit(modell, x, y)[0]
print("a = ", round(a, 2))
print("b = ", round(b, 2))


# Dersom vi ønsker å lage en graf av modellen kan vi bruke koden under. Den starter med å velge verdiene for $x$ som vi skal sette inn i modellen. Så beregner den $y$-verdiene for alle disse $x$-verdiene. Resten av koden er ulike kommandoer for å tilpasse grafen.

# In[12]:


x_akse = linspace(0, 10, 1000)
y_modell = modell(x_akse, a, b)

plot(x_akse, y_modell, color = "blue", label = "Lineær modell")
scatter(x, y, color = "red", label = "Datapunkter")
xlabel("x")
ylabel("y")
grid()
legend()
show()


# Under er hele programmet satt sammen. 
# 
#  * Endre på listene med $x$- og $y$-verdier og se hvordan modellen endrer seg. 
#  * Gjør om modellen til en andregradsmodell. Da må du innføre en ekstra parameter $c$, endre på linje 7, 8, 10 og 15. I tillegg må du legge til ei linje etter linje 12.
#  * Klarer du å lage en eksponentialmodell.
# 
# <iframe src="https://trinket.io/embed/python3/3adb2590c6" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# 
