# def mergeSort(a,b):
#     sorted_list = []
#     lengthA = len(a)
#     lengthB = len(b)
#     i = j = 0

#     while i < lengthA and j < lengthB :
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i +=1
#         else:
#             sorted_list.append(b[j])
#             j +=1
#     return sorted_list

# if __name__ == '__main__':
#     a = [23, 12, 32, 51]
#     b = [7,9,45,51]
#     print(mergeSort(a,b))


# def mergeSort(arr):
#     if len(arr) <= 1:
#         return 
    
#     mid = len(arr) // 2;

#     left = arr[:mid]
#     right = arr[mid:]

#     mergeSort(left)
#     mergeSort(right)

#     merge_sort_list(left,right,arr)

# def merge_sort_list(a,b,arr):
#     lena = len(a)
#     lenb = len(b)
#     i = j = k = 0

#     while i < lena and j < lenb :
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i +=1
#         else:
#             arr[k] = a[j]
#             j +=1

#     while i < lena:
#         arr[k] = a[i]
#         i +=1
#         k +=1
#     while j < lenb:
#         arr[k] = a[j]
#         j+=1
#         k+=1



# if __name__ == '__main__':
#     arr = [12,21,321,2,1,3,12,43,54]
#     mergeSort(arr)
#     print(arr)
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)