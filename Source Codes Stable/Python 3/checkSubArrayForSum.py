'''
Check if sum exists within an array in contagious form aka sum in subarray.
'''


def checkSubArraySum(inputArray, arraylength, sumWanted):
    Map = {}
    current_sum = 0
    for index in range(0, arraylength):
        current_sum = current_sum + inputArray[index]
        if current_sum == sumWanted:
            print("\nSum of {} found between indexes 0 to {}.".format(
                sumWanted, index))
            return
        if (current_sum - sumWanted) in Map:
            print("\nSum of {} found between indexes {} to {}.".format(
                sumWanted, Map[current_sum - sumWanted] + 1, index))
            return
        Map[current_sum] = index
    print("\nNo subarray with sum of {} exists.".format(sumWanted))


inputArray = [1, -3, 5, 7]
checkSubArraySum(inputArray, len(inputArray), 12)
checkSubArraySum(inputArray, len(inputArray), 4)
