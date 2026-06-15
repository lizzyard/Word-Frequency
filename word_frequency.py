import sys

def create_dictionary(sublist):
    word_count = {}
    for words in sublist:
        word_count[words] = word_count.get(words, 0) + 1

    print_dictionary(word_count)

def print_dictionary(dictionary):
    for k,v in sorted(dictionary.items()):
        print(k + ": " + str(v))
    greatest_count(dictionary)

def get_sentence():
    while True:
        print('Enter text: ')
        sentence = input(">")
        if any(char.isdigit() for char in sentence):
            print('Please type letters only.')
        elif any(char.isupper() for char in sentence):
            sentence = (sentence.lower()).split()
        else:
            sentence = sentence.split()
        clean_words(sentence)
        break
def clean_words(list_words):
    for index, item in enumerate(list_words):
        list_words[index] = item.strip(',?:;"\'')
    create_dictionary(list_words)

def greatest_count(dictionary):
    print("Most common word: " + max(dictionary, key=dictionary.get))
    print("Count: " + str(max(dictionary.values())))
    sys.exit()

get_sentence()
