class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """

        n = len(s)

        queue = [0]
        farthest = 0

        while queue:

            i = queue.pop(0)

            # Reachable range
            start = max(i + minJump, farthest)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0':

                    if j == n - 1:
                        return True

                    queue.append(j)

            # Avoid revisiting same range
            farthest = end + 1

        return n == 1
