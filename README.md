Recursion is a programming technique in which a function calls itself directly or indirectly in order to solve a problem. It involves breaking down a complex problem into simpler sub-problems, which are easier to solve. Recursion is particularly useful for tasks that can be defined in terms of similar subtasks, such as traversing data structures like trees and graphs, or solving problems that exhibit optimal substructure and overlapping subproblems, such as dynamic programming problems.

### Key Components of Recursion

1. **Base Case**: The condition under which the recursive function stops calling itself. This prevents infinite recursion and ensures that the function terminates.
2. **Recursive Case**: The part of the function where the function calls itself with modified arguments, moving towards the base case.

### Example of Recursion in Python

Here is a simple example of a recursive function that calculates the factorial of a number:

```python
def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Testing the function
print(factorial(5))  # Output: 120

```

In this example:

- The **base case** is when `n` is 0. The function returns 1, which stops the recursion.
- The **recursive case** is when `n` is greater than 0. The function calls itself with `n - 1`.

### Understanding Recursion with a Visual Example: Fibonacci Sequence

The Fibonacci sequence is another classic example where recursion can be used. The Fibonacci sequence is defined as follows:

- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)` for `n > 1`

Here is the recursive implementation in Python:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the function
print(fibonacci(7))  # Output: 13

```

## PROBLEMS

### 1. Print GFG n times without the loop.

**Example:**

```
Input:
5
Output:GFG GFG GFG GFG GFG
```

**Your Task:** This is a function problem. You only need to complete the **function printGfg()** that takes **N as parameter** and prints N times **GFG** recursively. Don't print newline, it will be added by the driver code.

```java
class Solution {

    void printGfg(int N) {
        if( N > 0){
            System.out.print("GFG ");
            N--;
            printGfg(N);
        }
        else{
            return;
        }
        
    }
}
```

### 1. Print numbers from *1 to n* without the help of loops. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively.

```java
class Solution
{
    
  static void printNos(int N) {
        if (N > 0) {
            printNos(N - 1);  // Recurse with N-1
            System.out.print(N + " ");  // Print the number after the recursive call
        }
    }
}

```

## 3. Print numbers from **N to 1** (space separated) without the help of loops.

```java
class Solution {

    void printNos(int N) {
        if(N > 0){
            System.out.print(N + " ");
            printNos(N-1);
        } else {
            return;
        }
    }
}
```

```

### 2. Sorting Algorithms

### a. Selection Sort

Selection Sort is an in-place comparison sorting algorithm. It divides the input list into two parts: the sublist of items already sorted, and the sublist of items remaining to be sorted.

**Code:**

```python
def selectionSort(a):
    for i in range(len(a) - 1):
        mini = i
        for j in range(i + 1, len(a)):
            if a[mini] > a[j]:
                mini = j
        # Swap the found minimum element with the first element
        a[i], a[mini] = a[mini], a[i]
    return a

a = [39, 63, 22, 94, 123]
print(selectionSort(a))

```

### b. Bubble Sort

Bubble Sort repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order.

**Code:**

```python
def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums = [23, 44, 21, 13, 4]
print(bubbleSort(nums))

```

### c. Insertion Sort

Insertion Sort works by building a sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Code:**

```python
def insertionSort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums

nums = [3, 23, 44, 11, 45]
print(insertionSort(nums))

```

### d. Quick Sort

QuickSort is a divide-and-conquer algorithm that works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.

**Code:**

```python
def quickSortSwap(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = quickSortSwap(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

arr = [2, 21, 45, 22, 13]
print(quickSort(arr, 0, len(arr) - 1))

```

### 3. Finding Intersection of Two Arrays

### a. Brute Force Method

**Code:**

```python
def intersectionUsingBrute(nums1, nums2):
    resultList = []
    for i in nums1:
        if i in nums2 and i not in resultList:
            resultList.append(i)
    return resultList

nums1 = [2, 3, 4, 5]
nums2 = [3, 4]
print(intersectionUsingBrute(nums1, nums2))

```

### b. Optimal Solution Using HashMap

**Code:**

```python
def intersectionUsingOpt(nums1, nums2):
    seen = {}
    result = []
    for i in nums1:
        seen[i] = 1
    for i in nums2:
        if i in seen and seen[i] == 1:
            result.append(i)
            seen[i] = 0  # Ensuring unique elements in result
    return result

print(intersectionUsingOpt(nums1, nums2))

```

### 4. Find Common Elements in Multiple Arrays

To find common elements in multiple 2D arrays, we can use a hashmap to count occurrences of each element.

**Code:**

```python
a = [[2, 3, 4], [4, 5, 6, 2]]
seen = {}
result = []

for i in a:
    for ele in i:
        seen[ele] = seen.get(ele, 0) + 1

for i in seen:
    if seen[i] == len(a):
        result.append(i)

print(result)  # Output: [2, 4]

```

### 5. Find the Index of the First Occurrence in a String

**Code:**

```python
haystack = "HELLO"
needle = "LL"

found = -1  # Initialize found index to -1
for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i + len(needle)] == needle:
        found = i
        break  # Exit loop once found
print(found)

```

### 6. Count Passengers Over Age 60

This script extracts and counts passengers over age 60 from a list of compressed passenger information strings.

**Code:**

```python
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
count = 0

for detail in details:
    age = int(detail[11:13])
    if age > 60:
        count += 1

print(count)

```

### 7. Kth Distinct String in an Array

Given an array of strings, find the `k`-th distinct string.

**Code:**

```python
def kthDistinct(arr, k):
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1

    disList = []
    for key, value in frequency.items():
        if value == 1:
            disList.append(key)

    if len(disList) >= k:
        return disList[k-1]
    else:
        return ""

arr = ["d", "b", "c", "b", "c", "a"]
k = 2
print(kthDistinct(arr, k))

```

### 8. ASCII Difference Score

Calculate the difference score between adjacent characters in a string based on their ASCII values.

**Code:**

```python
s = "hello"
score = 0

for i in range(len(s) - 1):
    score += abs(ord(s[i]) - ord(s[i + 1]))

print(score)

```

###**
