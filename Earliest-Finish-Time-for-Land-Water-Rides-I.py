class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """

        ans = float('inf')

        # Land ride first, then water ride
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                start_water = max(land_finish, waterStartTime[j])
                finish_time = start_water + waterDuration[j]

                ans = min(ans, finish_time)

        # Water ride first, then land ride
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                start_land = max(water_finish, landStartTime[i])
                finish_time = start_land + landDuration[i]

                ans = min(ans, finish_time)

        return ans
