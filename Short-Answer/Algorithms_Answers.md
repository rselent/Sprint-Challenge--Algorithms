#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

# Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
`O(n)`  
This algorithm is an example of linear time, because its runtime scales linearly with `n`.

For example, if `n = 1`, it goes through `one` iteration:  
It clears the `while` conditional on the first pass, because `0 < 1`, but after it increments `a` in the next step (where `a = 1` now), it will fail that while conditional, because `1 !< 1`.  

Likewise, if `n = 2`, it goes through `two` iterations:  
On its first pass, it clears the initial `while` conditional because, again, `0 < 8`, where it will then increment `a` such that `a = 4`.  
On its second pass, it clears the conditional again, because `4 < 8`, where it will then increment `a` again, such that `a = 8` now.  
But because `a` is equal to `n` now, it will fail the `while` conditional on its next pass, because `8 !< 8`.


```python
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
`O(nlogn)`  
This algorithm is an example of superlinear time, because its nested loops run in linear and logarithmic times, respectively.

The inner `while` loop is logarithmic because it is assumed that `j` is being incremented at double the rate that `n` is being incremented at (`O(logn)`), which is controlled / incremented by the outer `for` loop (`O(n)`).  
Thus, `O(n)` * `O(logn)` = `O(nlogn)`

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      return 2 + bunnyEars(bunnies-1)
```
`O(n)`  
This algorithm is another example of linear time.

Regardless of its recursive nature, the function will still only run / be called `n` times -- once per bunny -- before reaching the base case.

# Exercise II

* Start on ground floor
* Go to middle floor (between ground and top floors)
* drop_egg
	* if egg breaks, move to middle floor between current location and ground floor
	* if egg doesn't break, move to middle floor between current location and top floor
	* repeat `drop_egg` until floor `f` (highest floor egg doesn't break on) is found

