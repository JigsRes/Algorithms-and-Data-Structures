
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
        for i in range(num_weeks-1):
            for j in range(num_cities):
                heap_list=[]
                for city in d[j]:
                    if city in prev_list:
                        heap_list.append(days[city][i])
                        prev_list.add(j)
                if heap_list:
                    curr_cities[j]+=max(heap_list)

        for k in range(num_cities):
            if k in prev_list:
                curr_cities[k]+=days[k][num_weeks-1]
        return max(curr_cities)











obj = Solution()
print obj.maxVacationDays([[0,0,0],[0,0,0],[0,0,0]],
[[1,1,1],[7,7,7],[7,7,7]])


# print obj.maxVacationDays([[0,1,0],[0,0,0],[0,0,0]],
# [[0,0,7],[2,0,0],[7,7,7]])

print obj.maxVacationDays([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
[[0,0,7,0],[2,0,0,7],[7,7,7,7],[7,7,7,7]])

