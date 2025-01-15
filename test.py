#!/usr/bin/env python3

def numara_vocale(text):
    vocale = 'aeiouAEIOU'  # Lista de vocale pentru a verifica în ambele cazuri (majuscule și minuscule)
    contor = 0
    for caracter in text:
        if caracter in vocale:
            contor += 1
    return contor

# Exemplu de utilizare a funcției
text_input = " s."
numar_vocale = numara_vocale(text_input)
print(f"Numărul de vocale din textul dat este: {numar_vocale}")