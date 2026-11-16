class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # Empty list for resulting permutations
        # perms = [[]]

        # # Outer loop for numeber permutations to be done n! 
        # for n in nums:
        #     # initialize temp list fot permutations
        #     new_perms = []
        #     # each list of number got for perm
        #     for p in perms:
        #         # appending loop for n + 1 perm in the possible index
        #         for i in range(len(p) + 1):
        #             p_copy = p.copy()
        #             p_copy.insert(i, n)
        #             new_perms.append(p_copy)
        #         perms = new_perms
        # return perms        
        
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for n in nums:
                if n not in cur:          
                    cur.append(n)         
                    dfs(cur)              
                    cur.pop()             

        dfs([])
        return res
