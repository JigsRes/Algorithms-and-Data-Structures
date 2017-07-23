def generator(lst):
    for num in lst:
        yield num*num


my_list=[2,3,1,2,1]

squared_list= generator(my_list)


#one line generator
one_line_generator=(x*x for x in my_list)
print one_line_generator

print squared_list


for val in  one_line_generator:
    print val