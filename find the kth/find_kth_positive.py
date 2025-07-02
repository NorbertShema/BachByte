'''
Given an array arr of positive integers sorted in a strictly increasing order. 
and an integer k, 
write a function find_kth_positive() 
that returns the kth positive integer that is missing from this array
'''

def find_kth_positive(arr, k):
    # Write your code here
    left , right = 0, len (arr)-1
    
    while left <= right:
        mid = (left+ right)//2
        missing = arr [mid] - (mid +1)

        if missing < k:
            left = mid +1
        else:
            right = mid -1
    
    return left + k    

arr = [2, 3, 4, 7, 11]
k = 5
print(find_kth_positive(arr, k))  
# Expected output: 9


