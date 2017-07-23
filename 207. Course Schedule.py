# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
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
        rec_stack = [False for _ in xrange(numCourses)]

        def DFSUtil(node):
            print "visiting node", node
            visited[node]=True
            rec_stack[node]=True
            if node in graph.keys():
                for neighbor in graph[node]:
                    if visited[neighbor]==False:
                        if DFSUtil(neighbor)==False:
                            return False
                    elif rec_stack[neighbor]==True:
                        return False
            rec_stack[node]=False
            return True

        for key in graph.keys():
            if visited[key]==False:
                return DFSUtil(key)


        return True




obj=Solution()
# print obj.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
print obj.canFinish(2,[[1,0],[0,1]])