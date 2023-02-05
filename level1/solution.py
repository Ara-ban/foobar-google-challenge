def solution(s):
    # Your code here
    #thought process: 2:29 AM 2/4
    #first idea is to build a while where there is a counter that starts 
    #at one and can go up to the length of the list divided by 2(if list 
    #is even else divided by 3 if dividable by 3 etc..) and take everytime
    #the first i characters of the string and see if they repeat throughout
    #the string, else increment i where i is the counter.
    #now is this a general optimal approach? i will leave the answer for 
    #tomorrow
    #re, 00:38 2/5 can't think of another way and didn't get a lot of time today to think
    #about so here we go
    i=1
    while i<=len(s)//2:
        if len(s)%i==0:
            if s.count(s[:i])==len(s)//i:
                return (len(s)//i)
        i+=1
    return(1)

