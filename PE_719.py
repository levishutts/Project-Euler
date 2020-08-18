'''
Module to solve the problem here https://projecteuler.net/problem=719

An S-number is defined as a natural number, n, that is a perfect square AND its
square root can be obtained by splitting n's digits in 2 or more place and summed up.
e.g. 81 is an S-number because sqrt(81) = 8 + 1 = 9.

T(N) is the sum of all S-numbers 0 < N. The goal is to find T(10^12).
'''


import math
from itertools import chain, combinations

"""
This function is recursive and returns ALL possible permutations causing
serious issues when n > 10^9

def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result
"""

def sliceable(xs):
    #Return a sliceable version of the iterable xs.
    try:
        xs[:0]
        return xs
    except TypeError:
        return tuple(xs)

def partition(iterable):
    #Returns the next permutation of n
    '''
    TODO:
    if any of the sub-ints are greater than root, go to next permutation.
    '''
    s = sliceable(iterable)
    n = len(s)
    b, mid, e = [0], list(range(1, n)), [n]
    getslice = s.__getitem__
    splits = (d for i in range(n) for d in combinations(mid, i))
    return [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))]
            for d in splits]

def sqsplit(n):
    root = math.sqrt(n)
    #Check if perfect square
    if int(root + .5) ** 2 == n:
        
        #Check each permutation of digits
        for i in partition(str(n)): 
            #If any the sum the current permutation = root, return n
            sum = 0
            for j in i:
                sum += int(j)
            if sum == root:
                #Return S-number
                return n
    return 0
            
def PE_719(n):
    total = 0
    for i in range(n + 1):
        total += sqsplit(i)
    print(total)
                
