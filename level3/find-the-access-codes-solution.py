def solution(l):
    n=len(l)
    mult=[[] for i in range(n)]
    for i in range (n-1):
        for j in range(i+1,n):
            if l[j]%l[i]==0:
                mult[i].append(j)
    count=0
    for i in mult:
        for j in i:
            count+=len(mult[j])
    return(count)
#a naive solution would be in O(len(l)^3) and that would be of course inacceptable
#this one is in o(n^2), it was indeed accepted but not sure if there isn't a way
#to find a solution in nlogn
    
