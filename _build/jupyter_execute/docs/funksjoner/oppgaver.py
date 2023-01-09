#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyterquiz import display_quiz

example=[{
        "question": "Hva blir stigningstallet til ei linje som går gjennom (2, 3) og (5, 9)?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "2",
                "correct": True,
                "feedback": "Riktig."
            },
            {
                "code": "3",
                "correct": False,
                "feedback": "Se over hvordan du regner ut stigningstall og prøv igjen."
            },
            {
                "code": "4",
                "correct": False
            },
            {
                "code": "5",
                "correct": False
            }
        ]
    }]

display_quiz(example)

