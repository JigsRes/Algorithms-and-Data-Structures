class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        i = lower
        result=[]

        #loop while we reach the end
        while i < upper:
            #while there is a num in list pop it
            if nums:
                curr_num = nums.pop(0)
            else:   #to handle last element
                curr_num=upper+1
                # result.append(str(i+1)+"->"+str(upper))
                # print "add final" ,i+1, upper
                # break

            # if curr_num - i > 0 and curr_num!=i+1: #curr_num-1-i-1 , curr_num-i-2
            #     print "add", i + 1, curr_num - 1
            #i is the value in the previous pop
            if curr_num-i-2>=0:
                if curr_num-i-2==0:  #adding only one element
                    result.append(str(i + 1))
                else:  #adding list of elements
                    result.append(str(i + 1) + "->" + str(curr_num - 1))
            i = curr_num
        return result

obj= Solution()
print obj.findMissingRanges([0, 1, 3, 50, 75], 0,99)