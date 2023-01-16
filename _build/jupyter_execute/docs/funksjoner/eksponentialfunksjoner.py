#!/usr/bin/env python
# coding: utf-8

# # Eksponentialfunksjoner
# 
# Eksponentialfunksjoner er en funksjonstype som viser størrelser som endrer seg med en fast prosentstørrelse for hver tidsperiode.
# 
# ```{admonition} Definisjon: Eksponentialfunksjoner
# :class: def
# Eksponentialfunksjoner kan skrives på formen $f(x)=a\cdot b^x$, der $b>0$.
# 
# Vi ser at $a$ er funksjonsverdien når $x=0$ (skjæringspunktet med $y$-aksen), mens $b$ er en vekstfaktor. Eksponentialfunksjonen viser en utvikling som endrer seg med en fast prosentstørrelse for hver periode. Det kalles en eksponentiell endring.
# 
#  * Om $0<b<1$ vil funksjonen være avtagende.
#  * Om $b>1$ vil funksjonen være stigende.
# ```
# 
# Vekstfaktor er et begrep vi kjenner fra prosentregning.
# 
# ```{admonition} Definisjon: Vekstfaktor
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

# `````{admonition} Eksempel: Renteregning
# :class: eksempel, dropdown
# 
# Du setter 20000 kr inn i banken til fastrente på 3,0 % for hvert år. Det her kan beskrives ved hjelp av en eksponentialfunksjon med startverdi 20000 og vekstfaktor $1+\frac{3}{100}=1,03$. Eksponentialfunksjonen blir
# 
# $$f(x)=20000\cdot 1,03^x$$
# 
# der $x$ er antall år etter at du setter inn pengene. Vi tegner grafen til funksjonen
# 
# ```{figure} ./bilder/renter.png
# ---
# scale: 20%
# align: center
# ---
# ```
# 
# Vi ser at funksjonen stiger raskere og raskere. Det er på grunn av at vi hele tiden også får renter av rentene. Penger du setter i banken gir altså et eksempel på eksponentiell vekst.
# `````

# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Introduksjon
# <iframe width="800" height="600" src="https://www.youtube.com/embed/_7Ioav29USE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
