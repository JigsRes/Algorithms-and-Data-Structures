class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        pntr = 0
        sentence_length = len(sentence)
        sentence_len = []
        count = 0
        for word in sentence:
            sentence_len.append(len(word))
        total_sum= sum(sentence_len)+len(sentence_len)
        i = 0
        perfect_fit=0
        while i < rows:
            curr_sum = 0
            curr_sum += sentence_len[pntr]
            while curr_sum <= cols:
                pntr += 1
                if pntr > sentence_length - 1:
                    count += 1
                    count+=(cols-curr_sum)//total_sum
                    curr_sum+=((cols-curr_sum)//total_sum)*total_sum
                    pntr = 0
                curr_sum += 1
                curr_sum += sentence_len[pntr]
            i += 1
            if pntr==0:
                perfect_fit=i
                break
        if perfect_fit>0:
            count =  count*(rows//perfect_fit)
            remainder= (rows//perfect_fit)*perfect_fit
            i=remainder
            while i < rows:
                curr_sum = 0
                curr_sum += sentence_len[pntr]
                while curr_sum <= cols:
                    pntr += 1
                    if pntr > sentence_length - 1:
                        count += 1
                        count += (cols - curr_sum) // total_sum
                        curr_sum += ((cols - curr_sum) // total_sum) * total_sum
                        pntr = 0
                    curr_sum += 1
                    curr_sum += sentence_len[pntr]
                i += 1


        return count


obj= Solution()
print obj.wordsTyping(["I", "had", "apple", "pie"],4,5)