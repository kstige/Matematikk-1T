#!/usr/bin/env python
# coding: utf-8

# # Kvadratsetningene
# 
# Vi har nå sett på hvordan vi trekker sammen algebrauttrykk og hvordan vi multipliserer ut parenteser. Noen former for parentesuttrykk dukker opp så ofte at vi har gitt dem egne navn.
# 
# ```{admonition} Kvadratsetningene
# 
# **Første kvadratsetning:** $(a+b)^2=a^2+2ab+b^2$
# 
# **Andre kvadratsetning:** $(a-b)^2=a^2-2ab+b^2$
# 
# **Konjugatsetningen:** $(a+b)(a-b)=a^2-b^2$
# 
# Konjugatsetningen blir av og til også kalt for *tredje kvadratsetning*.
# ```
# 
# Sammenhengene over kan enkelt bevises ved å skrive ut kvadratene og multiplisere sammen parentesene. Det viser vi for første kvadratsetning i eksempelet under.
# 
# ```{admonition} Eksempel: Første kvadratsetning
# :class: eksempel
# 
# Vi skal regne ut $(x+4)^2$ med og uten første kvadratsetning.
# 
# **Uten**
# 
# $(x+4)^2=(x+4)\cdot (x+4)=x^2+4x+4x+16=x^2+8x+16$
# 
# **Med**
# 
# $(x+4)^2=x^2+2\cdot 4x +4^2=x^2+8x+16$
# ```
# 
# Eksempelet over viser at det i enkle tilfeller ikke er så mye tid å spare på å bruke kvadratsetningene. Fordelen kommer når uttrykkene i parentesene blir mer sammensatte. I tillegg vil den største nytten komme i å bruke kvadratsetningene baklengs, det vil si til faktorisering.
# 
# ```{admonition} Eksempel: Sammensatte kvadrater
# :class: eksempel
# 
# $(2a+3)^2=(2a)^2+2\cdot 2a\cdot 3+3^2=4a^2+12a+9$
# 
# $\displaystyle{\left(\frac{x}{3}-3y\right)^2 = \left(\frac{x}{3}\right)^2-2\cdot\frac{x}{3}\cdot 3y+(3y)^2=\frac{x^2}{9}-2xy+9y^2}$
# 
# $(\sqrt{5}+2)(\sqrt{5}-2)=(\sqrt{5})^2-2^2=5-4=1$
# ```

# ## Illustrasjon av første kvadratsetning
# 
# Vi kan bruke figuren under for å både bevise og illustrere første kvadratsetning.
# 
# ```{figure} ./bilder/1kvadratsetning.png
# ---
# scale: 50%
# ---
# ```
# 
# Sidene i kvadratet er $a+b$, så arealet av kvadratet er $(a+b)^2$. Vi kan imidlertid også skrive arealet ved hjelp av firkantene som den er delt opp i.
# 
# Blå firkant: $a^2$
# 
# Grønne firkatner: $2ab$
# 
# Rødbrun firkant: $b^2$
# 
# Vi ser da at $(a+b)^2=a^2+2ab+b^2$.
# 
# Tilsvarende illustrasjoner og bevis kan gjøres også for andre kvadratsetning og konjugatsetningen.
# 
# ## Øving på kvadratsetningene
# I appen under kan du øve på oppgaver om kvadratsetningene.

# In[1]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script>\nvar views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 0,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\nvar parameters1 = {\n   "width":800, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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",\n   };\nvar applet1 = new GGBApplet(parameters1, \'5.0\', views);\n\nwindow.addEventListener("load", function() {\n                    applet1.inject(\'applet_container1\');\n                 });\n\napplet.setPreviewImage(\'data:image/gif;base64,R0lGODlhAQABAAAAADs=\',\'https://www.geogebra.org/images/GeoGebra_loading.png\',\'https://www.geogebra.org/images/applet_play.png\');\n</script>\n\n<div id="applet_container1"></div>\n')

