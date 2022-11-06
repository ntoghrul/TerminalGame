

#Binary search in list
def binary_search(arr, left, right, x):
 
    
    if right >= left:
 
        mid = (right + left) // 2
 
        
        if arr[mid][1] == x:
            return 1
 
        
       
        elif arr[mid][1] > x:
            return binary_search(arr, left, mid - 1, x)
 
        
        else:
            return binary_search(arr, mid + 1, right, x)
 
    else:
       
        return -1



 

#Sorting list (Quick sort)




# function to find the partition position
def partition(array, left, right):


  pivot = array[right][1]

 
  i = left - 1

  
  
  for j in range(left, right):
    if array[j][1] <= pivot:
      
      
      i = i + 1

     
      (array[i], array[j]) = (array[j], array[i])

  
  (array[i + 1], array[right]) = (array[right], array[i + 1])

  
  return i + 1

# function to perform quicksort
def quickSort(array, left, right):
  if left < right:

    
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, right, left)

    # recursive call on the left of pivot
    quickSort(array, left, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, right)






