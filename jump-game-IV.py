from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        # Store indices having same value
        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([(0, 0)])   # (index, steps)
        visited = set([0])

        while queue:

            index, steps = queue.popleft()

            # Reach last index
            if index == n - 1:
                return steps

            neighbors = graph[arr[index]] + [index - 1, index + 1]

            for next_index in neighbors:

                if (0 <= next_index < n and 
                    next_index not in visited):

                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

            # Clear to avoid repeated processing
            graph[arr[index]] = []
