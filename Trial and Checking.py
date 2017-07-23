# import math
# a=-1
# a_int=bin(a)
# append_zeros=3
# a_int="0"*0+a_int
# print a_int
#
# for i in range(-10,10):
#     print i, ~i
#
# string_a=bin(a)[2:]
#
# print max(3,3)
#
#
# print math.ceil(1.5)
#
#
# print 1<<1

def visit(num):
    return True if num<2 else False


filtered= filter(visit,(0,5,1,2,-1,3))
print filtered