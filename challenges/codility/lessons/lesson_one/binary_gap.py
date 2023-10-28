# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

class Solution:
    @staticmethod
    def solution(N):
        bin_rep = bin(N)[2:]
        gaps = bin_rep.split('1')

        if bin_rep[-1] == '0':
            gaps = gaps[:-1]

        return max([len(gap) for gap in gaps])


if __name__ == "__main__":
    s = Solution()
    print(s.solution(1041))  # Should print 5
    print(s.solution(32))  # Should print 0
