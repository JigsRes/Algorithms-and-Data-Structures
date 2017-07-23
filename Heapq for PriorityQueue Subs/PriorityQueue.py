import  heapq

h=[]
heapq.heappush(h,1)
heapq.heappush(h,2)
heapq.heappush(h,5)
heapq.heappush(h,3)

print h

print "pushpop"
print heapq.heappushpop(h,4)

print "push replace"
print heapq.heapreplace(h,1)  #value returned 1 is larger than the value added 2. So pushpop should be used inseatd
print "now iterating"
for i in range(len(h)):
    print heapq.heappop(h)

print h


heapq.heappush(h,1)
heapq.heappush(h,2)
heapq.heappush(h,5)
heapq.heappush(h,3)

print heapq.nlargest(3,h)  #3 sorted in reverse order

print heapq.nsmallest(3,h)