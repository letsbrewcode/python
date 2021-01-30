# Problem: Substring Index
# Description: You are given two strings, one is a sentence containing words
# seprated by spaces and second is searchword. Scan each word of sentence to
# check if it begins with searchword. Return the index of the word where
# searchword is prefix of word.

# If searchword is a prefix of more than one word in sentence then return the
# index of the first such word. If there are no such words then return -1.

# Example 1:
# Input: sentence = "Jupiter is the largest planet in solar system",
# searchword = "sol"
# Output: 6

# Example 2:
# Input: sentence = "This problem is an easy problem", searchword = "pro"
# Output: 1

# Example 3:
# sentence = "Jupiter is the largest planet in solar system", searchword =
# "Saturn"
# Output = -1

# Source: Leetcode #1455
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word
# -in-a-sentence/

def substring_index(sentence, searchword):
    return

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    testcases = [("Jupiter is the largest planet in solar system", "sol", 6),
                ("This problem is an easy problem", "pro", 1),
                ("Jupiter is the largest planet in solar system", "Saturn", -1)]

    for t in testcases:
        test(substring_index(t[0], t[1]), t[2])
