import re
import collections

def most_common_words(text, top_words):
    with open(text) as file:
        words=file.read()

    words=re.findall(r'[A-Za-z]+', words)
    res = collections.Counter(words).most_common(top_words)
    return list(dict(res).keys())