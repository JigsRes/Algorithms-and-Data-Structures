class Solution(object):
    def outer(self):
        string="Hi"
        def inner(string2):
            print string, string2
        inner("Jigna")

obj=Solution()


list1=[0,2,1]
list2=[2,1,0]

if list1.sort()==list2.sort():
    print "True"
