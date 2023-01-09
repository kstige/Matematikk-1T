#!/usr/bin/env python
# coding: utf-8

# # Quiz om lineære funksjoner
# 
# $$ $$

# In[8]:


from jupyterquiz import display_quiz

oppgave1=[{
        "question": "Hva blir stigningstallet til ei linje som går gjennom (2, 3) og (5, 9)?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "2",
                "correct": True,
                "feedback": "Riktig."
            },
            {
                "answer": "-2",
                "correct": False,
                "feedback": "Du har fått feil fortegn. Kanskje du har byttet om på noen av koordinatene."
            },
            {
                "answer": "6",
                "correct": False,
                "feedback": "Her har du muligens glemt å dele på $\\Delta x$. Stigningstallet er $\\frac{\Delta y}{\Delta x}$."
            },
            {
                "answer": "3",
                "correct": False,
                "feedback": "Det her er  $\\Delta x$. Stigningstallet er $\\frac{\Delta y}{\Delta x}$."
            }
        ]
    }]

display_quiz(oppgave1)


# In[6]:


from jupytercards import md2json, display_flashcards

cards='''

# Stigningstall
$a=\\frac{\Delta y}{\Delta x}$

# Verbose Card Style
In the Verbose Card Style, the front is defined separately from the name and may
have multiple lines of content.

Cards can have mathematics written in LaTex:

$$
 \int e^x~dx
$$
---
The back follows a horizontal rule `---` and may also have 

multiple 

lines of content
'''

myjson=md2json(cards)

display_flashcards(myjson)

