# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector = [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].



class Vector2D(object):
    def __init__(self, vec2d):
        self.lists = vec2d
        self.curr_list = []
        if self.lists:
            self.curr_list = self.lists.pop(0)

    def next(self):
        to_return = self.curr_list.pop(0)
        return to_return

    def hasNext(self):
        if len(self.curr_list)!=0:
            return True
        else:
            while self.lists and self.curr_list==[]:
                self.curr_list=self.lists.pop(0)
            if self.curr_list==[]:
                return False
            else:
                return True



#Your Vector2D object will be instantiated and called as such:
vec2d=[[],[-1],[1,3,4],[],[2]]
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
print v