# https://leetcode.com/problems/rotate-image/
class Solution:
    '''
    Approaches
    1. Can use rotation matrix? No, inplace rotation is to be done.
       1.1. Create rotation matrix
       1.2. Multiple coordinate matrxi witg  rotation matrix to generate required coordinate matrix
       1.3. Map the content of input matrix according to the coordinate matrix.
    2. In place:
       1.1. Compute mapping of rotated matrix (not inplace?)          
       1.2. Set elements using mapping
       Details:
       For corner elements of outermost border
       1. t1 = a[0, n - 1]
       2. a[0, n - 1] = a[0, 0]
       3. t2 = a[n-1, n - 1]
       4. a[n - 1, n - 1] = t1
       5. t1 = a[n - 1, 0]
       6. a[n - 1, 0] = t2
       7. a[0, 0] = t1
       
       For next border elements
       1. t1 = a[1, n - 2]
       2. a[1, n - 2] = a[1, 1]
       3. t2 = a[n-2, n - 2]
       4. a[n - 2, n - 2] = t1
       5. t1 = a[n - 2, 1]
       6. a[n - 2, 1] = t2
       7. a[1, 1] = t1
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        t1 = matrix[0][n - 1]
        matrix[0][n - 1] = matrix[0][0]
        t2 = matrix[n-1][n - 1]
        matrix[n - 1][n - 1] = t1
        t1 = matrix[n - 1][0]
        matrix[n - 1][0] = t2
        matrix[0][0] = t1
        
        
        #n = len(matrix)
        t1 = matrix[1][n - 1]
        matrix[1][n - 1] = matrix[0][1]
        t2 = matrix[n-1][1]
        matrix[n - 1][1] = t1
        t1 = matrix[1][0]
        matrix[1][0] = t2
        matrix[0][1] = t1
