
def  consecutive(num):
    sumarray=[]
    curr_sum=0
    for i in range(1,num/2+2):
        curr_sum+=i
        sumarray.append(curr_sum)
    len1=len(sumarray)
    print sumarray
    count=0
    left=0
    right=len1-1
    while left<=right:
        if sumarray[left]==num:
            count+=1
            left+=1
            continue
        if sumarray[right]==num:
            count+=1
            right-1
            continue
        differnce=sumarray[right]-sumarray[left]
        if differnce==num:
            count+=1
            left+=1
            right-=1
            continue
        elif differnce>num:
            left+=1
            continue
        else:
            right

    # for i in range(len1-1,0,-1):
    #     for j in range(i-1, 0, -1):
    #         if sumarray[i]==num:
    #             count+=1
    #             break
    #         if sumarray[i]-sumarray[j]==num:
    #             print i, j
    #             count+=1
    #         elif sumarray[i]-sumarray[j]>num:
    #             break
    return count

print consecutive(15)