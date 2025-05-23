# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as name:
    n = name.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    l = letter.read()
for i in n:
    j = i[:-1]
    with open(f"./Output/ReadyToSend/{j}_letter.txt", "w") as ready:
        ready.write(l.replace("[name]", j))
