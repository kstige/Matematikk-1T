#!/usr/bin/env python
# coding: utf-8

# # Uttrykk, likning og identitet
# 
# I arbeidet med algebra og likninger er det viktig å skille mellom innholdet i begrepene *uttrykk, likning og identitet*. Mange misforståelser i matematikk på dette nivået bunner i at man behandler algebraiske uttrykk som ei likning og/eller motsatt. Vi starter derfor med å definere begrepene før vi viser viktige forskjeller.
# 
# ```{admonition} Algebraisk uttrykk
# Et algebraisk uttrykk er bygd opp av tall og variabler og inneholder ikke likhetstegn.
# 
# Eksempler:
#  * $3x+4$
#  * $4b^2-3a^2b+8$
# 
# Det er også verdt å merke seg at en formel inneholder et uttrykk. For eksempel vil formelen for arealet av en sirkel, $A=\pi r^2$, si at arealet er gitt ved uttrykket $\pi r^2$.
# ```
# 
# ```{admonition} Likning
# Dersom vi setter to algebraiske uttrykk lik hverandre, så har vi en likning. Likningen består av en høyre side og en venstre side med et likhetstegn mellom.
# 
# Eksempler:
#  * $3x + 4 = 2x +1$
#  * $x^2+6x+9=0$
# 
# En likning kan være sann for ingen, en eller flere verdier for den ukjente variabelen.
# 
# Når vi setter inn kjente størrelser i en formel, så vil vi i mange tilfeller ende opp med en likning. Får vi vite at arealet av en sirkel er 8, så kan vi sette opp likningen $8=\pi r^2$ som kan løses for å finne radien i sirkelen.
# ```
# 
# ```{admonition} Identitet
# En identitet er er en likning med uendelig mange løsninger. Det vil si at det er to algebraiske uttrykk som er lik for alle verdier av variablene.
# 
# Eksempler:
#  * $2(x+3)=2x+6$
#  * kvadratsetningnene ($(a+b)^2=a^2+2ab+b^2$)
# ```
# 
# Det kan virke unaturlig og undøvendig å skille mellom disse tre. Forskjellen er imidlertid viktig fordi vi må behandle uttrykk og likninger på forskjellige måter.
# 
# I en likning kan vi (men noen begrensninger) utføre samme matematiske operasjon på begge sider av likhetstegnet uten at likningen endres. Vi kan for eksempel multiplisere med et tall for å få vekk brøker. Ved å multiplisere med 5 i en likning gjør vi både venstre og høyre side av likningen 5 ganger så stor. Det endrer ikke likningen.
# 
# Dersom vi gjøre det samme i et uttrykk, så endrer vi hele uttrykket. Dersom vi multipliserer uttrykket av arealet til en sirkel med 5, så får vi $5\pi r^2$. Da har vi gjort arealet 5 ganger så stort. Det kan vi derfor ikke gjøre. Vi kan allikevel forenkle eller omskrive uttrykk. Da er det imidlertid viktig at hvert ledd i omskrivingen er en identitet. Eksempler på dette er når vi har laget fullstendige kvadrat (og faktorisert). Da legger vi til og trekker fra like mye slik at vi ikke endrer verdien på uttrykket.
# 
# Senere i faget skal vi arbeide med funksjoner. Det kan være verdt å merke seg at en funksjon er en likning som viser sammenhengen mellom to størrelser. Høyresiden i en funksjon vil være et uttrykk som viser verdien til venstre siden. Dette er på mange måter det samme som en formel.
# 
# `````{admonition} Avgjøre om en likning er en identitet
# :class: eksempel
# Vi skal avgjøre om $x^2+6x+8=(x+2)(x+4)$ er en identitet.
# 
# **For hånd**
# 
# Vi kan gå fram på to måter:
#  * faktorisere venstre side med fullstendig kvadrat metoden
#  * multiplisere ut høyre side
# 
# Det siste alternativet er enklest: $(x+2)(x+4)=x^2+4x+2x+8=x^2+6x+8$. Vi ser at uttrykkene er eksakt like. Det er derfor en identitet.
# 
# **Med CAS**
# 
# Vi skriver inn uttrykket i CAS med dobbelt likhetstegn "==" mellom. Da får vi symbolet vist i utklippet under. Dersom likningen er en identitet får vi resultatet *true*. Dersom det ikke er en identitet får vi *false*.
# 
# ```{figure} ./bilder/identitet.png
# ---
# scale: 70%
# ---
# ```
# 
# Vi ser at likningen er en identitet. Det vil si at den stemmer for alle verdier av $x$.
# `````
# 
