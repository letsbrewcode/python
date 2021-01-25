# Swap Chars
# Given a string and two indices, swap the chars on those indices.
# String length will be greater than 2 and indexes will not be out of bounds.

# Example 1
# Input: 'Universe', index1 = 1, index2 = 6
# Output: 'Usiverne'

# Solution 1 (Little messy)
def swap_chars(s, index1, index2):
    return s[:index1] + s[index2] + s[index1 + 1:index2] + s[index1] + s[index2 + 1:]

# Solution 2 (Cleaner approach, involved lists)
def swap_chars_2(s, index1, index2):
    chars = list(s)
    chars[index1], chars[index2] = chars[index2], chars[index1]
    return ''.join(chars)
    
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    testcases = [('Universe', 1, 6, 'Usiverne'),
                 ('Universe', 0, 7, 'eniversU'),
                 ('xy', 0, 1, 'yx')]

    for t in testcases:
        test(swap_chars(t[0], t[1], t[2]), t[3])
