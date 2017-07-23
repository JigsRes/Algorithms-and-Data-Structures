# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# For example,
# Given n = 2, return ["11","69","88","96"].

class Solution(object):
    def findStrobogrammatic(self, n):
        if n == 0:
            return [""]
        num_list = ["0" for _ in range(n)]
        common_zip = [["0", "0"], ["1", "1"], ["6", "9"], ["8", "8"], ["9", "6"]]
        middle_zip = [["0", "0"], ["1", "1"], ["8", "8"]]
        first_zip = [["1", "1"], ["6", "9"], ["8", "8"], ["9", "6"]]
        result = []

        def visit(curr_list, index):
            if index > n / 2 or (index == n / 2 and n % 2 == 0):
                result.append("".join(curr_list))
                return
            if index == n / 2 and n % 2 != 0:
                for pair in middle_zip:
                    curr_list[index] = pair[0]
                    curr_list[~index] = pair[1]
                    visit(curr_list, index + 1)
                return
            if index == 0:
                for pair in first_zip:
                    curr_list[index] = pair[0]
                    curr_list[~index] = pair[1]
                    visit(curr_list, index + 1)
                return
            for pair in common_zip:
                curr_list[index] = pair[0]
                curr_list[~index] = pair[1]
                visit(curr_list, index + 1)

        visit(num_list, 0)
        return result


obj = Solution()
print obj.findStrobogrammatic(3)