#pretty simple problem i guess
def solution(l,t):
    cord=[0,0]
    sm=l[0]
    for i in l[1:]:
        if sm==t:
            return(cord)
        sm+=i
        cord[1]+=1
        while sm>t:
            sm-=l[cord[0]]
            cord[0]+=1
    if sm==t:
        return(cord)
    else:
        return([-1,-1])
print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))
