#!/usr/bin/env python
# coding: utf-8

# # Funksjoner i programmering
# 
# Funksjoner i programmering er ikke nødvendigvis det samme som funksjoner i matematikk, men vi kommer hovedsaklig til å programmere funksjoner som likner på de matematiske. Dersom vi skal jobbe med funksjonen $f(x)=x^2+2x-4$ lager vi den slik:

# In[13]:


from pylab import *


# In[14]:


def f(x):
    return x**2+2*x-4


# 
# Vi ser at funksjonen er bygd opp av ei linje som definerer (med bruk av **def**) navnet $f$ på funksjonen og variabelen $x$ som settes inn i funksjonen. Den linja avsluttes med kolon tilsvarende som ved for eksempel løkker. Alt som hører til funksjonen skal stå med innrykk på linjene under. Normalt sett avsluttes en funksjon med **return** og uttrykket som skal returneres. Når vi ser på en matematisk funksjon vil det være funksjonsuttrykket som står bak return. I prinsippet kan funksjonen returnere andre ting (som for eksempel tekst) også.
# 
# Tilsvarende som når vi oppretter variabler, så blir det ikke skrevet ut noe når vi definerer en funksjon (med mindre funksjonen inneholder en print-setning). For å skrive ut funksjonsverdier fra funksjonen over kan vi for eksempel skrive:
# 

# In[3]:


print(f(3))


# Vi kan også lagre resultatet av et **kall** til funksjonen til en variabel, og bruke det videre:

# In[6]:


a = f(3)
b = a + 2
print(b)


# Selv om vi ikke skal bruke det videre kan vi også se på en funksjon som returnerer tekst.

# In[5]:


def hei(navn):
    print("Hei", navn)

hei("Per")


# I denne funksjonen har vi ikke brukt return, men ei print-setning. Da vil resultatet skrives ut direkte. Siden vi ved en matematisk funksjon vanligvis ønsker å bruke resultatet videre, så vil det være mest hensiktsmessig å bruke return.

# ## Grafer
# 
# For å tegne inn grafen til funksjonen må vi regne ut mange funksjonsverdier og sette punktene inn i et koordinatsystem. Dette kan gjøres veldig effektivt med disse linjene med kode.

# In[15]:


x_verdier = linspace(-4, 4, 1000)
y_verdier = f(x_verdier)


# Her bruker vi kommandoen linspace (den krever at vi har importert pylab) for å lage en liste med 1000 $x$-verdier mellom -4 og 4. Alle disse $x$-verdiene settes inn i funksjonen og lagres i ei liste med $y$-verdier.
# 
# Når vi skal plotte disse i en graf bruker vi.

# In[16]:


plot(x_verdier, y_verdier)
show()


# Det er store muligheter for tilpasninger av grafen. Noen av dem er vist i det fullstendige programmet under. Prøv å endre på dem for å se hvordan det påvirker resultatet.
# 
# <iframe src="https://trinket.io/embed/python3/eac2d0e239" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
