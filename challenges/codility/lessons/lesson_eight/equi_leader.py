# https://app.codility.com/programmers/lessons/8-leader/equi_leader/

class Solution:
    @staticmethod
    def solution(A):
        # Define leader
        element_counts = {}
        for value in A:
            if value in element_counts:
                element_counts[value] += 1
            else:
                element_counts[value] = 1

        leader = max(element_counts, key=element_counts.get)
        leader_count = element_counts[leader]

        if leader_count <= len(A) / 2:
            return 0

        # count equi leaders
        equi_leader_count = 0
        left_leader_count = 0
        for i in range(len(A)):
            if A[i] == leader:
                left_leader_count += 1

            if left_leader_count > (i + 1) / 2 and leader_count - left_leader_count > (len(A) - i - 1) / 2:
                equi_leader_count += 1

        return equi_leader_count


if __name__ == "__main__":
    s = Solution

    A = [3, 4, 3, 3, 3, 2]
    print(s.solution(A))

    print(s.solution([4, 3, 4, 4, 4, 2]))  # Expected output: 2

    print(s.solution([1, 2, 3, 4, 5, 6]))  # Expected output: 0

    print(s.solution([4, 4, 4, 4, 4, 4]))  # Expected output: 5 (every split results in two sequences with the same leader)

    print(s.solution([4, 4, 4, 2, 2, 2]))  # Expected output: 0

    print(s.solution([4, 4, 4, 2, 2, 2, 4, 4, 2, 2]))  # Expected output: 0

    print(s.solution([4, 4, 2, 2, 4, 2, 4, 4, 2, 2, 4, 2]))  # Expected output: 2 (at indices 4 and 10)
