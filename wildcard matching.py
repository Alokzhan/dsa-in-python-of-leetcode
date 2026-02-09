class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        s_idx_star = -1
        p_idx_star = -1
        
        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_idx_star = p_ptr
                s_idx_star = s_ptr
                p_ptr += 1
         
            elif p_idx_star != -1:
                p_ptr = p_idx_star + 1
                s_idx_star += 1
                s_ptr = s_idx_star
            
            else:
                return False
        
        return all(p[i] == '*' for i in range(p_ptr, len(p)))
