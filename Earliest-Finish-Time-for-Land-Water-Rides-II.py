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
        
        # Land ride first -> Water ride
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]
            
            for j in range(len(waterStartTime)):
                # start water ride after land ride finishes
                water_start = max(land_finish, waterStartTime[j])
                total_finish = water_start + waterDuration[j]
                
                ans = min(ans, total_finish)
        
        
        # Water ride first -> Land ride
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]
            
            for i in range(len(landStartTime)):
                # start land ride after water ride finishes
                land_start = max(water_finish, landStartTime[i])
                total_finish = land_start + landDuration[i]
                
                ans = min(ans, total_finish)
        
        return ans
