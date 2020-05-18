# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(smallest_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] =  arr[smallest_index], arr[cur_index]
        # Your code here

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# print(bubble_sort([2,1,0,5,4]))


def my_selection(array):
    for i in range(len(array)):
        curr = i
        smallest = curr
        for j in range(smallest, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[curr], array[smallest] = array[smallest], array[curr]
    return array

print(my_selection([2,1,0,5,4]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
