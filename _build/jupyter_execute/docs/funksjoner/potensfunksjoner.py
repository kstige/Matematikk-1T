#!/usr/bin/env python
# coding: utf-8

# # Potensfunksjoner
# 
# I polynomfunksjoner kan eksponenten kun være et heltall større eller lik 0. Det er imidlertid ingenting i veien for å ha negative tall eller desimaltall i en eksponent.
# 
# ```{admonition} Definisjon av potensfunksjoner
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
# ```{admonition} Eksempel på potensfunksjoner
# :class: eksempel
# Formen på en potensfunksjon avhenger av størrelsene $a$ og $b$. Under er funksjonen $f(x)=2x^b$ tegnet inn (for positive $x$-verdier) for noen forskjellige verdier av $b$.
# 
# ```{figure} ./bilder/potensfunksjon.png
# ---
# scale: 20%
# ---
# ```
# 
# 

# 

# ## Utforsk
# Utforsk hvordan en potensfunksjon avhenger av størrelsene $a$ og $b$ ved å endre på de i vinduet under.

# In[1]:


get_ipython().run_cell_magic('html', '', '\n<script src="https://www.geogebra.org/apps/deployggb.js"></script>\n\n<script>  \n    var params = {\n        "material_id": "nqwqdtps", \n        "appName": "graphing", \n        "width": 800, "height": 600, \n        "showToolBar": false, \n        "showAlgebraInput": false, \n        "showMenuBar": false,\n        "showResetIcon": true \n        };\n    var applet = new GGBApplet(params, false);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# In[ ]:




