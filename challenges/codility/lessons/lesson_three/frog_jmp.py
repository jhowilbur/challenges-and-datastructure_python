# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
import math


class Solution:
    @staticmethod
    def solution(X, Y, D):
        # long approach
        # count = 0
        # while X < Y:
        #     X += D
        #     count += 1
        # return count

        # math approach
        distance_to_cover = Y - X
        jumps = math.ceil(distance_to_cover/D)
        return jumps


if __name__ == "__main__":
    s = Solution()

    X = 10
    Y = 85
    D = 30
    print(s.solution(X, Y, D))
