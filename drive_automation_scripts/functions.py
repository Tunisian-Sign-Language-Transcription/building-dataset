from imports import *


def create_folder(folder_name):
    print("\nCreating folder for: {0}".format(folder_name))
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [dict_folder_id]
    }
    return service.files().create(body=file_metadata).execute()['id']


def progress_bar(word, nb_words):
    perc = round((word/nb_words)*100)
    os.system("cls")
    print("["+"="*round(perc)+"_"*round(100-perc)+"]" +
          str(word)+"/"+str(nb_words))


def fetch_words(filename):
    nb_words = 0
    words = []
    with open(filename, encoding='utf-8') as file:
        for line in file:
            words.append(line.rstrip())
            nb_words += 1
    return words, nb_words
