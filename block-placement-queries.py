class Solution(object):
    def getResults(self, queries):

        obstacles = []
        ans = []

        for q in queries:

            # add obstacle
            if q[0] == 1:

                obstacles.append(q[1])

            else:

                x = q[1]
                sz = q[2]

                arr = [0]

                for ob in obstacles:
                    if ob <= x:
                        arr.append(ob)

                arr.append(x)

                arr.sort()

                max_gap = 0

                for i in range(1, len(arr)):

                    max_gap = max(max_gap,
                                  arr[i] - arr[i - 1])

                ans.append(max_gap >= sz)

        return ans
