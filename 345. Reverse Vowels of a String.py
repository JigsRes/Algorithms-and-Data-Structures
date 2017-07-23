#Time Limit Exceeded
class Solution(object):
    def reverseVowels(self, s):
        list_string= list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left <right and list_string[left] not in ["a","e","i", "o", "u", "A", "E", "I", "O","U"]:
                left+=1
            while  right>left and list_string[right] not in ["a","e","i", "o", "u", "A", "E", "I", "O","U"] :
                right-=1
            list_string[left], list_string[right]= list_string[right], list_string[left]
            left+=1
            right-=1
        return "".join(list_string)

if __name__=="__main__":
    obj= Solution()
    print(obj.reverseVowels("hello"))
