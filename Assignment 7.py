import re
file = open(r'C:\Users\Pc\Documents\The Project Gutenberg EBook of The Bet and other stories.txt')
words = re.findall('\w+', file.read())
x = sum([len(word) for word in words]) / len(words)
print (x)
