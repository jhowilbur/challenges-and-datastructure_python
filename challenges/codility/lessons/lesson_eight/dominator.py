# https://app.codility.com/programmers/lessons/8-leader/dominator/

class Solution:
    @staticmethod
    def solution(A):

        if not A: # if empty
            return -1

        stack = []
        for value in A:
            if stack and stack[-1] != value:
                stack.pop()
            else:
                stack.append(value)

        if not stack: # if empty
            return -1

        candidate = stack[0]
        count = A.count(candidate)

        if count <= len(A) / 2:
            return -1

        return A.index(candidate)

        # Another way but need to fix
        # A = sorted(A)
        #
        # dictionary = {}
        # for value in A:
        #     if value in dictionary:
        #         dictionary[value] += 1
        #     else:
        #         dictionary[value] = 1
        #
        # key_of_maximum_index_repeated = max(dictionary, key=dictionary.get)
        # if dictionary[key_of_maximum_index_repeated] < N:
        #     return -1
        #
        # return 0


if __name__ == "__main__":
    s = Solution()

    # A = [3, 4, 3, 2, 3, -1, 3, 3]
    # A = [7, 7, 7, 3, 7, 3, 3, 3, 7]
    A = [7, 7, 7, 3, 7, 3, 3, 3, 3]
    print(s.solution(A))