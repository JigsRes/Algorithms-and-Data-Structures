class Solution(object):
    def numSqaures(self, n):
        i=1
        squares=[]
        while i*i<=n:
            squares.append(i*i)
            i+=1
        print squares
        dp_old=[False for _ in xrange(n+1)]
        dp_new=[False for _ in xrange(n+1)]
        count=0
        dp_old[0]=True
        while True:
            count += 1
            print dp_old, count

            for i in xrange(0,n+1):
                for square in squares:
                    if dp_old[i]==True and square+i<=n:
                        dp_new[square+i]=True

            if dp_new[n]==True:
                break
            dp_old=dp_new
            dp_new=[False for _ in xrange(n+1)]
            #dp_new[0]=True
        print count








obj=Solution()
obj.numSqaures(3)




