class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        seen_digit = False
        seen_dot = False
        seen_exp = False
        
        for i, ch in enumerate(s):
            
            if ch.isdigit():
                seen_digit = True
            
            elif ch in ['+', '-']:
                # sign only valid at start or after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            elif ch == '.':
                # dot cannot appear after exponent
                # and only one dot allowed
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            
            elif ch in ['e', 'E']:
                # only one exponent
                # exponent must come after a digit
                if seen_exp or not seen_digit:
                    return False
                
                seen_exp = True
                seen_digit = False   # must have digits after e
            
            else:
                return False
        
        return seen_digit
