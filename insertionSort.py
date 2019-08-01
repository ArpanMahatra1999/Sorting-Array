def insertionSort(A):
    #iteration from second to last element
    for i in range(1,len(A)):
        #take 2nd element as key in first iteration
        key = A[i]
        #initiating element before first element of each iteration
        j = i-1
        #while j isn't negative and key is less than previous element, exchange
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

A = [9,8,4,3,4,3,6,2,8,9]

insertionSort(A)

print("By Selection sort, the sorted array is: \n")
for i in range(len(A)):
    print(A[i],",")