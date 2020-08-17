import math
def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result
            
def sqsplit(n):
    root = math.sqrt(n)
    #Check if perfect square
    if int(root + .5) ** 2 == n:
        
        #Find all permutations
        combinations = list(splitter(str(n)))
        #print(n, combinations)
        
        #If any the sum of any permutations = n, add to total
        for i in combinations:
            sum = 0
            for j in i:
                sum += int(j)
            if sum == root:
                #print(n, root, combinations)
                return n
    return 0
            
def PE_719(n):
    total = 0
    for i in range(n + 1):
        total += sqsplit(i)
    print(total)
                
