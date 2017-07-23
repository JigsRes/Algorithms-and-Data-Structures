# Implement a data structure supporting the following operations:
#
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.

class AllOne(object):
    def __init__(self):
        self.d = {}
        self.stack_list =[]

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.d:
            curr_index = self.d[key] - 1
            stack_list_inst = self.stack_list[curr_index]
            stack_list_inst.remove(key)
            self.stack_list[curr_index] = stack_list_inst
            if len(self.stack_list)<curr_index+2:
                self.stack_list.append([key])
            else:
                self.stack_list[curr_index + 1].append(key)
            self.d[key] = self.d[key] + 1
        else:
            self.d[key] = 1
            if self.stack_list:
                self.stack_list[0].append(key)
            else:
                self.stack_list.append([key])

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.d:
            if self.d[key] == 1:
                del self.d[key]
                self.stack_list[0].remove(key)
            else:
                curr_index = self.d[key] - 1
                stack_list_inst = self.stack_list[curr_index]
                stack_list_inst.remove(key)
                self.stack_list[curr_index] = stack_list_inst
                self.stack_list[curr_index - 1].append(key)
                self.d[key] = self.d[key] - 1

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.d:
            max_val = max(self.d.values())
            return self.stack_list[max_val - 1][0]
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.d:
            min_val = min(self.d.values())
            return self.stack_list[min_val-1][0]
        else:
            return ""



        # Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("a")
obj.inc("a")
print obj.getMaxKey()
obj.inc("b")
print obj.getMaxKey()
print obj.getMinKey()
obj.dec("b")
obj.inc("a")
obj.inc("a")
obj.inc("a")
print obj.getMaxKey()
obj.inc("b")
obj.inc("b")

obj.inc("b")
obj.inc("b")
obj.inc("b")
print obj.getMinKey()
print obj.getMaxKey()





