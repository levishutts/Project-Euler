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

def partition(s):
    #Returns the next permutation of n
    
    n = len(s)
    b, mid, e = [0], list(range(1, n)), [n]
    #print('mid', mid)
    getslice = s.__getitem__

    #range 1 to n
    '''
    for i in range(1, n-1):
        for d in combinations(mid, i):
            print('d', d)
    '''
            
    splits = (d for i in range(1, n - 1) for d in combinations(mid, i))
    all_perm = []
    
    for d in splits:
        if d is '()':
            continue

        perm = []
        for sl in map(slice, chain(b, d), chain(d, e)):
            print('sl', sl)
            print('s[sl]', s[sl])
                      
        all_perm.append([s[sl] for sl in map(slice, chain(b, d), chain(d, e))])      
    
    #all_perm = [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))]
    #        for d in splits]
    print(all_perm)
    return all_perm

def sqsplit(n, root):
    #Check each permutation of digits
    for i in partition(str(n)): 
        #If any the sum the current permutation = root, return n
        sum = 0
        for j in i:
            sum += int(j)
        if sum == root:
            #print(i)
            #Return S-number
            print(root)
            return n
    return 0
            
def PE_719(n):
    '''
    TODO:
    make a permutation and check it rather than create all permutations then
    iterate through til success
    '''
    total = 0
    i = 1
    sq_check = 1
    while sq_check <= n:
        total += sqsplit(sq_check, i)
        i += 1
        sq_check = i**2
    #S-number = 81 is skipped due logic in sqsplit. So we ever reach root 9, add 81 to total
    if n >= 9:
        total += 81
    print('Total', total)
                
