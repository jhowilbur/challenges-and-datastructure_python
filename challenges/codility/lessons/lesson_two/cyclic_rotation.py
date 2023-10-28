# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

class Solution:
    @staticmethod
    def solution(A: list[int], K: int) -> list[int]:

        if not A or len(A) == 1:
            return A

        K %= len(A)  # validate K size in comparison with A (but could be not necessary

        while K != 0:
            A.insert(0, A.pop())
            K -= 1
        return A


if __name__ == "__main__":
    s = Solution

    A = [3, 8, 9, 7, 6]
    K = 3
    print(s.solution(A, K))

    A = [0, 0, 0]
    K = 1
    print(s.solution(A, K))

    A = [1, 2, 3, 4]
    K = 4
    print(s.solution(A, K))
