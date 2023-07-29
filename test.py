class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pure_number = sorted(list(set(nums)))
        all_combine = []
        for i in range(len(pure_number)):
             for j in range(i+1, len(pure_number)):
                 for k in range(j+1, len(pure_number)):
                     all_combine += [pure_number[i],pure_number[j],pure_number[k]]
        true_combine =[sum(a) == 0 for a in all_combine]
        return true_combine
    