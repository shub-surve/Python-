#Recursion-reversing an array

def reverseArrayRec(arr):
    p1 = 0
    p2 = len(arr)-1
    temp = 0
    if p1 < p2:
        temp = arr[p1]
        arr[p2] = arr[p1]
        arr[p2] = temp

        p1+=1
        p2-=1

        reverseArrayRec(arr)

    return arr

arr = [1 , 2 , 3 , 4 , 5]

reverseArrayRec(arr)

SORTING-I
SELECTION SORT:
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
def selectionSort(a):

    for i in range(len(a)-1):
        # print(len(a))
        mini = i
        for j in range(i+1 , len(a)):
           if a[mini] < a[j]:
                mini = j
                a[i] , a[mini] = a[mini] , a[i]
                
               
    return a

a=[39 , 63 , 22 , 94 ,123]

print(selectionSort(a))

# 75. Sort Colors===Selection sort

def sortColorsSelectio(nums):

    for i in range(len(nums)-1):
        min_index = 1
        for j in range(i+1 , len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
            nums[i]  , nums[min_index]= nums[i] , nums[min_index]

        return nums
    
nums = [0 , 1 , 2 , 1 , 2]

print(sortColorsSelectio(nums))
BUBBLE SORT: In Bubble Sort algorithm, 

traverse from left and compare adjacent elements and the higher one is placed at right side. 
In this way, the largest element is moved to the rightmost end at first. 
This process is then continued to find the second largest and place it and so on until the data is sorted.
def bubbleSort(nums):

    for i in range(len(nums)-1):

        for j in range(0,len(nums)-i-1):
            print(len(nums) - i - 1)
            if nums[j] < nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
        

    return nums

nums = [23 , 44 , 21 , 13 , 4]

print(bubbleSort(nums))
            
INSERTION SORT:Insertion sort is a sorting algorithm, which sorts the array by shifting the elements one at at time. It iterates the input elements by growing the sorted array at each iteration.
def insertionSort(nums):
   
    for i in range(1 , len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current

    return nums


nums = [3 , 23 , 44 , 11 , 45]

print(insertionSort(nums))
QUICK SORT:-
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

#Steps
1. set a pevot
2. setting high and low high(lastElement) and low(firstElement)
3. set i at low & j at high
4. start placing elements smaller then pevot to left and greater to right by swapping == so it goes like i = 0 , 1 
5. after first move to high index to the left of pevot placed
def quickSortSwap(arr , low , high):
    pevot = arr[high] #setting pevot
    i = low - 1 #i stores the index of greater values
    for j in range(low , high):
        if arr[j] <= pevot:
            i = i+1

            arr[i] , arr[j] = arr[j] , arr[i]
            
    arr[i+1] , arr[high] = arr[high] , arr[i+1]

    return i+1

def quickSort(arr , low , high):

    if low > high:
       pi = quickSortSwap(arr , high , low)

       quickSort(arr , low , pi-1)
       quickSort(arr , pi+1 , high)
    
    return arr

arr = [2 , 21 , 45 , 22 , 13]
            
quickSort(arr , 0 , 4)


###Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.###

#====>BRUTE FORCE

def insersionUsingBrute(nums1: list[int] , nums2 : list[int]):
    resultList = []
    for i in range(len(nums1)):
        if nums1[i] in nums2 and nums1[i] not in resultList:
            resultList.append(nums1[i])
    return resultList

nums1 = [2 , 3 ,4 , 5]
nums2 = [3 , 4]

# print(insersionUsing(nums1 , nums2))


#===> Optimal splution
# Take a dictionary and a result list-- for(x in num1) seen[x] = 1 -- for(x in nums2) if x in seen and seen == 1
#  append it to result and return result

def insersionUsingOpt(nums1: list[int] , nums2 : list[int]):
    seen = {}
    result = []

    for i in nums1:
        seen[i] = 1
    
    for i in nums2:
        if i in seen and seen[i] == 1:
            result.append(i)
    
    return result

print(insersionUsingOpt(nums1 , nums2))


#Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

#===> Brute Force Approach

# def insersionInMultiDimBrute(nums: list[int]):


seen = {}
result = []

a = [[2 , 3 , 4 ] ,[4 , 5 , 6 , 2] ]

for i in a:
   for ele in i:
    
        seen[ele] = seen.get(ele , 0) +1

for i in seen:
    if seen[i] == len(a):
        result.append(i)

   

result
# 28. Find the Index of the First Occurrence in a String


haystack = "HELLO"
needle = "LL"


for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i + len(needle)] == needle:
        print(i)
    else:
        print(-1)
    

You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

for i in range(len(details)):
    numb_str = details[i][:10]
    age_str = details[i][11:13]
    age = int(age_str)
    numb = int(numb_str)

    if age > 60:
        print(numb)
   
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 
def kthDistinct(arr , k):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    

    disList = []
    print(frequency)

    for i in frequency:
        if frequency[i] == 1:
            disList.append(i)
            print(disList)
        
    
    if len(disList) > 1:
        return disList[k-1]
    else:
        return ""
        
   
    

arr = ["d","b","c","b","c","a"]
k = 2

print(kthDistinct(arr , k))

            
2. Add Two Numbers
# Example string
s = "hello"
score = 0
# Convert string to ASCII values
for i in range(0 , len(s)-1):
    score += abs(ord(s[i]) - ord(s[i+1]) )
    

print(score) 
    


    

