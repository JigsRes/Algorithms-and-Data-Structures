class Solution(object):
    def maxVacationDays(self, flights, days):
        num_weeks= len(days[0])
        num_cities=len(flights)
        d={}
        for j in range(num_cities):
            can_reach_city_from=[]
            for i in range(num_cities):
                if flights[i][j]==1 or i==j:
                    can_reach_city_from.append(i)
            d[j]=can_reach_city_from

        curr_cities=[0 for _ in range(num_cities)]
        prev_list=set()
        prev_list.add(0)
        for i in range(num_weeks):
            prev_cities=curr_cities
            curr_cities=[0 for _ in range(num_cities)]
            for j in range(num_cities):
                heap_list=[]
                for city in d[j]:
                    if city in prev_list:
                        heap_list.append(prev_cities[city])
                        prev_list.add(j)
                if heap_list:
                    curr_cities[j]+=max(heap_list)
                    curr_cities[j]+=days[j][i]
        return max(curr_cities)











obj = Solution()
print obj.maxVacationDays([[0,0,0],[0,0,0],[0,0,0]],
[[1,1,1],[7,7,7],[7,7,7]])


print obj.maxVacationDays([[0,1,0],[0,0,0],[0,0,0]],
[[0,0,7],[2,0,0],[7,7,7]])

print obj.maxVacationDays([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
[[0,0,7,0],[2,0,0,7],[7,7,7,7],[7,7,7,7]])

