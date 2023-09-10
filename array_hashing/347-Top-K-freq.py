class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        ## the case were one number appears all the time.

        freq = [[] for i in range(len(nums) + 1)]  

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for n,c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        