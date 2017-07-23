
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid=(l+r)/2
            if matrix[mid//cols][mid%cols]==target:
                return True
            elif matrix[mid//cols][mid%cols]<target:
                l=mid+1
            else:
                r=mid-1
        return False


obj=Solution()
print obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)