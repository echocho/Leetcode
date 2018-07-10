def peak_index_in_mountain_array(A):

    #---- Solution 1: binary search
    #---- O(logN)

    left_indx, right_idx = 0, len(A) - 1

    while left_indx < right_idx:
        mid_indx = (left_indx + right_idx) // 2
        if A[mid_indx] < A[mid_indx + 1]:
            left_indx = mid_indx + 1
        else:
            right_idx = mid_indx
    return left_indx

    #---- Solution 2: linear search
    #---- O(N)

    # for indx in range(len(A)):
    #     if A[indx] > A[indx + 1]:
    #         return indx

    #---- Solution 3: directly return the index of the largest num in list
    #---- O(N + N)
    # return A.index(max(A))

print(peak_index_in_mountain_array([0,1,0]))
print(peak_index_in_mountain_array(([0,2,1,0])))
print(peak_index_in_mountain_array([1,2,3,4,1]))
