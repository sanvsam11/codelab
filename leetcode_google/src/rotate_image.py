class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix[0])
        half = size//2
        #transpose
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #mirror
        for r in range(size):
            for j in range(0, half):
                matrix[r][j], matrix[r][size-j-1] = matrix[r][size-j-1], matrix[r][j]
        return matrix

#main function to execute this file
def main():
    print("Test1: [[1,2,3],[4,5,6],[7,8,9]]:", "Pass" if Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]] else "Fail")

if __name__ == "__main__":
    main()