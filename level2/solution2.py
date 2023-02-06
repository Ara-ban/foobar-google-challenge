def solution(l):
    ch=[]
    for i in l:
        x=i.split(".")
        if len(x)==3:
            ch.append([int(x[0]),int(x[1]),int(x[2]),i])
        elif len(x)==2:
            ch.append([int(x[0]),int(x[1]),-1,i])
        else:
            ch.append([int(x[0]),-1,-1,i])
    ch.sort()
    for i in range(len(ch)):
        ch[i]=ch[i][3]
    return(ch)
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
