
from collections import defaultdict

def kth_most(array, k):
	freqs = defaultdict(int)
	for n in array:
		freqs[n] += 1
	return sorted(freqs, key=freqs.get)[k-1]


def super_kth_most(array, k):
	top_k = {}
	for n in array:
		if len(top_k) == k:
			if n in top_k:
				top_k[n] += 1
		else:
			top_k[n] = 1


if __name__ == '__main__':
	print (kth_most([1, 2, 3, 1, 2, 2, 3], 2))
