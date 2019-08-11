import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        similar_word = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? "
                             f"Enter Y if yes and any key for no: ").lower()
        return data[get_close_matches(word, data.keys())[0]] if similar_word == 'y' else "Please re-check the word"
    else:
        return "This word doesn't exist in the dictionary"


word = input('Enter a word: ').lower()

output = translate(word)

if type(output) is list:
    for item in output:
        print(item)
else:
    print(output)