import re

string="abc"
print string[:0]
def printvalue(x):
    print x

print repr([1,2,3])

print bin(12)
float_value=12.2
# print bin(operator.index(1200))

print bool(0)
print bool(None)


print repr(bytearray([1,2]))
print str.encode("Hi\n")

for byte in bytearray("Hello"):
    print (byte)

for byte in bytearray([1,2]):
    print byte

print callable(12)
print callable(sum)
print callable(printvalue)


print complex(1,2)
print dir(re)

for byte in bytearray("Helllo"):
    print type(byte)

print(divmod(8,6))

print(divmod(5.5,2))


print "Hello".istitle()
print "hELLO".istitle()
print "hello".istitle()
print "HELLO".istitle()

print "hello".rjust(10)