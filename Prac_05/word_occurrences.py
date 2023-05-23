
"""
Word Occurrences
Estimate: 12 minutes
Actual:   15 minutes
"""

user_sentence = input('Enter a sentence: ')

word_count = {}
for word in user_sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = dict(sorted(word_count.items()))

for key in sorted_word_count:
    thing, width, other_thing = key, 13, word_count[key]
    print(f"{thing:{width}} = {other_thing}")

