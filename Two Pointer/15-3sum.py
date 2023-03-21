"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

TC -> O(n logn) + O(n^2)

"""

def(nums):
	res = []
	nums.sort()

	for i, a in enumerate(nums):
		if i > 0 and a == nums[i - 1]: # just check it's not first time elm coming then check if prefix is also same then cont
			continue
		l, r = i+1, len(nums) - 1
		while l<r:
			if a + nums[l] + nums[r] > 0:
				r-=1
			elif a + nums[l] + nums[r] < 0:
				l+=1
			else:
				res.append([a, nums[l], nums[r]])
				l += 1
				while nums[l] == nums[l - 1] and l < r:
					l+=1
	return res