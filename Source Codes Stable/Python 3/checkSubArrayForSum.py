# Python 3 program to check if sum exists within an array in contagious form aka subarray.

def checkSubArraySum(inputArray, arraylength, sumWanted):
	Map = {}
	current_sum = 0
	for index in range(0,arraylength):
		current_sum = current_sum + inputArray[index]
		if current_sum == sumWanted:
			print("Sum found between indexes 0 to", index)
			return
		if (current_sum - sumWanted) in Map:
			print("Sum found between indexes", Map[current_sum - sumWanted] + 1, "to", index)
			return
		Map[current_sum] = index
	print("No subarray with given sum exists.")

inputArray = [1, -3, 5, 7]
checkSubArraySum(inputArray, len(inputArray), 12)
