# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0

    for i in range(elements):
        print(arrA)
        print(arrB)
        print(merged_arr)

        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
            print(merged_arr)
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            print(merged_arr)
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            print(merged_arr)
        else:
            merged_arr[i] = arrB[b]
            b += 1
            print(merged_arr)
            
            
         
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    
    mid = len(arr) // 2
    
    if len(arr) <=1:
        return arr
      
    else:
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)
       
        return merge(left_sorted, right_sorted)



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
