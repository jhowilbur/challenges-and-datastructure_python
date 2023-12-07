class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootY] += 1

def solution(X, Y, C):
    N = X

    dsu = UnionFind(N + 1) # 1-based indexing

    for recommendation in C:
        A, B = map(int, recommendation.split())
        dsu.union(A, B)

    # Finding groups (sets of students recommended by someone)
    groups = {}
    for student in range(1, N + 1):
        root = dsu.find(student)
        if root not in groups:
            groups[root] = set()
        groups[root].add(student)

    # Finding the intersection of all groups
    common_students = set(range(1, N + 1))
    for group in groups.values():
        common_students &= group

    return len(common_students)

print(solution(3, 3, ['1 2', '2 1', '2 3']))  # Expected output: 1
# print(solution(3, 3, ["1 2", "2 1", "2 3"]))  # Expected output: 1
# print(solution(2, 2, ["1 2", "2 1"]))            # Expected output: 2
# print(solution(4, 3, ["1 2", "2 3", "3 4"]))    # Expected output: 1
# print(solution(4, 4, ["1 2", "2 3", "3 4", "4 1"]))  # Expected output: 4
# print(solution(6, 4, ["1 2", "2 1", "3 4", "4 3"]))  # Expected output: 0
# print(solution(100, 99, ["1 " + str(i) for i in range(2, 101)]))  # Expected output: 1