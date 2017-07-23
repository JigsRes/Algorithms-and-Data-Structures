def solution(A, K):
    res=[0 for _ in range(K)]
    for i in range(len(A)-K+1):
        j=0
        m=i
        while(j<K  and A[m]>=res[j] ):
            if A[m]> res[j]:
                res= A[i:i+K]
                break
            j+=1
            m+=1

    return res




print solution([], 3)
print solution([3,2,1,3,1,2], 3)