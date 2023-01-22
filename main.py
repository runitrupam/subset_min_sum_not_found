'''
Question :
Given an array of positive numbers,
 find the smallest positive integer value that cannot be represented as the sum of elements of any subset of a given set.
'''


# Language = Python

# Solution
# TC  = O(nlogn) Array is sorted
def smallest_positive_number(A: int) -> int:
    ans = 1
    A.sort()  # sorted in ascending order
    # iterate over the array , and check if the value <= is found .
    # if < ans then you can get the and by some combination .
    for i in range(0, len(A)):
        if A[i] <= ans:
            ans += A[i]
        else:
            break
    return ans


A = [1, 2, 3, 4, 5]
print(smallest_positive_number(A))
A = [11, 1, 2, 3, 4, 5, 56]
print(smallest_positive_number(A))
A = [11, 1, 2, 3, 4, 5, 56, 27]
print(smallest_positive_number(A))
