class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0) #pop the first element and call recursively
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n) #append the popped elememt to the permutation
            result.extend(perms) #extend the result with all permutations for this call
            nums.append(n) #append the number popped back to nums
        return result
        