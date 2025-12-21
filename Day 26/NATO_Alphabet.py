import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = nato_alphabet.set_index("letter")["code"].to_dict()

input_name = input("enter your name ")
for letter in input_name :
    final_output = alphabet_dict[letter.upper()]
    print(f"{letter}-->{final_output}")