# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
from typing import Set


class Solution:
    @staticmethod
    def solution_for_multiple_values(A: list[int]):
        A = sorted(A)
        set_a = set()

        for i in range(len(A)):
            number_i = A[i]

            if len(A) > 0:
                if i == 0:
                    next_i = A[i + 1]
                    if number_i != next_i:
                        set_a.add(number_i)

                elif i == len(A) - 1:
                    before_i = A[i - 1]
                    if number_i != before_i:
                        set_a.add(number_i)

                else:
                    next_i = A[i + 1]
                    before_i = A[i - 1]
                    if number_i != before_i and number_i != next_i:
                        set_a.add(number_i)

        return set_a

    @staticmethod
    def solution(A: list[int]):
        count_dict = {}

        for num in A:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        for key, value in count_dict.items():
            if value % 2 != 0:
                return key

if __name__ == "__main__":
    s = Solution

    A = [9, 3, 9, 3, 9, 7, 9]
    print(s.solution(A))

    # A = [9, 3, 9, 3, 9, 7, 8]
    # print(s.solution_for_multiple_values(A))
