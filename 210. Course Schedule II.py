# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        for x, y in prerequisites:
            if y in graph.keys():
                graph[y].append(x)
            else:
                graph[y] = [x]
        #print graph
        visited = [False for _ in xrange(numCourses)]
        rec_stack = [False for _ in xrange(numCourses)]
        result=[]

        def DFSUtil(node):
            #print "visiting node", node
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
            result.append(node)
            return True

        for key in range(numCourses):
            if visited[key]==False:
                if not  DFSUtil(key):
                    return []

        return result[::-1]