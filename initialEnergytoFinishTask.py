class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """

        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        answer = 0

        for actual, minimum in tasks:

            # Need more initial energy
            if energy < minimum:

                answer += (minimum - energy)

                energy = minimum

            # Finish task
            energy -= actual

        return answer
