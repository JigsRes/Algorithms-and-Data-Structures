# class Solution(object):
#     def getSum(self, a, b):
#         a_string = bin(a)[2:]
#         b_string = bin(b)[2:]
#         length_a = len(a_string)
#         length_b = len(b_string)
#         max_len = max(length_a, length_b)
#         a_string = "0" * (max_len - length_a) + a_string
#         b_string = "0" * (max_len - length_b) + b_string
#         carry = 0
#         i = -1
#         j = -1
#         result = 0
#         print a_string, b_string
#         while i >= -max_len:
#             count_1 = 0
#             count_1 = 1 if a_string[i] == "1" else 0
#             count_1 += 1 if b_string[i] == "1" else 0
#             count_1 += carry
#
#             print i,count_1, carry
#             if count_1 == 1 or count_1 == 3:
#                 result += 2 ** (~i)
#             if count_1 == 2 or count_1 == 3:
#                 carry = 1
#             else:
#                 carry = 0
#             i -= 1
#             print result
#
#         result += 2 ** (max_len ) if carry else 0
#
#         return result


class Solution(object):
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        print bin(MAX)

        def calSum(m, n):
            print m, n
            print bin(m), bin(n)
            if n == 0:
                return m
            res, carry = (m ^ n) & mask, ((m & n) << 1) & mask
            return calSum(res, carry)

        result = calSum(a, b)
        print result <= MAX
        return result if result <= MAX else  ~(result ^ mask)

#print len('11111111111111111111111111111101')

obj=Solution()
print obj.getSum(-2,-1)


1111111111111111111111111111111
11111111111111111111111111111101