# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

class Solution:
    @staticmethod
    def solution(A):
        min_value = float('inf')
        total_left = 0
        total_right = sum(A)

        for i in range(len(A) - 1):
            total_left += A[i]
            total_right -= A[i]

            diff_from_sides = abs(total_right - total_left)

            if diff_from_sides < min_value:
                min_value = diff_from_sides

        return min_value


if __name__ == "__main__":
    s = Solution()

    A = [3, 1, 2, 4, 3]
    print(s.solution(A))