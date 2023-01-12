#!/usr/bin/env python
# coding: utf-8

# # Oppgaver om rasjonale funksjoner og asymptoter
# 
# ```{admonition} Oppgave 1: Finn asymptotene
# :class: oppgave
# 
# **1)** Kan du finne den loddrette asymptoten kun ved å se på funksjonsuttrykket?
# 
# **2)** Kan du finne den vannrette asymptoten kun ved å se på funksjonsuttrykket?
# 
# Huk av for "Vis graf" eller "Vis asymptoter" om du trenger hjelp.
# ```

# In[28]:


get_ipython().run_cell_magic('html', '', '\n<!DOCTYPE html>\n<html>\n<head>\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n</head>\n<body>\n\n<script>\nvar views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\nvar parameters1 = {"id": "app1","width":1550,"height":600,"showMenuBar":false, "bordercolor": "#be8322","showAlgebraInput":false,"showToolBar":false,"customToolBar":"0 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24  20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49  50 , 71  14  68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6","showToolBarHelp":false,"showResetIcon":true,"enableLabelDrags":false,"enableShiftDragZoom":true,"enableRightClick":false,"errorDialogsActive":false,"useBrowserForJS":false,"allowStyleBar":false,"preventFocus":false,"showZoomButtons":true,"capturingThreshold":3,"appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },"showFullscreenButton":true,"scale":1,"disableAutoScale":false,"allowUpscale":false,"clickToLoad":false,"appName":"classic","buttonRounding":0.7,"buttonShadows":false,"language":"nb","ggbBase64":"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"};\nvar applet1 = new GGBApplet(parameters1, \'5.0\', views);\nvar parameters2 = {"id": "app1","width":1550,"height":800,"showMenuBar":false, "bordercolor": "#be8322","showAlgebraInput":false,"showToolBar":false,"customToolBar":"0 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24  20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49  50 , 71  14  68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6","showToolBarHelp":false,"showResetIcon":true,"enableLabelDrags":false,"enableShiftDragZoom":true,"enableRightClick":false,"errorDialogsActive":false,"useBrowserForJS":false,"allowStyleBar":false,"preventFocus":false,"showZoomButtons":true,"capturingThreshold":3,"appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },"showFullscreenButton":true,"scale":1,"disableAutoScale":false,"allowUpscale":false,"clickToLoad":false,"appName":"classic","buttonRounding":0.7,"buttonShadows":false,"language":"nb","ggbBase64":"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"};\nvar applet2 = new GGBApplet(parameters2, \'5.0\', views);\n\nwindow.addEventListener("load", function() {\n                    applet1.inject(\'applet_container1\');\n                    applet2.inject(\'applet_container2\');\n                 });\n\napplet.setPreviewImage(\'data:image/gif;base64,R0lGODlhAQABAAAAADs=\',\'https://www.geogebra.org/images/GeoGebra_loading.png\',\'https://www.geogebra.org/images/applet_play.png\');\n</script>\n\n</body>\n</html>\n\n')


# In[25]:


get_ipython().run_cell_magic('html', '', '\n<div id="applet_container1"></div>\n')


# ```{admonition} Oppgave 2: Finn koeffisientene
# :class: oppgave
# Endre på koeffisienten $a$, $b$, $c$ og $d$ for å se hvordan den rasjonale funksjonen $f(x)=\frac{ax+b}{cx+d}$ endrer seg.
# 
# Prøv å svare på følgende oppgaver:
# 
#  * Kan du få den loddrette asymptoten til å bli $x=2$ på forskjellige måter?
#  * Kan du finne en funksjon som har asymptoter $x=1$ og $y=2$?
#  * Hvordan kan du få loddrett asymptote lik $x=0$?
#  * Kan du få vannrett asymptote $y=0$? Hvorfor/hvorfor ikke?
#  * Hvilke av koeffisientene påvirker den loddrette asymptoten?
#  * Hvilke av koeffisientene påvirker den vannrette asymptoten?
# 
# ```

# In[26]:


get_ipython().run_cell_magic('html', '', '\n<div id="applet_container2"></div>\n')


# `````{admonition} Oppgave 3: Rasjonal funksjon med andregradsuttrykk
# :class: oppgave
# Funksjonen $f$ er gitt ved $f(x)=\frac{x^2+4x+4}{x^2-x-2}$
# 
# **a)** Finn asymptotene til funksjonen.\
# **b)** Skisser funksjonen. \
# **c)** Finn definisjonsmengden og verdimengden til funksjonen.
# 
# ````{admonition} Løsningsforslag
# :class: losning, dropdown
# **a)** Starter med å finne loddrette asymptoter. Det er nullpunktene til nevneren. Må da løse likningen:
# 
# $$x^2-x-2=0$$
# 
# Med abc-formelen får vi $x=-2 \vee x=1$ som også er likningene for de loddrette asymptotene.
# 
# Neste steg er å finne eventuelle vannrette asymptoter. Lar $x$ bli veldig stor. Da vil $x^2$-leddene dominere slik at: $f(x) \approx \frac{x^2}{x^2} = 1$
# 
# Vi har altså en vannrett asymptote for $y=1$.
# 
# **b)** Lager en enkel verditabell for noen verdier av funksjonen.
# 
# ```{figure} ./bilder/rasjonaltabell2.png
# ---
# scale: 40%
# ---
# ```
# 
# Merker av punktene og asymptotene. Det gir følgende skisse av grafen:
# ```{figure} ./bilder/rasjonalfunksjon2.png
# ---
# scale: 20%
# ---
# ```
# 
# **c)** Definisjonsmengden er alle tillatte verider for $x$. Vi kan bruke alle reelle tall utenom $x=-2$ og $x=1$. Det gir
# 
# $$D_f = \mathbf{R} \backslash \{-2, 1\}$$
# 
# Vi ser at funksjonsgrafen krysser den vannrette asymptoten. Den er derfor med i verdimengden. Vi ser imidlertid at det er et område funksjonen ikke dekker. Dette området ligger mellom punktene $A$ og $B$ markert i figuren under.
# 
# ```{figure} ./bilder/rasjonalverdimengde.png
# ---
# scale: 40%
# ---
# ```
# 
# Verdimengden blir derfor $V_f = \mathbf{R}\backslash \langle -1.78, 0 \rangle$
# 
# ````
# 
# `````
