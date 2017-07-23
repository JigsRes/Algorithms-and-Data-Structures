import collections

def solution(A, B):
    lst_b=B.split()
    lst_a=A.split()
    values_b=[]
    values_a=[]

    for str in lst_a:
        lst=list(str)
        lst.sort()
        values_a.append(lst.count(lst[0]))
    values_a.sort()
    counter= collections.Counter(values_a)
    max_index = max(values_a)
    count_values=[0 for _ in range(max_index+1)]


    for i in range(1,max_index+1):
        if i in counter.keys():
            count_values[i]=counter[i]+count_values[i-1]
        else:
            count_values[i]=count_values[i-1]


    for str in lst_b:
        lst=list(str)
        lst.sort()
        b_val=lst.count(lst[0])
        currkey=min(b_val-1, max_index)
        values_b.append(count_values[currkey])
    return  values_b


print solution('aaab aaabb cccddd ffgggggaaaaa', 'aa hhccccccccccccc ddaaaaa' )