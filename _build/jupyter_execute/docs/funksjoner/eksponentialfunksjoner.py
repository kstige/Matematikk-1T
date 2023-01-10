#!/usr/bin/env python
# coding: utf-8

# # Eksponentialfunksjoner
# 
# En funksjonstype som kan likne litt på potensfunksjoner er eksponentialfunksjoner. Det er imidlertid viktig å kunne skille de fra hverandre. Der variabelen $x$ i potensfunksjoner er grunntallet i en potens, vil variabelen i en eksponentialfunksjon befinne seg i eksponenten.
# 
# ```{admonition} Definisjon av potensfunksjoner
# :class: def
# Eksponentialfunksjoner kan skrives på formen $f(x)=a\cdot b^x$, der $b>0$.
# 
# Vi ser at $a$ er funksjonsverdien når $x=0$, mens $b$ er en vekstfaktor. Eksponentialfunksjonen viser ern utvikling som endrer seg med en fast prosentstørrelse fo hver periode. Vi sier at funksjonen $f$ endrer seg eksponentielt.
# ```
# 
# Vekstfaktor er et begrep vi kjenner fra prosentregning.
# 
# ```{admonition} Definisjon av vekstfaktor
# :class: def
# Dersom en størrelse øker eller minker med $p$ % vil vekstfaktoren være gitt ved $1\pm \frac{p}{100}$ der $+$ er ved økning og $-$ er ved nedang.
# 
# Når vi kjenner vekstfaktoren kan vi finne ny verdi ved
# 
# $$
# \begin{align*} 
# \! N &= \qquad G && \cdot & V \\ 
# \textrm{ny verdi} &= \textrm{gammel verdi} && \cdot &\textrm{vekstfaktor}
# \end{align*}
# $$
# 
# Når en størrelse endrer seg med samme prosent over flere perioder (f.eks. år) vil vi kunne regne ut ny verdi fra gammel verdi med:
# 
# $$
# N = G\cdot V^{\text{antall perioder}}
# $$
# 
# Dersom vi kaller ny verdi $f(x)$, gammel verdi $a$, vekstfaktor $b$ og antall perioder for $x$ ser vi at dette er akkurat formen til eksponentialfunksjonen.
# ```
# 
# 

# ```{admonition} Eksempel: Renteregning
# :class: eksempel, dropdown
# 
# Du setter 20000 kr inn i banken til fastrente på 2,0 % for hvert år. Det her kan beskrives ved hjelp av en eksponentialfunksjon med startfunksjon 20000 og vekstfaktor $1+\frac{2}{100}=1,02$. Eksponentialfunksjonen blir
# 
# $$f(x)=20000\cdot 1,02^x$$
# 
# der $x$ er antall år etter at du setter inn pengene. 

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 10, 100)
y = 20000*1.02**x

plt.plot(x, y)
plt.xlabel("x antall år")
plt.ylabel("f(x) kr")
plt.ylim(0, 26000)
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")
plt.grid()
plt.show()

