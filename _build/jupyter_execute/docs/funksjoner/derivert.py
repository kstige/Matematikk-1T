#!/usr/bin/env python
# coding: utf-8

# # Den deriverte
# 
# Den momentane vekstfarten er en viktig størrelse fordi den leder oss mot en av de viktigste størrelsene i matematikken. Vi ser først på et eksempel.
# 
# ```{admonition} Eksempel: Momentan vekstfart
# :class: eksempel, dropdown
# Bruker GeoGebra-under eksempelet til å finne den momentane vekstfarten (MV) til $f(x)=x^2$ for $x\in\{-4,-3,-2,-1,0,1,2,3,4\}$. Verdiene fyller vi inn i en tabell.
# | **x**    | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
# |----------|---|---|---|----|---|---|---|---|---|
# | **MV**| -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8 |
# 
# ```

# 
# I eksempelet over ser vi at for hver verdi vi har av $x$, så får vi en verdi for den momentane vekstfarten. Det vil si at den momentane vekstfarten oppfyller kravet til å være en funksjon. Denne funksjonen gir vi et eget navn: Vi kaller den for "den deriverte av $f(x)$", og vi bruker skrivemåten $f'(x)$.
# 
# ```{admonition} Definisjon: Den deriverte
# :class: def
# 
# $f'(x)$ (leses "f derivert av x") er en funksjon som har funksjonsverdi lik stigningstallet til tangenten til $f(x)$ i punktet $(x, f(x))$.
# 
# Den deriverte i et punkt har samme verdi som den momentane vekstfarten i punktet.
# ```
# 
# Vi kommer nå til å bruke for eksempel $f'(2)$ i stedet for å snakke om den momentane vekstfarten til $f(x)$ i punktet $(2, f(2))$. Det er allikevel viktig å huske på at den deriverte er en funksjon som gir oss den momentane vekstfarten.

# ## Uttrykk for den deriverte
# I 1T kommer vi ikke til å ha arbeide med å finne funksjonsuttrykket for den deriverte (det kommer i R1/S1). Fokuset kommer til å være på forståelsen av hva den deriverte sier oss. Det kan allikevel være greit å se at den deriverte også vil være gitt ved et funksjonsuttrykk.
# 
# `````{admonition} Eksempel: Funksjonsuttrykk for den deriverte
# :class: eksempel, dropdown
# Vi ser på tabellen fra forrige eksempel en gang til, me kaller nå verdiene for den momentane vekstfarten for $f'(x)$.
# 
# | **x**    | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
# |----------|---|---|---|----|---|---|---|---|---|
# | **f'(x)**| -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8 |
# 
# Vi ser at $f'(x)$ har den doble verdien av $x$. Det må bety at funksjonsuttrykket for $f'(x)$ må være
# 
# $$
# f'(x)=2x
# $$
# 
# ```{figure} ./bilder/derivertuttrykk.png
# ---
# scale: 80%
# align: right
# ---
# ```
# Vi kan bruke CAS for å undersøke om dette stemmer. Vi definerer funksjonen ved $f(x):=x^2$ før vi i linje 2 skriver inn $f'(x)$ slik vi ser i figuren til høyre.
# 
# `````

