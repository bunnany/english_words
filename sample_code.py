##
# Sample code to use load_words.py

import load_words as lw


def load_words():
    """ Load a list of words to a list. """ 
    return lw.load_words()


def check_word(words, word):
    """ Check if a word exists in the list of words. """
    if word in words:
        return True
    else:
        return False


def main():
    ENGLISH_WORDS = load_words()
    word = input("Enter a word: ")
    
    print(word in ENGLISH_WORDS)
