class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        start = [i for i in range(n)]
        
        memo[0] = nums[0]
        start[0] = 0
        
        for i in range(1, n):
            if start[i-1] > 0:
                p1 = memo[start[i-1]-1] * memo[i-1] * nums[i]
                p2 = memo[i-1] * nums[i]
                p3 = nums[i]
                p4 = p2
                
                if nums[start[i-1]] != 0:
                    p4 = int(p2 / nums[start[i-1]])

                # print(i, p1,p2,p3, p4)
                if p1 >= max(p1, p2, p3, p4):
                    start[i] = start[start[i-1]-1]
                    memo[i] = p1
                elif p2 >= max(p1, p2, p3, p4):
                    start[i] = start[i-1]
                    memo[i] = p2
                elif p3 >= max(p1, p2, p3, p4):
                    start[i] = i
                    memo[i] = p3
                else:
                    start[i] = start[i-1] + 1
                    memo[i] = p4

            else:
                p2 = memo[i-1] * nums[i]
                p3 = nums[i]
                p4 = p2
                if nums[start[i-1]] != 0:
                    p4 = int(p2 / nums[start[i-1]])]
                
                # print(i, p2, p3, p4)
                
                if p2 >= max(p2, p3, p4):
                    start[i] = start[i-1]
                    memo[i] = p2
                elif p3 >= max(p2, p3, p4):
                    start[i] = i
                    memo[i] = p3
                else:
                    start[i] = start[i-1] + 1
                    memo[i] = p4
        # print(memo)
        return max(memo)