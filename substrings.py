
from collections import defaultdict

def findSubstrings():
    words = ["Apple", "Melon", "Orange", "Watermelon"] 
    parts = ["a", "lon", "mel", "el", "An", "ater"]

    substrings = []
    for word in words:
        last_index, last_len = 10 ** 10, -1
        for part in sorted(parts, key=len, reverse=True):
            index = word.find(part)
            if index > 0:
                if index < last_index and len(part) >= last_len:
                    last_index, last_len = index, len(part)
        end = last_index + last_len
        if last_len > 0:
            new_word = '%s[%s]%s' % (word[:last_index], word[last_index:end], word[end:])
            substrings.append(new_word)
        else:
            substrings.append(word)

    print ' '.join(substrings)


if __name__ == '__main__':
    findSubstrings()