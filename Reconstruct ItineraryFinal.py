
import collections

class Solution(object):
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        targetsb=collections.defaultdict(list)

        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        for a, b in sorted(tickets):
            targetsb[a] += b,

        for k in targets.keys():
            print targets[k], targetsb[k]



        def visit(airport):
            print "from", airport
            while targets[airport]:
                visiting=targets[airport].pop()
                print visiting
                visit(visiting)
            route.append(airport)

        visit('JFK')
        return route[::-1]

obj=Solution()
print obj.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])

#Expected Output:

# ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
