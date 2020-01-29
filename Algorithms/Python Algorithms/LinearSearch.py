

def linear_search(a_list, x):

	for item in a_list:
		if item == x:
			return item
	
	print("Item not found")
	
	return -1 

def linear_search_index(a_list, x):

	for i in range(0, len(a_list)):
		if a_list[i] == x:
			return a_list[i]
	
	print("Item not found")
	
	return -1

print(linear_search([1,2,3,4,5,6,7,8,9,0], 5))