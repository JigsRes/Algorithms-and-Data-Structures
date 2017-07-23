class Solution(object):
    def palindromePairs(self, words):
        result_list=[]
        d_match_to_1={}
        d_match_to_2 = {}
        d_match_1={}
        d_match_2={}
        for i, word in enumerate(words):
            rev_word=word[::-1]
            d_match_1[word]=[i]
            for j in range(1,len(word)+1):
                if self.isPalindrom(word[:j]):
                    d_match_2[word[j:]]=d_match_2.get(word[j:],[])+[i]

            d_match_to_1[rev_word]=[i]
            for j in range(1,len(rev_word)+1):
                if self.isPalindrom(rev_word[:j]):
                    d_match_to_2[rev_word[j:]]=d_match_to_2.get(rev_word[j:],[])+[i]
        print d_match_1
        print d_match_2
        print d_match_to_1
        print d_match_to_2


        for key in d_match_to_1.keys():
            if key in d_match_1:
                for value_l in  d_match_to_1[key]:
                    for value_r in d_match_1[key]:
                        if value_l != value_r:
                            print key, [value_l,value_r]
                            result_list.append([value_l,value_r])
            if key in d_match_2:
                for value_l in  d_match_to_1[key]:
                    for value_r in d_match_2[key]:
                        if value_l != value_r:
                            print key, [value_l, value_r]
                            result_list.append([value_l,value_r])

        for key in d_match_to_2.keys():
            if key in d_match_1:
                for value_l in  d_match_to_2[key]:
                    for value_r in d_match_1[key]:
                        if value_l != value_r:
                            print key, [value_l, value_r]
                            result_list.append([value_l,value_r])


        return result_list









    def isPalindrom(self, string):
        if string == string[::-1]:
            return True
        else:
            return False




obj= Solution()
print obj.palindromePairs(["abcd","dcba","lls","s","sssll"])
print obj.palindromePairs(["","s"])