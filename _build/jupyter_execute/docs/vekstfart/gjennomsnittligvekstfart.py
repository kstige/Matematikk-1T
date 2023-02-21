#!/usr/bin/env python
# coding: utf-8

# # Gjennomsnittlig vekstfart
# 
# For lineære funksjoner har vi sett på stigningstallet. Det forteller hvor raskt funksjonen endrer seg. Det som er spesielt med lineære funksjoner er at de endrer seg med dette samme stigningstallet hele tiden. Stigningstallet kan også kalles vekstfarten til den lineære funksjoner.
# 
# Andre funksjonstyper har ikke et stignignstall, men det kan allikevel være nyttig å se på vekstfarten til funksjonen. Vi tar utgangspunkt i definisjonen av vekstfarten (stigningstallet) til en lineær funksjon når vi definerer det vi vil kalle gjennomsnittlig vekstfart.
# 
# `````{admonition} Definisjon: Gjennomsnittlig vekstfart
# :class: def
# For å finne den gjennomsnittlige vekstfarten til funksjonen $f(x)$ på intervallet $[x_1, x_2]$ bruker vi
# 
# $$
# \frac{\Delta f(x)}{\Delta x} = \frac{f(x_2)-f(x_1)}{x_2-x_1}
# $$
# 
# Dette er det samme som stigningstallet til den rette linja gjennom punktene $(x_1, f(x_1))$ og $(x_2, f(x_2))$.
# 
# Vekstfarten har en enhet som er gitt ved enheten til $f(x)$ delt på enheten til $x$.
# 
# ```{figure} ./bilder/vekstfart.png
# ---
# scale: 40%
# ---
# ```
# `````

# ```{admonition} Eksempel: Gjennomsnittlig vekstfart for hånd
# :class: eksempel
# 
# Vi ser på funksjonen $f(x)=x^2 +2x-1$ og skal finne gjennomsnittlig vekstfart i intervallene $x\in[2, 4]$ og $x\in[-3,1]$.
# 
# Gjennomsnittlig vekstfart i $[2, 4]$:
# 
# $$
# \frac{\Delta f(x)}{\Delta x} = \frac{f(4)-f(2)}{4-2}=\frac{(4^2+2\cdot 4-1)-(2^2+2\cdot 2-1)}{2}=\frac{23-7}{2}=8
# $$
# 
# Gjennomsnittlig vekstfart i $[-3, 1]$:
# 
# $$
# \begin{align*}
# \frac{\Delta f(x)}{\Delta x} = \frac{f(1)-f(-3)}{1-(-3)} &=\frac{(1^2+2\cdot 1-1)-((-3)^2+2\cdot (-3)-1)}{4} \\
# &=\frac{2-2}{4}=0
# \end{align*}
# $$
# 
# I det siste intervallet er den gjennomsnittlige vekstfarten lik 0. Det betyr ikke at det ikke skjer noen endring i funksjonen inne i intervallet, men at funksjonen har samme verdi for start- og sluttverdien i intervallet.
# ```
# 
# I GeoGebra-appen under kan du skrive inn ulike funksjoner og endre intervallet den gjennomsnittlige vekstfarten skal regnes ut for. Utregning vises på høyre side. Bruk appen til å finne den gjennomsnittlige vekstfarten i eksempelet over.

# In[10]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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"\n   };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Introduksjon
# <iframe width="680" height="350" src="https://www.youtube.com/embed/arxmvGGeFdU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ```{tab-item} Eksempel i GeoGebra
# <iframe width="680" height="350" src="https://www.youtube.com/embed/CDjh7ENzTQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
