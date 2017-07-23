
def solution(S, K):
    length=len(S)
    i=length-1
    lst=[]
    count=0
    while(i>=0):
        if count==K:
            lst.append('-')
            count=0
        if S[i]!='-':
            if S[i].isalpha():
                lst.append(S[i].upper())
            else:
                 lst.append(S[i])
            count+=1
        i-=1

    res= "".join(lst[::-1])
    print res
    return res






solution("2-4A0r7-4k",4)