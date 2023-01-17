#!/usr/bin/env python
# coding: utf-8

# # Potensfunksjoner
# 
# En funksjonstype som kan likne litt på eksponentialfunksjoner er potensfunksjoner. Det er imidlertid viktig å kunne skille de fra hverandre. Der variabelen $x$ i en eksponentialfunksjon er eksponenten i en potens, vil variabelen i en potensfunksjon være grunntallet.
# 
# Potensfunksjonen vil derfor minne en del om polynomfunksjoner. Eksponenten i en polynomfunksjon kan kun være et heltall større eller lik 0. Det er imidlertid ingenting i veien for å ha negative tall eller desimaltall i en eksponent, og bruker vi det får vi en potensfunksjon
# 
# ```{admonition} Definisjon: Potensfunksjoner
# :class: def
# Potensfunksjoner er funksjoner på formen $f(x) = a\cdot x^b$, der $a$, $b \in \mathbf{R}\backslash\{0\}$.
# 
# Dersom $b$ ikke er et heltall, så vil potensfunksjonen kun være definert for positive verdier av $x$.
# 
# Dersom $b$ er negativ, så vil potensfunksjonen ikke være definert $x=0$.
# ```
# 
# Det er viktig å legge merke til at potensfunksjoner i motsetning til polynomfunksjoner kun inneholder ett ledd. Polynomfunksjoner med ett ledd er også potensfunksjoner.
# 
# ```{admonition} Eksempel: Potensfunksjoner
# :class: eksempel
# Formen på en potensfunksjon avhenger av størrelsene $a$ og $b$. Under er funksjonen $f(x)=2x^b$ tegnet inn (for positive $x$-verdier) for noen forskjellige verdier av $b$.
# 
# ```{figure} ./bilder/potensfunksjon.png
# ---
# scale: 20%
# ---
# ```
# 
# ```{admonition} Eksempel: Ukjent rente
# :class: eksempel
# Tenk deg at du har 10.000 kr du skal sette av til sparing i 10 år. Det finnes forskjellige sparealternativer med ulik rente. Dersom vi lar $x$ være vekstfaktoren (se side om [eksponentialfunksjoner](eksponentialfunksjoner.ipynb)) renta gir, så vil funksjonen $f(x)=10000\cdot x^{10}$ gi hva sparebeløpet har vokst til etter 10 år.
# ```
# 
# 

# ## Utforsk
# Utforsk hvordan en potensfunksjon avhenger av størrelsene $a$ og $b$ ved å endre på de i vinduet under.

# In[1]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script>  \n    var params = {\n        "material_id": "nqwqdtps", \n        "appName": "graphing", \n        "width": 800, "height": 600, \n        "showToolBar": false, \n        "showAlgebraInput": false, \n        "showMenuBar": false,\n        "showResetIcon": true \n        };\n    var applet = new GGBApplet(params, false);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Introduksjon
# <iframe width="680" height="350" src="https://www.youtube.com/embed/Vk5XVQ3WoIs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
