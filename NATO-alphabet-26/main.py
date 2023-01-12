import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter: row.code for (index,row) in data.iterrows()}
print(dict)

is_game_on=True
while is_game_on:

    word= input("enter the word: ").upper()
    # below list comprehension will return list contains of code with dict.letter match with word.letter which user have enter and split into single word
    new_word=[dict[letter] for letter in word]
    print(new_word)
    again= input("do you want to try again? yes or no: ")
    if again== 'yes':
        is_game_on=True
    else:
        is_game_on=False
