nums = (-10, 20, 3, -2, 5)
closest_pair = None
min_sum = float('inf')

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        pair_sum = abs(nums[i] + nums[j])
        if pair_sum < min_sum:
            min_sum = pair_sum
            closest_pair = (nums[i], nums[j])

print("Pair closest to zero:", closest_pair)
