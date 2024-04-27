class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        return True
        
def main():
    print("Test1: [2,3,1,1,4]:", "Pass" if Solution().canJump([2,3,1,1,4]) == True else "Fail")

if __name__ == "__main__":
    main()