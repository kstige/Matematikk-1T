#!/usr/bin/env python
# coding: utf-8

# # Arealsetningen
# 
# Vi vet fra før at arealet til en trekant er gitt ved halvparten av grunnlinja multiplisert med høyden. Her skal vi se på hvordan vi kan utnytte de trigonomeriske formlene til å finne areal for trekanter vi før ikke har kunnet regne på.
# 
# Vi starter med å se på en trekant med spisse vinkler og tenker oss at sidene $b$, $c$ og vinkelen $u$ på figuren under er kjent. Kan vi da finne arealet?.
# 
# ```{figure} ./bilder/arealsetningen1.png
# ---
# scale: 40%
# align: right
# ---
# ```
# 
# Dersom vi velger $c$ som grunnlinje, så ser vi at vi mangler $h$ i den *vanlige formelen$ for areal til en trekant. Men om vi bruker det vi kan om sinus, så ser vi at
# 
# $\sin u = \frac{h}{b}$
# 
# som gir oss
# 
# $h=b\sin u$.
# 
# Vi kan derfor regne ut arealet ved: $\text{Areal}=\frac{1}{2}\cdot c \cdot h = \frac{1}{2}\cdot b\cdot c\cdot \sin u$. Det går an å vise at vi får tilsvarende uttrykk ved å ta utgangspunkt i andre sider i trekanten. Dette arealsetningen.
# 
# `````{admonition} Arealsetningen
# 
# Vi kan finne arealet til en trekant ved å regne ut halvparten av produktet mellom to sider og sinus til vinkelen mellom dem.
# 
# ```{figure} ./bilder/arealsetningen.png
# ---
# scale: 30%
# align: right
# ---
# ```
# 
#  * $\text{Areal} = \frac{1}{2}bc\sin A$
#  * $\text{Areal} = \frac{1}{2}ac\sin B$
#  * $\text{Areal} = \frac{1}{2}ab\sin C$
# 
# Som vi viser i eksempelet under, så gjelder arealsetningen også for trekanter med en stump vinkel.
# `````
# 
# `````{admonition} Arealsetningen for trekant med stump vinkel
# :class: eksempel, dropdown
# 
# Vi ser på trekanten til høyre og lar $b$, $c$ og $u$ være kjent. Vi velger $c$ som grunnlinje og starter med å finne et uttrykk for høyden $h$.
# 
# ```{figure} ./bilder/arealsetningen2.png
# ---
# scale: 30%
# align: right
# ---
# ```
# 
# Vi ser på den hvite trekanten som ligger mellom $\bigtriangleup ABC$ og $h$. Den har vinkelen $180^{\circ}-u$ som er supplementvinkelen til $u$. Videre bruker vi at sinus til supplementvinkler er like.
# 
# $\sin (180^{\circ}-u) = \sin u = \frac{h}{b}$
# 
# Det gir som før at $h=b\sin u$. Setter vi det inn i formelen for arealet til en trekant, så får vi:
# 
# $\text{Areal}=\frac{1}{2}c \cdot h = \frac{1}{2}bc\sin u$
# `````
# 
# En konsekvens av måten vi regner ut arealet til en trekant på er at dersom de tre punktene som definerer trekanten ligger på to parallelle linjer, så vil arealet være det samme om vi flytter det punktet som ligger alene langs linja. Prøv det i appen under.

# In[1]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 1,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":false,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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",\n    };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# ## Bruk av arealsetningen
# 
# 
# `````{admonition} Eksempel: Kjent areal, ukjent vinkel
# :class: eksempel
# 
# En trekant har arealet 16, $AB=8$ og $AC=6$. Hvor stor er vinkel $A$?
# 
# Vi starte med å lage ei skisse av problemet. Da vil vi kunne oppdage at her er det faktisk to trekanter som oppfyller kravene i oppgava.
# 
# ```{figure} ./bilder/kjentareal.png
# ---
# scale: 40%
# ---
# ```
# 
# For å løse problemet tar vi utgangspunkt i arealsetningen. Vi kaller arealet $A_{\bigtriangleup}$ for å ikke blande med vinkel $A$.
# 
# $$
# A_{\bigtriangleup}=\frac{1}{2}bc\sin A \\
# \sin A = \frac{2A_{\bigtriangleup}}{bc} = \frac{2\cdot 16}{6\cdot 8}=\frac{2}{3}\\
# \angle A = \sin^{-1}\frac{2}{3}\approx 41,8^{\circ}
# $$
# 
# Her har vi fått vinkelen i trekanten til venstre, men hvordan kan vi få trekanten til høyre? Hvis vi husker at sinus til supplementvinkler er lik, så får vi at den andre vinkelen er $180^{\circ}-41,8^{\circ}=138,2^{\circ}$
# 
# `````
