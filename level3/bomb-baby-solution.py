def solution(m,l):
    r=0
    while True:
        if m==l and l==1:
            return(str(r))
        elif m<1 or l<1 or m==l:
            return("impossible")
        elif m==1 or l==1:
            return (r+abs(m-l))
        else:
            if m>l:
                z=m//l
                r+=z
                m-=l*z
            else:
                z=l//m
                r+=z
                l-=m*z
#subtracting by multiplication is the only way to pass the hidden test 3 as
#iterating all substractions (by putting m-=l r+=1 in the last if else) gets
#run time error
