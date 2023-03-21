from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        count_dict = Counter(nums)
        #print(count_dict)
        #print(list((key for key in count_dict if count_dict[key]>=2)))
        if len(list((key for key in count_dict if count_dict[key]>=2)))==0:
            return False
        else:
            return True
