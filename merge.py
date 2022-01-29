def mergeSort(arr):
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2;

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge_sort_list(left,right,arr)

def merge_sort_list(a,b,arr):
    lena = len(a)
    lenb = len(b)
    i = j = k = 0

    while i < lena and j < lenb :
        if a[i] <= b[j]:
            arr[k] = a[i]
            i +=1
        else:
            arr[k] = a[j]
            j +=1
        k +=1

    while i < lena:
        arr[k] = a[i]
        i +=1
        k +=1
    while j < lenb:
        arr[k] = a[j]
        j+=1
        k+=1



if __name__ == '__main__':
    arr = [12,21,321,2,1,3,12,43,54]
    mergeSort(arr)
    print(arr)