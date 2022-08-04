"""
We want to find the most frequently used words in a long string of text.
Write a function most_common_words(text) that returns an array containing words with their frequencies,
sorted from most common to least common, with ties broken by alphabetic order.

For greater accuracy, your solution should ignore punctuation and capitalization.

Examples
For example, given the string

text = 'It was the best of times, it was the worst of times.'
then most_common_words(text) should return
[
  ('it', 2),
  ('of', 2),
  ('the', 2),
  ('times', 2),
  ('was', 2),
  ('best', 1),
  ('worst', 1)
]
"""


def most_common_words(text):
    # remove punctuation
    punct = '''.!;:'",?'''
    for ch in text:
        if ch in punct:
            text = text.replace(ch, "")

    # case-insensitive
    text = text.lower()
    # split the text into words
    text = text.split()

    # hash-map or dictionary in py for the words and their occurrences
    dic = {}
    for word in text:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    # we sort alphabetically and then by frequency
    dic = sorted(dic.items())
    dic = sorted(dic, reverse=True, key=lambda x: x[1])

    return dic


"""
If I have to output it as an array:
    new_list = []
    for key, value in dict.iteritems():
        new_list.append(list([str(key),str(value)]))                 
    new_list.sort(reverse = True, key = lambda x: x[1])
      
    return new_list
"""


def test_most_common_words():
    text = 'It was the best of times, it was the worst of times.'
    expected = [
        ('it', 2),
        ('of', 2),
        ('the', 2),
        ('times', 2),
        ('was', 2),
        ('best', 1),
        ('worst', 1),
    ]
    assert most_common_words(text) == expected


test_most_common_words()




