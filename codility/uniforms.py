#!/bin/python

import sys


def build_uniforms(s):
    uniform = {}
    current_uniform = None
    s = s + '0'
    for i in range(len(s)-1):
        if s[i] == s[i+1]:  # uniform
            # print 'match with %s%s' % (s[i], s[i+1])
            if current_uniform and s[i] in current_uniform:
                current_uniform += s[i]
            else:
                current_uniform = s[i]
        else:
            # print 'no match with %s%s' % (s[i], s[i+1])
            if current_uniform:
                # print 'no match with CU[%s] %s%s' % (current_uniform, s[i], s[i+1])
                current_uniform += s[i]
                # print 'new CU: %s' % current_uniform
                uniform[s[i]] = len(current_uniform)
                current_uniform = None
            else:
                uniform[s[i]] = 1
    return uniform


def build_weghts(keys):
    weights = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in keys.iterkeys():
            weights[letter] = alphabet.find(letter) + 1
    return weights

s = raw_input().strip()
n = int(raw_input().strip())

weights = build_weghts(build_uniforms(s))


for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    for w in weights.itervalues():
        if x % w == 0:
            print 'Yes'
            break
    print 'No'
  