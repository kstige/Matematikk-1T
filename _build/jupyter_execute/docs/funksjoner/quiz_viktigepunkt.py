#!/usr/bin/env python
# coding: utf-8

# # Quiz om viktige punkt
# 
# $$ $$

# In[1]:


from jupyterquiz import display_quiz

oppgave1=[{
        "question": "Hva er skjæringspunktet til $f(x)=x+4$ med y-aksen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "$(0, 4)$",
                "correct": True,
                "feedback": "Riktig."
            },
            {
                "answer": "$4$",
                "correct": False,
                "feedback": "Det her er bare y-koordinaten til skjæringspunktet."
            },
            {
                "answer": "$(0, -4)$",
                "correct": False,
                "feedback": "Det her er skjæringspunktet med x-aksen."
            },
            {
                "answer": "$-4$",
                "correct": False,
                "feedback": "Det her er nullpunktet til funksjonen."
            }
        ]
    }]

oppgave2=[{
        "question": "Hva er skjæringspunktet til $f(x)=x+4$ med x-aksen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "$(0, 4)$",
                "correct": False,
                "feedback": "Det her er skjæringspunktet med y-aksen.."
            },
            {
                "answer": "$4$",
                "correct": False,
                "feedback": "Det her er y-koordinaten til skjæringspunktet med y-aksen."
            },
            {
                "answer": "$(0, -4)$",
                "correct": True,
                "feedback": "Riktig."
            },
            {
                "answer": "$-4$",
                "correct": False,
                "feedback": "Det her er nullpunktet til funksjonen."
            }
        ]
    }]

display_quiz(oppgave1)
display_quiz(oppgave2)

