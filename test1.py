def  twins(a, b):
    result=[]
    zipped= zip(a,b)
    for string1, string2 in zipped:
        len1=len(string1)
        len2=len(string2)
        if len1!=len2:
            result.append("No")
            return
        if len1==0:
            result.append("Yes")
            return
        even_list1, even_list2,odd_list1, odd_list2  =[],[],[],[]
        for i in range(len1):
            if i%2==0:
                even_list1.append(string1[i])
                even_list2.append(string2[i])
            else:
                odd_list1.append(string1[i])
                odd_list2.append(string2[i])
        if even_list1.sort() ==even_list2.sort() and odd_list1.sort()==odd_list2.sort():
            result.append("Yes")
        else:
            result.append("No")
    return result


print twins(["cdab", "dcba"],["abcd", "abcd"])