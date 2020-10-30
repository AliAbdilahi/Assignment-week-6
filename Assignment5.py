import re
path=r"C:\Users\Pc\Documents\The Project Gutenberg EBook of The Bet and other stories.txt".replace('\\', '/')
def hapax_function(get_path):
    file = open(get_path)
    book = re.findall('\w+', file.read().lower())
    frequency = {key: 0 for key in book}
    for word in book:
        frequency[word] += 1
    for word in frequency:
        if frequency[word] == 1:
            print(word)
hapax_function(path)

