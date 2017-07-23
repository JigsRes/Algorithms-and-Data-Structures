
#Cannot work. Can do but have to use a different data structure
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for x, y in prerequisites:
            if y in graph.keys():
                graph[y].append(x)
            else:
                graph[y] = [x]
        print graph
        visited = [False for _ in xrange(numCourses)]

        my_stack = []
        for key in graph.keys():
            if visited[key] == False:
                my_stack.append(key)
                print "new visit", key
                while my_stack:
                    print my_stack, visited
                    key=my_stack.pop(0)
                    visited[key] = True
                    if key in graph.keys():
                        for neighbor in graph[key]:
                            if visited[neighbor] == False:
                                my_stack.append(neighbor)
                            elif neighbor in my_stack:
                                return False
        return True




obj=Solution()
print obj.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
print obj.canFinish(8,[[1,0],[0,1]])
