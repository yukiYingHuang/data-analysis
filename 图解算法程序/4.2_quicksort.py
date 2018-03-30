import random

def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[-1]  #以最后一个数为基准值
    # pivot = array[0]  #以第一个数为基准值
    # sub-array of all the elements less than the pivot
    less = [i for i in array[:-1] if i <= pivot]  #以最后一个数为基准值
    # less = [i for i in array[1:] if i <= pivot]  #以第一个数为基准值
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[:-1] if i > pivot]  #以最后一个数为基准值
    # greater = [i for i in array[1:] if i > pivot]  #以第一个数为基准值
    return quicksort(less) + [pivot] + quicksort(greater)

def quicksort1(array):  #以中间的数作为基准值
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[len(array)//2]
    array.pop(len(array)//2)
    # sub-array of all the elements less than the pivot
    less = [i for i in array if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 23, -2, 3,6,10]))
print(quicksort1([10, 23, -2, 3,6,10]))