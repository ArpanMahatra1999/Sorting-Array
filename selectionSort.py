def selectionSort(A):
    #for i number of iteration
    for i in range(len(A)):
        #first element is to be compared
        min_idx = i
        #first element is to be compared with all remaining elements
        for j in range(i+1,len(A)):
            #if first element is greater than 2nd, exchange to first and again iterated by above until minimum element is determined and indexed
            if A[min_idx]>A[j]:
                min_idx = j
        #swapping first element with minimum one
        A[i],A[min_idx] = A[min_idx],A[i]

A = [9,8,4,3,4,3,6,2,8,9]

selectionSort(A)

print("By Selection sort, the sorted array is: \n")
for i in range(len(A)):
    print(A[i],",")