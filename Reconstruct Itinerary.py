import heapq

class Solution(object):
    def findItinerary(self, tickets):
        d={}
        for ticket in tickets:
            if ticket[0] in d.keys():
                heapq.heappush(d[ticket[0]],ticket[1])
            else:
                new_list=[]
                heapq.heappush(new_list,ticket[1] )
                d[ticket[0]]=new_list

        itinerary=[]
        key="JFK"

        # def goToNext(from_airport):
        #     if d and from_airport in d.keys():
        #         itinerary.append(from_airport)
        #         to = heapq.heappop(d[from_airport])
        #         correctPath= goToNext(to)
        #         if not correctPath:
        #             hold=to
        #             to=heapq.heappop(d[from_airport])
        #             itinerary.pop()
        #             itinerary.append(to)
        #             d[from_airport].append(hold)
        #             return goToNext(to)
        #
        #
        #     if d and from_airport not in d.keys():
        #         return False
        #
        #     if not d:
        #         return True

        def goToNext(from_airport):
            print from_airport
            if not d:
                return True
            itinerary.append(from_airport)
            if d and from_airport in d.keys():
                not_visited= d[from_airport]
                for to_aiport in not_visited:
                    d[from_airport].pop()
                    correctPath = goToNext(to_aiport)
                    if correctPath:
                        if d[from_airport]==[]:
                            d.pop(from_airport)
                        return True
                    else:
                        print "back track"
                        d[from_airport].append(to_aiport)
                itinerary.pop()
                return False


            if d and from_airport not in d.keys():
                return False

        goToNext(key)


        # while key in d.keys() and d[key]:
        #     to=heapq.heappop(d[key])
        #     itinerary.append(to)
        #     if not d[key]:
        #         d.pop(key, None)
        #     key=to

        print itinerary

obj=Solution()
obj.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])

#Expected Output:

# ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