# ## Fortegn til den deriverte
# 
# Siden den deriverte er stigningstallet til tangenten i et punkt på grafen, så vil fortegnet til den deriverte vise oss om grafen stiger eller synker. Bruk GeoGebra-appen over til å kontrollere at den deriverte (den momentane vekstfarten) er positiv når grafen stiger og negativ når grafen synker.
# 
# På samme måte som vi er interessert i punktene der $f(x)=0$ (nullpunktene til funksjonen), så har også punkt der $f'(x)=0$ spesiell interesse. At den deriverte er 0 i et punkt må bety at tangenten til grafen er vannrett i punktet. Hvis vi ser for oss en graf, så ser vi at det skjer i topp- og bunnpunkt. Ved å finne nullpunktene til $f'(x)$ kan vi altså finne topp- og bunnpunkt for $f(x)$.
# 
# ```{admonition} Fortegnet til den deriverte
# :class: def
# 
# For en funksjon $f(x)$ gjelder det at:
# 
#  * $f'(x)>0$ når grafen stiger mot høyre
#  * $f'(x)<0$ når grafen synker mot høyre
#  * $f'(x)=0$ og skifter fortegn når grafen har topp- eller bunnpunkt
# 
# Det siste punktet gjelder ikke for eventuelle topp- og bunnpunkt som er endepunkter i definisjonsmengden til funksjonen.
# 
# ```
# 
# Når vi skal analysere en funksjon og finne ut hvordan den oppfører seg ønsker vi ofte å bare se på fortegnene til funksjonen og den deriverte. Til det bruker vi det vi kaller ei fortegnslinje. Vi bruker hel linje for å markere at funksjonen (eller den deriverte) er positiv, stipla linje om den er negativ, og en $0$ om det er nullpunkt.
# 
# `````{admonition} Eksempel: Fortegnslinje
# :class: eksempel, dropdown
# 
# Ei fortegnslinje kan se ut som på figuren under
# 
# ```{figure} ./bilder/eksempelfortegnslinje.png
# ---
# scale: 50%
# ---
# ```
# 
# Denne fortegnslinja viser at funksjonen har nullpunkt for $x=-2$ og $x=2$. For $x<-2$ og $x>2$ er funksjonen positiv. For $-2<x<2$ er funksjonsverdien negativ. Fortegnslinja for den deriverte viser et nullpunkt for $x=0$ og at den deriverte er negativ før $x=0$ og positiv etter. Det betyr at $x=0$ må være et bunnpunkt for funksjonen.
# 
# Det kan være flere funksjoner som passer med dette, men et eksempel er:
# 
# ```{figure} ./bilder/fortegnslinjemedgraf.png
# ---
# scale: 20%
# ---
# ```
# `````
# 
# Under kan skrive inn funksjonsuttrykk for polynomfunksjoner og få fram fortegnslinje for $f(x)$ og $f'(x)$ (og for den andrederiverte $f''(x)$, men den ser vi ikke på i 1T). Prøv deg fram med ulike funksjonsuttrykk og se hvordan fortegnslinja for $f(x)$ viser hvor funksjonen er positiv/negativ og hvordan fortegnslinja $f'(x)$ viser hvor funksjonen stiger/synker. Du kan også tegne inn grafen til $f'(x)$ dersom du vil se den.

# In[1]:


