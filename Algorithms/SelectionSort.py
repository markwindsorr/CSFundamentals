def selection_sort(a_list):

	for i in range(len(a_list)):

		# Initially set min position to our current index
		min_index = i

		# Start traversing past our current index to find new
		# minimum index
		for j in range(i+1, len(a_list)):
			if a_list[min_index] > a_list[j]:
				min_index = j

		# Once we've found the minimum we swap the minimum
		# with the beginning of the unsorted list
		temp = a_list[i]
		a_list[i] = a_list[min_index]
		a_list[min_index] = temp

	return a_list

print(selection_sort([5,2,1,9,0,4,6]))
