import os

file=open('Employee.py', 'r')

print file.name

for line in file:
    print line


file.close()