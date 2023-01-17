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

# In[2]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script>\nvar views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\nvar parameters1 = {\n   "width":1550, "height":600, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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"\n   };\nvar applet1 = new GGBApplet(parameters1, \'5.0\', views);\nvar parameters1 = {"width":1550,\n   "height":600, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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"\n   };\nvar applet2 = new GGBApplet(parameters2, \'5.0\', views);\n\nwindow.addEventListener("load", function() {\n                    applet1.inject(\'applet_container1\');\n                    applet2.inject(\'applet_container2\');\n                 });\n\napplet.setPreviewImage(\'data:image/gif;base64,R0lGODlhAQABAAAAADs=\',\'https://www.geogebra.org/images/GeoGebra_loading.png\',\'https://www.geogebra.org/images/applet_play.png\');\n</script>\n\n</body>\n</html>\n\n')


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
