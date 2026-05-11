class Solution(object):
    def countTriples(self, n):
        count = 0
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_sq = a*a + b*b
                c = int(c_sq ** 0.5)
                
                if c*c == c_sq and c <= n:
                    count += 1
        
        return count
