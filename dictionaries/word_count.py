# Problem: Word Count
# Read the file provided, little_prince.txt and count the occurence 
# of each word. Then print the words in another file in decreasing 
# order of occurence. That is if prince is the most occuring word then
# it should be on top. Also do not remove any special characters (This
# makes it little easier), i.e. prince and prince, are two different
# words

# Your output should be 
# <word> <count>
# <word> <count>
# ...

# Only consider words that occur 50 times or more.

def word_count(file):
    return

word_count('path/to/file')

# HINT - Break the problem down into smaller problem
# 1. Try to read the file and print it. See if you can do it.
# 2. Break each line into words and print it. Print it.
# 3. Create a dictionary and add all the words to it. Print it.
# 4. Reverse sort the dictionary and print it.
# 5. Remove all the words that occur less than 50 times.
# 6. Write the dictionary entries in a file.