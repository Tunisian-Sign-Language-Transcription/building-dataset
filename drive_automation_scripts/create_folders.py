from time import sleep
from functions import *

if __name__ == '__main__':
    words, nb_words = fetch_words('../words.txt')
    for index, word in enumerate(words):
        progress_bar(index+1,nb_words)
        create_folder(word)
