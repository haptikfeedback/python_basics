def word_count(string):

    string = string.lower()
    word_dictionary = dict()
    list_of_words = string.split()

    for word in list_of_words:
        word_dictionary[word] = list_of_words.count(word)  

    return word_dictionary
