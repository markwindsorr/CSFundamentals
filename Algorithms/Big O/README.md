<h1 align="center">
    :white_circle: Space & Time Complexity
</h1>

<h3 align="center">
	Big O is the metric we use to describe the efficiency of algorithms
</h3>


## Time Complexity

This is what we are referring too when we use the term asymptotic runtime or Big 
O.

|               | Order Of Growth | Description       | Example          |  
| ------------- |:---------------:| -----------------:|-----------------:| 
| Constant      | O(1)            | Statement         | Add 2 numbers    |
| Logarithmic   | O(log n)        | Divide in Half    | Binary Search    |
| Linear        | O(n)            | Simple Loop       | Find maximum     |
| Linearithmic  | O(n log n)      | Divide & Conquer  | Mergesort        |
| Quadratic     | O(n^2)          | Double Loop       | Check All pairs  |
| Cubic         | O(n^3)          | Triple Loop       | Check all triples|
| Exponential   | O(2^n)          | Exhaustive Search | Check all subsets|

***Big O*** describes the upper bound on the time. So if we describe an algorithm as any of the above orders of growth, it means that the algorithm is at least as fast as these. We could describe an algorithm that prints all values of an array as O(n), but we could also describe it(but wouldn't) as O(nlogn), O(n^2) ...

***Big Omega*** describes the lower bounds. That means when we say an algorithm is Omega(N), it won't be faster than that

***Big Theta*** means both Big O and Big Theta. So when an algorithm is Theta(N) if its both O(N) and Omega(N)

### Best, Worst & Expected Case

We can describe the runtime of an algorithm in 3 different ways. We'll look at quicksort as an example. Check out the quick sort section for a refresher:

***Best Case*** is not something we usually discuss when it comes to time complexity. If all elements are equal in an array, then quick sort will just traverse the array once giving a O(n).

***Worst Case*** is what happens when we are really unlucky. For example, if quick sort repeatedly picks the smallest or largest element in the array as the pivot point. In this case, the recursion doesn't divide the array in half and recurse on each half, it just shrinks the subarray by one element. This will give us O(n^2) as our worst case.

***Expected Case*** in quick sort is O(nlogn), because we expect the worst case situation not to happen. The pivot selection can be very low or very high, but it usually won't happen every single time.
___

## Space Complexity

Time is not the only thing that matters in creating an algorithm. We also care about how much memory space is required by your algorithm. For example, an array of size n requires O(n) space, where as a 2D array of size nxn requires O(n^2) space.

____

Sources & Thanks To

<sub><sup>Cracking the Coding Interview (Gayle Laakmann Mcdowell)</sup></sub>




