get_ipython().run_cell_magic('html', '', '\n<meta name=viewport content="width=device-width,initial-scale=1">\n<meta charset="utf-8"/>\n<script src="https://cdn.geogebra.org/apps/deployggb.js"></script>\n\n<script> \n    var views = {\'is3D\': 1,\'AV\': 0,\'SV\': 0,\'CV\': 1,\'EV2\': 1,\'CP\': 0,\'PC\': 0,\'DA\': 0,\'FI\': 0,\'macro\': 0};\n    var parameters = {\n   "width":1550, "height":658, \n   "bordercolor": "#be8322", \n   "showResetIcon":true,\n   "enableLabelDrags":false,\n   "enableRightClick":false,\n   "errorDialogsActive":false,\n   "useBrowserForJS":false,\n   "showZoomButtons":true,\n   "appletOnLoad":function(api){ /* api.evalCommand(\'Segment((1,2),(3,4))\');*/ },\n   "showFullscreenButton":true,  \n   "disableAutoScale":false,\n   "allowUpscale":false,\n   "clickToLoad":false,\n   "appName":"classic",\n   "buttonRounding":0.7,\n   "buttonShadows":false,\n   "language":"nb",\n   "ggbBase64":"UEsDBBQAAAAIACNVUFZwzca8HgUAADMmAAAXAAAAZ2VvZ2VicmFfZGVmYXVsdHMyZC54bWztWl9z2jgQf75+Co+e7h4CNmD+ZOJ00s7cXGbStHPJ3NyrMMLoIiSfJQfIp+/qD7YJkKZAiuk0DxErS2vt77darSRfvJ9PmfdIMkkFj1DQ8JFHeCxGlCcRytX4rI/eX767SIhIyDDD3lhkU6wiFOqWRT+QGr1woOtwmkYoZlhKGiMvZVjpLhES4zGjnCDPm0t6zsUtnhKZ4pjcxRMyxTcixsromiiVnjebs9mssXxrQ2RJExTL5lyOmkmiGlAiD4bOZYTcj3PQu9J71jb9Wr4fNP/9dGPfc0a5VJjHMBAwa0TGOGdKwk/CyJRw5alFSiKUCsoV8hgeEhahL1ryfh9nhPyBPNcJ0PLR5bvfLuREzDwx/I/EUKeyHFS7fkZo6jbw+KNgIvOyCPV6yANwdTGMUCsMATSWTnCEfNuY4QXJvEcMGlwNzpWITX9TO8ZMOsXmTZ/EiNgnHdeeU2AJ4PSkIsCH3wiQJ1NCRjBq5GyEH0DPwjBd0WhMv6NPTmNYrVUL5qrdwGIhspH05hG6xbfIW7jyyZbQ5KLpgH0dxCOSEj6CRis4Bzvh3O0bnHUBOOuixjA7jUeFuXsiMB8aZJjHb4DyZ17FtrUTtkELggOYZMpfwWIF32v+N0lg1FWU26eD8klgvOrDnZ3QhZwA7IH/dfRfA5dFUer/kLqIacrI/MdCbzMjB+ONEQrYW7tlGVXYdVp2DNDhvZtA19Za+NSExg+cSMjiwDGKTvrHX3QEC5RRJiBNpArwDHp9q4H8z1dIo8AZhTZ7EzHOeaytKsD9mGePVTbaHf8YfJQ6d44ub0TGdiwlSbRU4HK3lEvX3i2x+6ldW+SKabXXXMHuCiCBgci1kT8Qkt6Dqs/8PsNc6i3Wc0eBbU5WjVIOdTeBuIt664/2mD0ZXrzEdngKbJ8k1weIePwRZwUTVdZ2y6m2rvoNcIMjU/cd4b8KxP7pzym7715O1N1t6rf8zmb04LDp2ABuB+MRzBMlDP84sUwhTiKh+5FxcEMWDmsXkRTzA+xq2CKpzOgvS7ngo2f52N+M7YxW0FrZeIZtQ2oI6p45eODbv6Az8IOgC+cHR89uXsZ4ZQujQbYVJco213tLlGsxbw6BZyy4PjxfbkGsVCDZOYn4UacNIaEJ4TYsQxDxjY4FFKD5SUv63mIeGHkBBTx90gVUm+5gV0bn3pXtcWUbXrVs0bZFxxahw+8b3KYQ3iqZ8rMForPbtqgO0aQ+nB8st66T8/B8SrJKaLhdyoXvhDY4gA356umUZHQEZE8pwHkGOE8xrKY6Lx9KwXIF13Bwu8XLazjrcDM6UhOdiMH4xnSuibXoeROR0SfBVQGWp/31ipkLu5UDi01Et17KM18Vt7b59HYPrvjqfuEZ84SVk/HKSiUD9qjfNFo/JHyZGBiI4aXbaPXbQT9s+72gNwj73VfyFPRLnuyD/WjaNh+BvvX5iLO4PCqFJHcLk8DbQbl0q40f9DphuzVohcFg0IEfMPZD7wb/LCrKnU0dTwONB6w1fbODPibiXJbH11YqEAKX3Ck5ru1+B+dzyijOFutvejOIFZmXCcO9ESqfIdQwIdxuCsCelEO7tlLlrt8aM6aAIodvROAcwbyE8g84fkgykXPn2pURHMZ0t/jU8UxhKAQjsBtemvVhKVdumNdW/m0AuRX8mLsF+BYnfhiK+cpi9Y0rMlnOgBsjVO59N8yA11u5viKdHd0Vdjmf+877yo0ZSpWAZuXzqObyW6zLr1BLAwQUAAAACAAjVVBWguJBXXsDAABPEQAAFwAAAGdlb2dlYnJhX2RlZmF1bHRzM2QueG1s7ZjNctMwEIDP8BQa3YntxE7rTl0mAweYAaZML1xVW0kEjuRKShz31XgHnomVVm0d6F86aZl2yCFrSd5d6dv1WvLh2/WiJiuujVCyoMkgpoTLUlVCzgq6tNM3+/Tt0evDGVczfqoZmSq9YLagmbvzUg9ag70sd32saQpa1swYUVLS1Mw6lYKq6bQWklNC1kYcSPWFLbhpWMlPyjlfsE+qZNbbmlvbHERR27aDC68DpWcRGDbR2lTRbGYHICmBqUtT0HBxAHY3tNuR1xvGcRJ9+/wJ/bwR0lgmS5gILKviU7asrYFLXvMFl5bYruGwACVFOQIfNTvldUE/Sgtr5aWbIimXegX6QbmgoySL6dHrV4elUroyRK0LCiRUh+IcRQt4ARmOrXBshWMtdrbY2frOyBk0c9USdfodHBfU6iV4DRPyDX8PDL9TtdJEF3QIHiBuSQzyFGQ+hIDUzZyBxUES4y9J8zhJxskQ9WvWcU1WDIwGr2xpVelN+t4pq03w5Z1/VhXHkTTcLwXkhCNjLIfog3PTcF75K+QJy4JU6HxW9e1BRpzYrubEzkX5Q3ID8cx6Su7ig6gq7pITdfiZRBXj/gvaMA2pZDWkG46LGZcrIKa0IevYT6IDAdbOXcsl6Trx7Q4EjJ47Ad1eHVaixZpMUGOCN06GKEYoUhRZIHYYheT5K43YWpjR+8ugTUKzlznxyGfOtoEG90AS/iHK7qELMX6siELy/KuYknDNYdW/ft6O2z+YJdOWG8Fk7/F95wb+JD9+DuQfk/vNIMG+5D1+x769wQ/K6oP45bkHOExAAkIvL0tUtiuMU+beYMHEjZXvOmIB1E2ZGko8Fmys16GG31kMGlV3c15pJa+49rqu0I4C2oc8SduGI8lGPh4ZvjF6GT1IA7UsH8fpON1ZbB6a4luRnehyLha84mwTLcT+qdAOE3wbp3serRMvg+1xBxVZQHXoc326lPUlAyafI9fhi8nZYy3MYpNq8oRUx1iYkWoOrWdIVXJ7uc4v7rpfVbP/VXUblmdLVvkdWFjq14t2nykm6C5L4zjN3W9vnGT7SQonmh0B2sW+VCyaWpTC3uukce05w3XiYaJDcQ4ieNv26EEmYxR7KPZR5HfuRMxST+Hkfd1OOQxtBjl9WJBB79q9MnwquGdQrww/0Tmlr3TrfjnqfTqILr5THP0GUEsDBBQAAAAIACNVUFbWN725GQAAABcAAAAWAAAAZ2VvZ2VicmFfamF2YXNjcmlwdC5qc0srzUsuyczPU0hPT/LP88zLLNHQVKiuBQBQSwMEFAAAAAgAI1VQVnN3FCM/DgAAvjwAAAwAAABnZW9nZWJyYS54bWztW+ty28YV/u08xQ6byUitReJ+cclkZNnTpuMkmsjJZBonHRBckohAgAZAifTlXfIIafIGfoA8U7+zuwABkqJISZXTJpnIABZ7O5f9zrcHy+4n80nMLniWR2nSa+ltrcV4EqaDKBn1WrNieOS1Pvn4g+6IpyPezwI2TLNJUPRaNtWs2uGp7do+lQXTaa8VxkGeR2GLTeOgoCa9VjocxlHCWywa9FrO0LM55+FRYHP3yLKs8Kg/NM0jw9Ut1zYCz/FQk83z6FGSfh5MeD4NQn4WjvkkeJaGQSFGHRfF9FGnc3l52S7n106zUQdTyDvzfNAZjfptXFsMQiZ5r6VuHqHfRutLU7QzNE3vfPPZMznOUZTkRZCEmAgpYBZ9/MGD7mWUDNJLdhkNijHUZduQeMyj0RgqcWyvxTpUawq9THlYRBc8R9vao5C+mExbolqQ0PsH8o7FlWAtNoguogHPei2tbTmu5juua+m+aVue1WJpFvGkUHV1OeZaH5hYrRPNsWzd0Q1fMw3D9jRncy/dTjmn7kXEL+Xk6E7MG5UuojzqxxwyZDOyZTLMYJ1eaxjEOZ7zYhHzfoAhVcFyPuZDNM+jV6jsGhBCahKdatpD+nPwZ2mYtZSmGhRVizSNRacae/OGGZqhsYd00eXFkKWafNRMeTHkxZIXW9axZEtLVrVkHUvWscyaeGr6N5PPJDF2lQ8+U8mHejp7w3CBTHQxGc0bN5g/XSz16MhHV1x0oRY8erLUp0cY+G6E2UMUWzeaxmI6syGRzXQfKnZougbTbWahxEOJy0wqs3WLmYyq6CYT1rCEZA7e0Gv8i4XGdLIaDMVgcdjeIEPbNrNRzaW2pDMHwqOVhj+qjRnhz6Qy08SfKDMt/JHpbXRky24wD9t0xJ0t/iVd2hjFxnhvmHiFMsvHcFRguzozMRM8uxpDv+geMxbSwMnof51J/3KZ4THRq+hfg45uYRl9aRl7Hze73ahYGsq1PXRdBP1e6/jZ354+/vJ4fQaGvXkGet0l94aPSmrDxYopx8RQ4n/xtzaiuZfQckobRmws5+0jOg20up2hy+EtUvluw+sGdHPPY1qa796Nmm173ZlcGpWC7MqoLrnheliQV4CGuN6N+f1rzN/tlKGyq2bE8jHVVT5e8Amoh8ZckzkC1gUmAgwBBhIYXYO5NnMJ1Et4BJx5zKGrwkhCSK+BkTYhaA0oHSoEGFEMYALjJGIaVgmauBewSZDahE3gm7WEOEyQutIZAzAzh6BQYR1mYVRoZ2D6ADeHARFtgzmE1VcAH4hgmkeVYsc8BklUJhA6jJLprGjoLZwQUxK3RYraQSwInqo/SMPzx5WmVU88yEHDlt2CzSyZl2Q3DWL2oBsHfQ5WOjojN2DsIohp2YoRhmlSsBJzLCrrdgQJ7PJZGEeDKEi+ht1LqvT5bNLnGfwNtykJKTqh5qxki4L2VGRRE30+6IZpmg3OFjnchM3/yTM0Nn0DhM3wDdMxLEM3HOhvIV8Zvt92PFund7bhaPQqDwPycMNw2p7uuJ6L6GVaOvGZxRXvPE8Ozi/OeFFAATkL5hxuKhU+ymiNKUXSw6f54zReFk3TKClOgmkxy8Q+ASNlJNZxMoq50KUwM2h0eN5P52dSiZgq9fV8McXTkdJQf3SSxmnGsAINAgD0Jq6IMHQVdWhqVS0TaEND4oI6uIgq1HFVBdoRdcQVlegqatEGRJpaSos5SlGVzYN5lAt4wdKu+6JwE6LlsyQqnpUPRRSeL4Wl+tIJKjVShSeR3ESIOlTwdD7NODZHcik0h1Xd3Muw3c6KH+/k10qRDb/GpmQ3vzY8o+0Bni3dME1f9zA15dZwyTa83jF9x7ex1SG+oTzXbdtAYNuwHdMER/frXt18Z+nKX9a8uubJf7h1DTBv5mBX+Oxt+1x3yBwuGwzyMedF6ZINx6vtvZWkaDA84XFMplni7nq9nMcUBdKEsfFZmKWxwH12UbsP03g2wWKBRVlG8knTdjtrs+qq0FTOcZIOuAwlyhnQVRxMcz6oBZhup9Gqe86zhMdUe5bz3Hwiqy71HSIcRcksneXyjdS2eIUGp0ExPk4GX/IRZDoNiOIUUO5qJwMeRhM0lOXKewLy7q9gLFk64KOMl0aWU5S+Jd7SwlzKX+lTLvZlNSViKVQXO4aYC/I2iWRuYhLMpT8WHMFd1s/DLJrSumV98LBzvlyZgyinHqoCqg2N5BBNmrGICvKtp8mYF0C57BwGTpCMmhXjFEsHPQQF3iPt0g2DPISLiGnjehpEmeCWgoKQ89ATQKQCTBJphsYBEHVwcHBgHnYOrMPDQySouJAWrsyzKDyQFUzWYXgNOoKXJ8Ri1HuhKpCQxkDddFZcM66J2O34nu8ih+NZ735qsQQc9aLaRYlx0skEgy/HUoS50+i+21lKjPtSETdXCQQ+MLV3Py118ZTeQNcH1au6Jm6qggMdSjXZn1n+MitgAPTZ0MG9CWtdLax4dRfCUmcHBgT2IfA0upWwtd4VMPOXADQU91rz7w+MQ/YXthDXHiOmIIIYVpb01i5W0QRJwkZ5vSOBpQBzlvZ/AKCuEJcaRuF9Fcew6hHF8C9iGCWM4+k4qJAkDhZEN2pEXHT2WYWpJT2P5iWeLvFtGQiLMQIOMpmIL4i6cvq0ZcTN36PBgMt9SIqsclQscI+kgqQOLxPZgdgYIgOe80y9iUY8uYCQKXB1ron2C1zQ6yt6otz3XBfPC1zw9hVdUCyaI2meRXN2LBseyxrHhowvx6Zod2zJi10BqNK/QDuxwOEJtHv9NCF4x2SEBeTmKUDX82OEZagU3S/ErVS+8BRR4UT2q3pbs7BgQJX9Tm5mXwd0EAamCyxMl5uZWExGRHJRqnilLF0JNSoCwTDSANIsS6a7pxrFGiEllvqEnVS0rOnyyT66fLKuyyZhWnrxb0iX5ONX6nIdWy6iBIFXwYtu2ohV6ygi+EYltmpSEZEG1xCzEaioGEvbtB3dtyxfox2wpYh0DtYILTSohdM2PFP3bFNzdde3PbD0oJ+D0xX4jASCkyw/I0mfVmTRdGgdS9II0U0fe3aBNWU98InoFchYhTyCzR5LpnQtGOkKhNbQCJR+HY2CLFzazCy565XrsaQDmP1VqIuc2irutlEm/tNJrfSRaKtrfTEc5rwQzoE5Y7aWv9HxKnYJxikommJ6bU13LeTffQNZDN/CDQAaSRnScBWBMD18OVyIXVhtf3DFMv4yxWcsvrKGn8gVXLokLWEBfo0lfLrPEj69Bg7vdAUv1XxEuVjo+Ugt2s16vuECP8J3W6wQDakhXfccG19f5ZJfLcb6uR5PxUZ5sx1OpAmEwhsmmG03QRMtZhuBQkl1PVDsxQ/ubEXew1L0pYcg473JRcptKDIbimb2Wh/Oeh9uN+YXGfZOozQJ4mf03b5p1dN6fFw16XC7SeUxgJJD3Cwu3gmHvHu6GE2mcYQ6a8usHkg3rblbW2Iz3RvtYYnR78ISCkuJnm9EuRvxRal8YQeh8YYNHu8TYx6/nxgj3dNQtGHFRoqHNeHjRR4lbCYgZNfgU/azytRvFGp22AEJGGqY4ngfUxy/p3AvvtvA+zdj+WZjhGl+W2NcyQR2scZpGi8AUCu2oJgPO+CMwObQX6hd1lRWQGohwEY4uM5IcqjKDDILcXsE2Xufq9uwFGxto7tbxfEVOGzssRqy53xET9XE5DGyO5z4fqgdzOZRHAXZYi0lfXtrwE1i4v/VOoe3r6e+zzmf0oeXL5LnWZDkdNJwNSeE72BZ3fEHfBjMYhUXeFLPWjderYWMTeuDYsh+Jgv/MNk9mGzdWPQJvUbA1hjXdqsFN4oFNzRaLSwj+SDYyubAXG6xfx82vcqkuy7LtWwV8uz/eq2/VemqxcHpIXLuc1zk4ZGmRyTld5WVxisbzyMkfJv/lXnD6ynz5qhxjQz8PKcwKkT46OUsLf6qqBnryUck+A+eBc/5N9+ezbLBcz4vviVRv/uOUv+qxUd/mgdoJ1jElnakm0a7dz+++1G1hT6oLXuB81XhazmFt69ll2+v7lKpsd6r7FDeb7JEgXZLM0j5d82L6WorfD+fI6JcSLtaLE4W4btCNKwyiGBrn9WOnInvomIbU8L2xtSlyFPKJBwOHm4laGcK0DbuHcUOpcHMxts52Co8jm8W1MqTEZ48GPFf2j0a/2s4tw3WNoauzagAx6ijwoFciw+ZXJuH5QrbZYEZ16UGygN4WGKWMsqdL7G7W03CRqe0IZK5mbbpefiRhWniGLgjd19a23dty0ESEWeSDMvycC7n+m0QQdow4vFgZZ2pJPTqKntOuh3yGAC2dbmRQWS3pb5rLXeFPrXh29ks15xgKmtXp5muJTOOTFJajsLgzRvbjUC6wnBqp2Lq2+CvhZYfKRsvJv0UGaBaC3lylA7SQLVn5DFrL3FoZFSMZfE1STmBFFGaiZx3vmJwadGGsX/9twTbX3+Wu91ff9kn8Y3Wu2W+gRv46OXjsCeO2Llw3PKrwT2kvndPF94+973Cgq+m8it6/HlHPept/LDD9R3TcFzf8nwctH0/nxC2HqJ4f3r85ab+uHZm8f/DH+sJPEXJtmzadgjfiEO18P2PGT6f0jFcgjiesAlAciQ+e/PkoSLhOPGDKvl5Fl3gdw4Ji5joqJ+e5zxp7xHuzZ3onIz2+4aVWxHqLTRYJitNXcxnB/ViZ93YM5EWXn/++BH76vwH0s2QRzFp+S0TWxvD1b7HbibKQhS8EOqWTZ7A6Pn5DKpno6go3rKjF/iNSbHYh15ZvwF978uuiIcqfnVEBwG2Miy37fq6Zjj48ZtlOqYFMkVpDZxrtAxP11xAreWLHy9t4lgIkcuTnuJnGOrHvh//B1BLAQIUABQAAAAIACNVUFZwzca8HgUAADMmAAAXAAAAAAAAAAAAAAAAAAAAAABnZW9nZWJyYV9kZWZhdWx0czJkLnhtbFBLAQIUABQAAAAIACNVUFaC4kFdewMAAE8RAAAXAAAAAAAAAAAAAAAAAFMFAABnZW9nZWJyYV9kZWZhdWx0czNkLnhtbFBLAQIUABQAAAAIACNVUFbWN725GQAAABcAAAAWAAAAAAAAAAAAAAAAAAMJAABnZW9nZWJyYV9qYXZhc2NyaXB0LmpzUEsBAhQAFAAAAAgAI1VQVnN3FCM/DgAAvjwAAAwAAAAAAAAAAAAAAAAAUAkAAGdlb2dlYnJhLnhtbFBLBQYAAAAABAAEAAgBAAC5FwAAAAA=",\n    };\n    var applet = new GGBApplet(parameters, \'5.0\', views);\n    window.addEventListener("load", function() { \n        applet.inject(\'ggb-element\');\n    });\n</script>\n\n<div id="ggb-element"></div> \n')


