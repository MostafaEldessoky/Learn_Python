# TODO 1. Create a dictionary in this format:
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
NATO = {v.letter: v.code for k, v in data.iterrows()}
while True:
    inp = input("Enter Your Name: ").upper()
    try:
        x = [NATO[i] for i in inp]
    except KeyError:
        print("sorry only letters are allowed")
    else:
        print(x)
