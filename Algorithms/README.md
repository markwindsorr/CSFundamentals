<h1 align="center">
    :scroll: Algorithms
</h1>

<h3 align="center">
	A step by step process to carry out a task
</h3>

People use computers to process large amounts of data or solve difficult problems. Two questions arise from the usage of algorithms.

* How long does my algorithm take?
* How much memory will it use?

## Scientific Method

The same approach that scientists use to understand the natural world is effective for studying the run time of algorithms

* Observe: some feature of the natural world
* Hypothesize: a model that is consitent with the observations
* Predict: Events using the hypothesis
* Verify: the predictions by making further observations
* Validate: by repeating until the hypothesis and observations agree

___

## Orders-Of-Growth Classifications

|               | Order Of Growth | Description       | Example          |  
| ------------- |:---------------:| -----------------:|-----------------:| 
| Constant      | O(1)            | Statement         | Add 2 numbers    |
| Logarithmic   | O(log n)        | Divide in Half    | Binary Search    |
| Linear        | O(n)            | Simple Loop       | Find maximum     |
| Linearithmic  | O(n log n)      | Divide & Conquer  | Mergesort        |
| Quadratic     | O(n^2)          | Double Loop       | Check All pairs  |
| Cubic         | O(n^3)          | Triple Loop       | Check all triples|
| Exponential   | O(2^n)          | Exhaustive Search | Check all subsets|

<sub><sup>Algorithms (Sedgewick, Wayne)</sup></sub>

___


### Selection Sort

| Algorithm      | In Place        | Best   | Average  |  Worst  | Remarks         |  
| -------------  |:---------------:| ------:|---------:|--------:|----------------:| 
| Selection Sort | YES             | 1/2n^2 | 1/2n^2   | 1/2n^2  | n exchanges; quadratic in best case          |


Selection sort maintains two sub arrays, the sorted array and the unsorted array. It repeatedly finds the minimum in the unsorted array and puts it at the the beginning.

1. Set minimum index to current 
2. Search the unsorted list after the current index for the minimum, once found
   assign minimum_index
3. Swap the minimum_index value with the current index (which is the beginning of the unsorted list)
4. Repeat until the list is sorted

* [Python Selection Sort](https://github.com/markwindsorr/CSFundamentals/blob/master/Algorithms/SelectionSort.py)

___





