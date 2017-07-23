class Solution(object):
    def calcEquation(self, equations, values, queries):
       d={}
       for equation, value in zip(equations, values):
           if equation[0] in d.keys() and equation[1] not in d.keys():
               d[equation[1]]=[d[equation[0]][0], d[equation[0]][1]*value]
           if equation[1] in d.keys() and equation[0] not in d.keys():
               d[equation[0]] = [d[equation[1]][0]* value, d[equation[1]][1]]













obj= Solution()
obj.calcEquation([["a", "b"], ["b", "c"]],[2.0, 3.0]
, [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]] )
           # equations = [["a", "b"], ["b", "c"]],
           # values = [2.0, 3.0],
           # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]].
           #