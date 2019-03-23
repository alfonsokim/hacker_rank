from collections import defaultdict
import itertools

class Cooccurrence:
    def __init__(self):
        self.occurrences = defaultdict(int)
        self.words = {}
    
    def get(self, a, b):
        key = tuple(sorted([a, b]))
        return self.occurrences[key]
    
    def update(self, line):
        words = line.strip().split(' ')
        for word1, word2 in itertools.combinations(words, 2):
            if word1 != word2:
                key = tuple(sorted([word1, word2]))
                self.occurrences[key] += 1
                    
    def __str__(self):
        return str(self.occurrences)
                


# alice bob
# bob claire dan
# c(alice, bob) = 1
# c(alice, claire) = 0

# alice bob
# (alice, bob) = 1
# (bob, claire) = 1
# (bob, dan) = 1

# bob bob

if __name__ == '__main__':
    test = Cooccurrence()
    test.update('alice bob')
    test.update(' bob claire dan')
    # test.update('alice al ice')
    # print(test)
    print(test.get('alice', 'bob'))
    print(test.get('bob', 'alice'))
    print(test.get('bob', 'me'))
    print(test.get('claire', 'bob'))
    test.update('claire frank')
    print(test.get('claire', 'frank'))
    test.update('bob alice')
    print(test.get('alice', 'bob'))
    test.update('bob bob')
    print(test.get('bob', 'bob'))