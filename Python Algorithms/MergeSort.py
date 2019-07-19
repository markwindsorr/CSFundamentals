# Merge Sort

"""
Merge Sort is a Divide and Conquer Algorithm. It divides input array in two halfs, recursively calls 
itself for the two halves and then merges the two sorted halves.

The merge() function is used for merging two halves

mergeSort(array, left, right)

if r > 1:

    1. Find the middle point in the array by dividing into 2 halves:
       middle = (1 + array.count) / 2

    2. Call mergeSort for first half:
       mergeSort(array, left, middle)

    3. Call mergeSort for second half
       mergeSort(array, middle+1, right)

    4. Merge the two halves sorted in step 2 and 3:
       merge(array, left, middle, right)



"""

#___________________________________________________________________________________________________



def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)