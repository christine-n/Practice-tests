def targetSum():
	arr = [12, 3, 1, 2, -6, 5, -8, 6]
	target_sum = -2
	n = len(arr)
	arr.sort()
	# arr = [-8, -6, 1, 2, 3, 5, 6, 12]
	arr_sums = []
	for i in range(n):
		left = i + 1
		right = n - 1
		while left < right:
			res_sum = arr[i] + arr[left] + arr[right]
			if res_sum == target_sum:
				arr_sums.append([arr[i], arr[left], arr[right]])
				left += 1
				right -= 1
			elif res_sum < target_sum:
				left +=1
			elif res_sum > target_sum:
				right -= 1

	return arr_sums

print(targetSum())