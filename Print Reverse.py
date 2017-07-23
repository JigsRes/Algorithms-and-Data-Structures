def printreverse(string, i):
    if i>len(string)-1:
        return
    printreverse(string,i+1)
    print string[i],

def printStraight(string, i):
    if i>len(string)-1:
        return
    print string[i],
    printStraight(string,i+1)



string='Hello World'
printStraight(string,0)
print
printreverse(string,0)
