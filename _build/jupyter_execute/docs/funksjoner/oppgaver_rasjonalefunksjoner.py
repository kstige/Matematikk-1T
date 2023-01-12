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

# In[24]:


get_ipython().run_cell_magic('html', '', '\n<!DOCTYPE html>\n<html>\n<head>\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n</head>\n<body>\n\n<script>\nvar views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\nvar parameters1 = {"id": "app1","width":1550,"height":800,"showMenuBar":false, "bordercolor": "#be8322","showAlgebraInput":false,"showToolBar":false,"customToolBar":"0 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24  20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49  50 , 71  14  68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6","showToolBarHelp":false,"showResetIcon":true,"enableLabelDrags":false,"enableShiftDragZoom":true,"enableRightClick":false,"errorDialogsActive":false,"useBrowserForJS":false,"allowStyleBar":false,"preventFocus":false,"showZoomButtons":true,"capturingThreshold":3,"appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },"showFullscreenButton":true,"scale":1,"disableAutoScale":false,"allowUpscale":false,"clickToLoad":false,"appName":"classic","buttonRounding":0.7,"buttonShadows":false,"language":"nb","ggbBase64":"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"};\nvar applet1 = new GGBApplet(parameters1, \'5.0\', views);\nvar parameters2 = {"id": "app1","width":1550,"height":800,"showMenuBar":false, "bordercolor": "#be8322","showAlgebraInput":false,"showToolBar":false,"customToolBar":"0 73 62 | 1 501 67 , 5 19 , 72 75 76 | 2 15 45 , 18 65 , 7 37 | 4 3 8 9 , 13 44 , 58 , 47 | 16 51 64 , 70 | 10 34 53 11 , 24  20 22 , 21 23 | 55 56 57 , 12 | 36 46 , 38 49  50 , 71  14  68 | 30 29 54 32 31 33 | 25 17 26 60 52 61 | 40 41 42 , 27 28 35 , 6","showToolBarHelp":false,"showResetIcon":true,"enableLabelDrags":false,"enableShiftDragZoom":true,"enableRightClick":false,"errorDialogsActive":false,"useBrowserForJS":false,"allowStyleBar":false,"preventFocus":false,"showZoomButtons":true,"capturingThreshold":3,"appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },"showFullscreenButton":true,"scale":1,"disableAutoScale":false,"allowUpscale":false,"clickToLoad":false,"appName":"classic","buttonRounding":0.7,"buttonShadows":false,"language":"nb","ggbBase64":"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"};\nvar applet2 = new GGBApplet(parameters2, \'5.0\', views);\n\nwindow.addEventListener("load", function() {\n                    applet1.inject(\'applet_container1\');\n                    applet2.inject(\'applet_container2\');\n                 });\n\napplet.setPreviewImage(\'data:image/gif;base64,R0lGODlhAQABAAAAADs=\',\'https://www.geogebra.org/images/GeoGebra_loading.png\',\'https://www.geogebra.org/images/applet_play.png\');\n</script>\n\n</body>\n</html>\n\n')


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
