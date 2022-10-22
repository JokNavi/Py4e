words = dict()
with open('words.txt') as f:
    for word in f.read().split():
        words[word.lower()] = word.upper()

chosen_word = input('->: ')  
if chosen_word in words: 
    print(f'{chosen_word.capitalize()} has been found in the Dict.')
else:
    print('That word isn\'t in the Dict.')