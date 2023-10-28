# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

class Solution:
    @staticmethod
    def solution(A):
        # wrong way
        # A = sorted(A)
        # B = range(A[1], A[-1])
        # for value in B:
        #     if value not in A:
        #         return value
        # return 0

        # right way Gauss
        N = len(A) + 1
        total = (N * (N+1)) // 2

        for value in A:
            total -= value

        return total


if __name__ == "__main__":
    s = Solution()

    A = [2, 3, 1, 5]
    print(s.solution(A))