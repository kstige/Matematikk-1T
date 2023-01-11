#!/usr/bin/env python
# coding: utf-8

# # Rasjonale funksjoner
# 
# Vi husker at et rasjonalt tall er et tall som kan skrives som en brøk med heltall i teller og nevner. Tilsvarende vil vi definere rasjonale funksjoner på følgende måte.
# 
# ```{admonition} Definisjon av rasjonale funksjoner
# :class: def
# En brøkfunksjon som har polynomfunksjoner i både teller og nevner kalles en rasjonal funksjon.
# ```
# 
# Rasjonale funksjoner skiller seg blant annet fra polynomfunksjoner ved at noen $x$-verdier ikke er med i definisjonsmengden. Det er de verdiene for $x$ som gjør at nevneren blir 0. Slike verdier gir grafen loddrette asymptoter. Det er loddrette linjer som grafen beveger seg mot, men aldri vil krysse. I tillegg vil rasjonale funksjoner også ha vannrette (eller skrå asymptoter).
# 
# ```{admonition} Loddrett/vertikal asymptote
# :class: def
# En rasjonal funksjon har loddrette asymptoter for de $x$-verdiene der nevneren har nullpunkt. Om $x=a$ er et nullpunkt vil $x=a$ også være en asymptote.\
# Dersom telleren har nullpunkt for samme $x$-verdi må funksjonen undersøkes nærmere for å kunne si om det er en loddrett asymptote.
# ```
# 
# ```{admonition} Vannrett/horisontal asymptote
# :class: def
# En rasjonal funksjon har vannrett asymptote for $y=b$ dersom grafen nærmer seg $b$ når $x$ går mot $\pm \infty$. 
# ```
# 
# `````{admonition} Eksempel: Rasjonal funksjon og asymptoter
# :class: eksempel, dropdown
# 
# Under er et bilde av grafen til den rasjonale funksjonen $f(x)=\frac{2x+1}{x-3}$. Det er også tegnet inn en loddrett asymptote for $x=3$ og en vannrett asymptote for $y=2$. Vi ser at grafen nærmer seg disse linjene fra begge sider uten å krysse dem.
# 
# ```{figure} ./bilder/rasjonalfunksjon.png
# ---
# scale: 20%
# ---
# ```
# For å finne den loddrette asymptoten finner vi nullpunktet til nevneren. Siden nevneren er $x-3$ ser vi at nullpunktet og dermed den loddrette asymptoten er $x=3$. Det vil si at definisjonsmengden til funksjonen blir $D_f = \mathbf{R} \backslash \{3\}$
# 
# For å finne den vannrette asymptoten tenker vi oss at vi lar $x\rightarrow \infty$ ($x$ går mot uendelig). Da vil alle ledd i brøken som ikke inneholder $x$ bli veldig små i forhold til leddene som inneholder $x$. 
# 
# $$
# f(x)=\frac{2x+1}{x-3} \approx \frac{2x}{x}=2
# $$
# 
# når $x$ blir stor. Det vil si at $y=2$ er en vannrett asymptote. Vi ser av grafen at funksjonen aldri krysser denne linja, så verdimengden til funksjonen blir $V_f=\mathbf{R} \backslash \{2\}$.
# `````

# `````{admonition} Eksempel: Skisser rasjonal funksjon
# :class: eksempel, dropdown
# 
# En rasjonal funksjon er gitt ved $g(x)=\frac{3x}{2x+2}$. Vi skal finne asymptotene og skissere grafen.
# 
# Den loddrette asymptoten finner vi der nevneren er 0. Det er når $x=-1$.
# 
# Den vannrette asymptoten finner vi ved å la $x$ bli veldig stor. Da vil $g(x)\approx \frac{3x}{2x}=\frac{3}{2}$. Vi har altså en vannrett asymptote for $y=\frac{3}{2}$.
# 
# Disse to asymptotene vil dele opp grafen vår. For å kunne skissere litt nøyere regner vi ut en verditabell med noen $x$-verdier på hver side av den loddrette asymptoten. Det er også greit å se at telleren (og dermed funksjonen) har nullpunkt for $x=0$.
# 
# ```{figure} ./bilder/rasjonaltabell.png
# ---
# scale: 100%
# ---
# ```
# 
# Vi starter med å tegne inn asymptotene og punktene vi har funnet. Så trekker vi ei kurve gjennom punktene og lar kurven nærme seg asymptotene når $x$ går mot $-1$ og når $x$ går mot $\pm \infty$.
# 
# ```{figure} ./bilder/rasjonaleksempel.png
# ---
# scale: 20%
# ---
# ```
# `````

# ## Videoer
# Her kan du se videoer for en del av innholdet på denne siden:
# 
# ````{tab-set} 
# ```{tab-item} Introduksjon og eksempel
# <iframe width="800" height="600" src="https://www.youtube.com/embed/as-JDL1HFIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ```
# 
# ````
