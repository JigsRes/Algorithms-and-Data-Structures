
my_list=[2,3,1,2,1]

#one line list comprehensions
one_line_generator=[x*x for x in my_list]
print one_line_generator


#using map+lambda

sqaured_list_using_map= map(lambda n:n*n,  my_list)
print sqaured_list_using_map

filter_using_lambda= filter(lambda n:n>2, my_list)

print filter_using_lambda