#!/usr/bin/env python
# coding: utf-8

# # Enhetssirkelen
# 
# Definisjonen vi har brukt for sinus, cosinus og tangens har tatt utgangspunkt i rettvinklede trekanter. Derfor gjelder de kun på såkalte spisse vinkler (vinkler mindre enn $90^{\circ}$). Her skal vi gi en utvidet definisjon som også gjelder for vinkler større enn $90^{\circ}$.
# 
# Til det bruker vi det vi kaller for *enhetssirkelen*. Det er en sirkel med radius 1 og sentrum i origo. Vi tegner inn en rettvinklet trekant i sirkelen slik at hypotenusen går mellom origo og et punkt på sirkelbuen. Hypotenusen vil da ha lengde 1.
# 
# `````{admonition} Generell definisjon av de trigonometriske forholdene
# Vi lar vinkelen $u$ ha toppunkt i origo, det ene vinkelbeinet langs $x$-aksen og det andre vinkelbeinet langs et linjestykke mellom origo og sirkelbuen. Vinkelen $u$ går mot klokka. Koordinatene til skjæringspunktet mellom enhetssirkelen og vinkelbeinet definerer vi til $(\cos u, \sin u)$.
# 
# ```{figure} ./bilder/enhetssirkelen.png
# ---
# scale: 40%
# ---
# ```
# 
# Vi definerer da
# 
#  * $\sin u$ er $y$-koordinaten til skjæringspunktet
#  * $\cos u$ er $x$-koordinaten til skjæringspunktet
#  * $\tan u = \frac{\sin u}{\cos u}$
# 
# `````
# 
# Bruk appen under og la vinkelen være en vanlig spiss vinkel og kontroller at denne nye definisjonen stemmer med den opprinnelige definisjonen vi har brukt.
# 
# 

# In[2]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 1,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"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",\n    };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# ## Noen spesielle vinkelkombinasjoner
# 
# Det er noen kombinasjoner av vinkler som kan være verdt å merke seg.
# 
# ```{admonition} Supplement- og komplementvinkler
# Supplementvinkler er to vinkler som blir $180^{\circ}$ tilsammen (f.eks. $120^{\circ}$ og $60^{\circ}$).
# 
# Komplementvinkler er to vinkler som blir $90^{\circ}$ tilsammen (f.eks. $30^{\circ}$ og $60^{\circ}$).
# ```
# 
# I oppgavene under skal du se på sammenhengen mellom sinus og cosinus til supplement- og komplementvinkler.
# 
# `````{admonition} Undersøk supplementvinkler
# :class: oppgave
# 
# Lag en tabell tilsvarende tabellen under
# 
# $$\begin{array}{|l|l|l|l|l|l|}
# \hline
# u         & 180^{\circ}-u & \sin u & \sin(180^{\circ}-u) & \cos u & \cos(180^{\circ}-u) \\ \hline
# 30^{\circ} & & & & & \\ \hline
# 55^{\circ} & & & & & \\ \hline
# 81^{\circ} & & & & & \\ \hline
# \end{array}$$
# 
# Bruk appen over eller CAS til å fylle ut tabellen.
# 
# Finner du noen sammenhenger mellom
# 
#  * $\sin u$ og $\sin(180^{\circ}-u)$?
#  * $\cos u$ og $\cos(180^{\circ}-u)$?
# 
# ```{admonition} Løsningsforslag
# :class: losning, dropdown
# 
# $$\begin{array}{|l|l|l|l|l|l|}
# \hline
# u          & 180^{\circ}-u & \sin u & \sin(180^{\circ}-u) & \cos u & \cos(180^{\circ}-u) \\ \hline
# 30^{\circ} & 150^{\circ}   & 0,5    & 0,5                 & 0,87   & -0,87               \\ \hline
# 55^{\circ} & 125^{\circ}   & 0,82   & 0,82                & 0,57   & -0,57               \\ \hline
# 81^{\circ} & 99^{\circ}    & 0,99   & 0,99                & 0,16   & -0,16               \\ \hline
# \end{array}$$
# 
# Vi ser at sinus til supplementvinkler er lik. Det betyr at om vi kjenner sinus til en vinkel, så kan vi ikke være sikker på hvilken vinkel vi har ($u$ eller $180^{\circ}-u$). Dersom vi løser ei oppgave med kjent sinus-verdi kan det derfor være lurt å tegne opp trekanten for å se hvilken vinkel vi skal ha.
# 
# Vi ser videre at cosinus til supplementvinkler har samme absoluttverdi, men motsatt fortegn.
# ```
# `````
# 
# `````{admonition} Undersøk komplementvinkler
# :class: oppgave
# 
# Lag en tabell tilsvarende tabellen under
# 
# $$\begin{array}{|l|l|l|l|l|l|}
# \hline
# u         & 90^{\circ}-u & \sin u & \sin(90^{\circ}-u) & \cos u & \cos(90^{\circ}-u) \\ \hline
# 30^{\circ} & & & & & \\ \hline
# 55^{\circ} & & & & & \\ \hline
# 81^{\circ} & & & & & \\ \hline
# \end{array}$$
# 
# Bruk appen over eller CAS til å fylle ut tabellen.
# 
# Finner du noen sammenhenger her.
# 
# ```{admonition} Løsningsforslag
# :class: losning, dropdown
# 
# $$\begin{array}{|l|l|l|l|l|l|}
# \hline
# u          & 90^{\circ}-u & \sin u & \sin(90^{\circ}-u) & \cos u & \cos(90^{\circ}-u) \\ \hline
# 30^{\circ} & 60^{\circ}   & 0,5  & 0,87 & 0,87 & 0,5  \\ \hline
# 55^{\circ} & 35^{\circ}   & 0,82 & 0,57 & 0,57 & 0,82 \\ \hline
# 81^{\circ} & 9^{\circ}    & 0,99 & 0,16 & 0,16 & 0,99 \\ \hline
# \end{array}$$
# 
# Vi ser at $\sin u = \cos(90^{\circ}-u)$ og $\cos u = \sin(90^{\circ}-u)$. Ved å se på en rettvinklet trekant å bruke den "gamle" definisjonen på sinus og cosinus for hver av vinklene, så kan vi kanskje overbevise oss om at det må være slik.
# ```
# `````
