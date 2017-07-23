class Solution(object):
    def minArea(self, image, x, y):
        if not image:
            return 0
        rows = len(image)
        cols = len(image[0])
        matrix = []
        for row in image:
            matrix.append(list(row))
        minx = x
        maxx = x
        miny = y
        maxy = y
        bounds=[minx, maxx, miny, maxy]
        def visit(m, n, boundaries):
            if 0 <= m < rows and 0 <= n < cols:
                if matrix[m][n] == "1":
                    boundaries[0] = min(m, boundaries[0])
                    boundaries[1] = max(m, boundaries[1])
                    boundaries[2] = min(n, boundaries[2])
                    boundaries[3] = max(n, boundaries[3])
                    matrix[m][n]="0"
                    map(visit, (m + 1, m-1,m,m),(n,n,n+1,n-1),(boundaries,boundaries,boundaries,boundaries))
        print bounds
        visit(x, y, bounds)
        print bounds
        return (bounds[1] - bounds[0] + 1) * (bounds[3] - bounds[2] + 1)


obj=Solution()
print obj.minArea(["0010","0110","0100"],0,2)

#print obj.minArea(["00001"],0,4)