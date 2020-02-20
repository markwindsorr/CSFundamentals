<h1 align="center">
    :scroll: Algorithms
</h1>

<h3 align="center">
	A step by step process to carry out a task
</h3>

People use computers to process large amounts of data or solve difficult problems. Two questions arise from the usage of algorithms.

* How long does my algorithm take? (Time Complexity)
* How much memory will it use? (Space Complexity)

___

## Time Complexity

### Orders-Of-Growth Classifications

|               | Order Of Growth | Description       | Example          |  
| ------------- |:---------------:| -----------------:|-----------------:| 
| Constant      | O(1)            | Statement         | Add 2 numbers    |
| Logarithmic   | O(log n)        | Divide in Half    | Binary Search    |
| Linear        | O(n)            | Simple Loop       | Find maximum     |
| Linearithmic  | O(n log n)      | Divide & Conquer  | Mergesort        |
| Quadratic     | O(n^2)          | Double Loop       | Check All pairs  |
| Cubic         | O(n^3)          | Triple Loop       | Check all triples|
| Exponential   | O(2^n)          | Exhaustive Search | Check all subsets|


___

# Sorting

### Selection Sort

| Algorithm      | In Place        | Best   | Average  |  Worst  | Remarks         |  
| -------------  |:---------------:| ------:|---------:|--------:|----------------:| 
| Selection Sort | YES             | 1/2n^2 | 1/2n^2   | 1/2n^2  | n exchanges; quadratic in best case          |


Selection sort maintains two sub arrays, the sorted array and the unsorted array. It repeatedly finds the minimum in the unsorted array and puts it at the the beginning of the unsorted array.

1. Set minimum index to current 
2. Search the unsorted list after the current index for the minimum, once found
   assign minimum_index
3. Swap the minimum_index value with the current index (which is the beginning of the unsorted list)
4. Repeat until the list is sorted

* [Python Selection Sort](https://github.com/markwindsorr/CSFundamentals/blob/master/Algorithms/SelectionSort.py)

___

### Insertion Sort

| Algorithm      | In Place        | Best   | Average  |  Worst  | Remarks         |  
| -------------  |:---------------:| ------:|---------:|--------:|----------------:| 
| Insertion Sort | YES             | n      | 1/4n^2   | 1/2n^2  | use for small or partially sorted arrays |

Insertion sort works the same way as if we were to sort a deck of cards with our hands. Considers one item at a time and inserts each into its proper place among the sorted array.

* [Python Insertion Sort](https://github.com/markwindsorr/CSFundamentals/blob/master/Algorithms/Python%20Algorithms/InsertionSort.py)

___

### Merge Sort

| Algorithm      | In Place        | Best     | Average  |  Worst  | Remarks         |  
| -------------  |:---------------:| --------:|---------:|--------:|----------------:| 
| Merge Sort     | No              | 1/2nlog n| nlogn    | nlog n  | nlogn guarantee and stable |

Merge sort works as follows. To sort an array, divide it into two halves, sort the two halves recursively, and then merge the results.

____

### Quick Sort

| Algorithm      | In Place        | Best     | Average  |  Worst  | Remarks         |  
| -------------  |:---------------:| --------:|---------:|--------:|----------------:| 
| Quick Sort     | Yes             | n        | 2nlogn   | 2nlog n  | nlogn guarantee |

Quick sort is a divide and conquer method for sorting. It works by selecting a pivot point and then sorting the two parts on either side of the pivot point independantly.

____

# Searching

### Linear Search

The simplest search algorithm in which we start at the beginning and look at each value sequentially and check it matches what we are searching for.

* [Python Linear Search](https://github.com/markwindsorr/CSFundamentals/blob/master/Algorithms/Python%20Algorithms/LinearSearch.py)


### Binary Search

Binary search can be used on a sorted list. It works by repeatedly dividing the list in two and discarding the half that we know does not contain the item we are searching. We do this until we've narrowed down the possible locations of the item to just one.

____


### Depth First Search (DFS)

DFS is used for tree, matrix or graph traversal. (Note that pre order tree traversal is a form of DFS). The algorithm starts at a root node and explores as far along as possible each branch. When implementing dfs for a graph we must check if the node is visited, because we may run the risk of getting stuck in an infinite loop.

Pseudocode:
```
def depth_first_search(Node root):
    if root == null: return
    visit(root)
    root.isVisited = true
    for node in root.adjacent:
    	if node.isVisited == false"
    		depth_first_search(node)
``` 

____



### Binary Search

Binary search can be used on a sorted list. It works by repeatedly dividing the list in two and discarding the half that we know does not contain the item we are searching. We do this until we've narrowed down the possible locations of the item to just one.

____


Sources & Thanks To

<sub><sup>Algorithms (Sedgewick, Wayne)</sup></sub>




























