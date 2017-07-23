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