#!/bin/python

import sys
from collections import defaultdict

def build_uniforms(s):
    uniform = {}
    current_uniform = None
    s = s + '0'
    for i in range(len(s)-1):
        if s[i] == s[i+1]:  # uniform
            if current_uniform and s[i] in current_uniform:
                current_uniform += s[i]
            else:
                current_uniform = s[i]
        else:
            if current_uniform:
                current_uniform += s[i]
                uniform[s[i]] = len(current_uniform)
                current_uniform = None
            else:
                uniform[s[i]] = 1
    return uniform


def test(uniforms, x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for key, times in uniforms.iteritems():
        weight = alphabet.find(key) + 1
        if x == weight:
            return 'Yes'
        max_weight = weight * times
        if x <= max_weight and x % weight == 0:
            return 'Yes'
    return 'No'


s = raw_input().strip()
n = int(raw_input().strip())
uniforms = build_uniforms(s)

for a0 in xrange(n):
    x = int(raw_input().strip())
    print test(uniforms, x)
  