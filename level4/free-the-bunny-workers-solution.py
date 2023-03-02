from itertools import combinations
def solution(nb,nr):
    #each key should be present at least with nb-nr+1 bunny else we can find nr
    #bunny without the key, it should also be present with at most nb-nr+1 bunny
    #because there is always one of nb-nr+1 bunnies in a nr combination of nb bunnies
    key_occr=nb-nr+1
    #the number of keys that needs to be present is the combination of nb by nr
    #because every combination of the bunnies should have a unique key between them
    rslt=[[] for i in range(nb)]
    for key, bns in enumerate(combinations(range(nb), key_occr)):
        for bn in bns:
            rslt[bn].append(key)
    return(rslt)
print(solution(5,3))
            
