DESCRIPTION = '''
You are given two integers, x and y, 
which represent your current location on a Cartesian grid: (x, y). 
You are also given an array points where each points[i] = [ai, bi] represents 
that a point exists at (ai, bi). 
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
'''



class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        good_points = []
        for index, point in enumerate(points):
            if x == point[0] or y == point[1]:
                good_points.append((index,point))
        if good_points:
            manh_dist = []
            for _, point in good_points:
                manh_dist.append(Solution.manhattan_distance((x,y), point))
            min_index = 0
            min_val = manh_dist[0]
            for index, val in enumerate(manh_dist):
                if val < min_val:
                    min_index = index
                    min_val = val
            return good_points[min_index][0]
        else:
            return -1
        
    def manhattan_distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    
s = Solution()
print(s.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))

