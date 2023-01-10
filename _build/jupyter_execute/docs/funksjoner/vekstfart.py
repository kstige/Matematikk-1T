#!/usr/bin/env python
# coding: utf-8

# # Vekstfart
# 
# For lineære funksjoner har vi sett på stigningstallet. Det forteller hvor raskt funksjonen endrer seg. Det som er spesielt med lineære funksjoner er at de endrer seg med dette samme stigningstallet hele tiden. Stigningstallet kan også kalles vekstfarten til den lineære funksjoner.
# 
# Andre funksjonstyper har ikke et stignignstall, men det kan allikevel være nyttig å se på vekstfarten til funksjonen. Vi tar utgangspunkt i definisjonen av vekstfarten (stigningstallet) til en lineær funksjon når vi definerer det vi vil kalle gjennomsnittlig vekstfart.
# 
# ```{admonition} Definisjon av gjennomsnittlig vekstfart
# For å finne den gjennomsnittlige vekstfarten til funksjonen $f(x)$ på intervallet $[x_1, x_2]$ bruker vi
# 
# $$
# \frac{\Delta f(x)}{\Delta x} = \frac{f(x_2)-f(x_1)}{x_2-x_1}
# $$
# 
# Dette er det samme som stigningstallet til den rette linja gjennom punktene $(x_1, f(x_1))$ og $(x_2, f(x_2))$.
# 
# Vekstfarten har en enhet som er gitt ved enheten til $f(x)$ delt på enheten til $x$.
# ```

# In[14]:


get_ipython().run_cell_magic('html', '', '\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<div id="ggb-point"></div>\n\n<script>\n  var ggbApp = new GGBApplet({\n      "height": 400,\n      "showToolBar": true,\n      "showMenuBar": true,\n      "showAlgebraInput": false,\n      "showResetIcon": true,\n      "enableLabelDrags": false,\n      "enableRightClick": false,\n      "enableShiftDragZoom": true,\n      "useBrowserForJS": false,\n      "material_id": "uh5nffph"\n  }, \'ggb-point\');\n\n  ggbApp.inject();\n</script>\n')