# `````{admonition} Eksempel: Fra graf til fortegnslinje
# :class: eksempel, dropdown
# 
# Vi skal tegne fortegnslinje for funksjonen $f(x)=\frac{1}{2}x^{3} - 3x^{2} + \frac{3}{2}x + 5$ som er tegnet i grafen under. Ved å ta utgangspunkt i grafen skal vi tegne fortegnslinje for funksjonen og den deriverte til funksjonen.
# 
# ```{figure} ./bilder/graftilfortegnslinje.png
# ---
# scale: 20%
# ---
# ```
# 
# Når vi skal tegne fortegnslinje for selve funksjonen, så ser vi på hvor den er positiv og hvor den er negativ. Vi ser da at 
# 
#  * $f(x)>0$ for $x\in\langle -1, 2\rangle \cup \langle 5, \rightarrow\rangle$.
#  * $f(x)<0$ for $x\in\langle \leftarrow, -1\rangle \cup \langle 2, 5\rangle$.
#  * $f(x)=0$ for $x\in\{-1, 2, 5\}$.
# 
# Når vi skal tegne fortegnslinje for den deriverte, så ser vi på hvor funksjonen stiger og synker. Det er litt vanskelig å se nøyaktig, men om vi finner $x$-verdiene til topp- og bunnpunkt ved hjelp av CAS, så ser vi at
# 
#  * $f(x)$ stiger slik at $f'(x)>0$ for $x\in\langle\leftarrow, 2-\sqrt{3}\rangle \cup \langle 2+\sqrt{3}, \rightarrow\rangle$.
#  * $f(x)$ synker slik at $f'(x)<0$ for $x\in\langle 2-\sqrt{3}, 2+\sqrt{3}\rangle$.
#  * $f(x)$ er flat slik at $f'(x)=0$ for $x\in \{2-\sqrt{3}, 2+\sqrt{3}\}$.
# 
# ```{figure} ./bilder/fortegnslinjeeksempel.png
# ---
# scale: 35%
# ---
# ```
# `````
