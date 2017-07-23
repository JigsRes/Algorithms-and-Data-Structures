#Method that returns all the prime factors of a positive integer
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:

        print "comparing","i*i", i*i,"to n", n
        if n % i:
            print n, "not divisible by", i, "thus increment", i, "by 1"
            i += 1
        else:
            print n,"divisible by", i, "thus ",i ,"is factor", "change n to n//i","change",n, "to", n//i
            n //= i
            factors.append(i)
    print "if n >1", n, "then", n, "is prime factor. Add it"
    if n > 1:
        factors.append(n)
    return factors




print prime_factors(90)



# n = 27
# i = 2
#
# while i * i <= n:
#     print i,n
#     if i * i ==n:
#         n = i
#         print  n
#         break
#
#     while n%i == 0:
#         n = n / i
#     i = i + 1
#
# print (n)