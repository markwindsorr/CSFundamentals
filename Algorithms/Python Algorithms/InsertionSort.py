def insertion_sort(a_list):

	for i in range(1, len(a_list)):

		current_item = a_list[i]

		# Compare current item with the sorted portion
		# i > 0 because there is no item on the left of index 0
		while i > 0 and a_list[i-1] > current_item:
			a_list[i] = a_list[i-1]
			i = i - 1
			a_list[i] = current_item

		print(a_list)


	return a_list

print(insertion_sort([5,2,1,9,0,4,6]))



