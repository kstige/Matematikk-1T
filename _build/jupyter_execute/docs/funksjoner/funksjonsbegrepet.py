#!/usr/bin/env python
# coding: utf-8

# # Funksjonsbegrepet
# 
# En funksjon er en regel som sier noe om to tall som hører sammen. Regelen, $f$, gir deg et tall $f(x)$ for hvert tall $x$ vi setter inn.
# 
# ```{admonition} Definisjon av funksjon
# :class: def
# Når hver verdi av $x$ vi putter inn gir oss en verdi for $f(x)$ ut, så sier vi at $f$ er en funksjon av $x$.
# ```
# 
# ```{admonition} Eksempel: Funksjoner
# :class: eksempel, dropdown
# 
# $$
# f(x)=3x+2 \\
# g(x)=\sqrt{2x+4} \\
# g(x)=\frac{2}{x}
# $$
# 
# I alle tilfellene over har vi funksjoner siden vi for hver verdi av $x$ vil få ut en verdi for $f(x)$.
# ```
# 
# ## Representasjonsmetoder
# Alle funksjoner kan representeres på tre måter:
# 
# -   Funksjonsuttrykk
# -   Verditabell
# -   Graf
# 
# Et funksjonsuttrykk kan være $f(x) = 3x + 2$. For denne funksjonen kan vi lage en verditabell:
# | **x**    | -1 | 0 | 1 | 2 |
# |----------|----|---|---|---|
# | **f(x)** | -1 | 2 | 5 | 8 |
# 
# Og vi kan ha en graf:
# 

# In[17]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)
y = 3*x +2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-4, 8)
plt.xticks(np.arange(-2, 3, 0.5))
plt.yticks(np.arange(-4, 8))
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")
plt.grid()
plt.show()


# 
# ## Definisjonsmengde
# Definisjosmengden til en funksjon er alle verdier for $x$ som vi kan sette inn i variabelen. 
# 
# ```{admonition} Eksempler på definisjonsmengde
# :class: eksempel, dropdown
# Funksjonen $f(x)= 3x + 2$ har definisjonsmengde $D_f = \mathbf{R}$ siden vi kan sette inn alle reelle tall for $x$.
# 
# Funksjonen $g(x) = \sqrt{2x+4}$ har definisjonsmengde $D_g = \left[-2, \rightarrow\right>$ siden vi ikke kan ta kvadratrota av et negativt tall.
# 
# Funksjonen $h(x)=\frac{2}{x}$ har definisjonsmengde $D_h = \mathbf{R} \, \backslash \, \{0\}$ siden vi kan sette inn alle reelle tall utenom $0$.
# ```
# 
# Vi kan velge en definisjonsmengde som er mindre enn den vi finner ved å se på lovlige verdier for $x$. Dersom funksjonen $f(x)=80x$ viser hvor langt en bil har kjørt etter $x$ timer vil definisjonsmengden starte ved $x=0$ selv om det fint går an å sette negative verdier inn i funksjonen.
# 
# ## Verdimengde
# Verdimengden til en funksjon er alle verdier vi kan få ut av funksjonen.
# 
# ```{admonition} Eksempler på verdimengde
# :class: eksempel, dropdown
# Funksjonen $f(x)= 3x + 2$ har verdimengde $V_f = \mathbf{R}$ siden vi kan få ut alle reelle tall fra funksjonen.
# 
# Funksjonen $g(x) = \sqrt{2x+4}$ har verdimengde $V_g = \left[0, \rightarrow\right>$ siden kvadratrota ikke kan være negativ.
# 
# Funksjonen $h(x)=\frac{2}{x}$ har verdimengde $D_h = \mathbf{R} \, \backslash \, \{0\}$ siden vi kan få ut alle reelle tall utenom $0$.
# ```
# 
# 

# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Funksjonsbegrepet
# <iframe width="800" height="600" src="https://www.youtube.com/embed/ajiYu0oFwJo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ```{tab-item} Definisjons- og verdimengde
# <iframe width="800" height="600" src="https://www.youtube.com/embed/tuw28VOvGO4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
