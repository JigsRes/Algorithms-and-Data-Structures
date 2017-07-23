# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            print value1
            for v in value1:
                for coin in coins:
                    print "coin", coin
                    newval = v + coin
                    #print "Using coin new value", newval
                    if newval == amount:
                        #print "new value equal amount"
                        return nc
                    elif newval > amount:
                        #print "newval greater than amount"
                        continue
                    elif not visited[newval]:
                        print "visited", newval
                        visited[newval] = True
                        value2.append(newval)
            print visited
            value1, value2 = value2, []
        return -1
obj=Solution()
print obj.coinChange([1,2,5],8)