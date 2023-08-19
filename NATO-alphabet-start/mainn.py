import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
#Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

create_dict = {row.letter : row.code for (index,row) in file.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs

word = input("enter name : ").upper()

list_iter = [item for item in word if item != " "]


make_output_list = [create_dict[item] for item in list_iter]
print(make_output_list)
