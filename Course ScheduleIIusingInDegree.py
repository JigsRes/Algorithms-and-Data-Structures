#Two solutions First DFS, Second BFS Indegree
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
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

        for key in graph.keys():
            if visited[key]==False:
                if not  DFSUtil(key):
                    return []

        return result[::-1]





obj=Solution()
print obj.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
print obj.canFinish(2,[[1,0],[0,1]])