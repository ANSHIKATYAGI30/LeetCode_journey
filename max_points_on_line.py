class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)

        if n <= 2:
            return n

        ans = 1

        for i in range(n):

            slopes = {}

            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Reduce slope using gcd
                g = self.gcd(dx, dy)

                dx //= g
                dy //= g

                slope = (dx, dy)

                slopes[slope] = slopes.get(slope, 1) + 1

                ans = max(ans, slopes[slope])

        return ans

    def gcd(self, a, b):

        while b:
            a, b = b, a % b

        return abs(a)
