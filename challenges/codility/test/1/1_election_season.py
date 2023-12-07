from collections import defaultdict


def solution(X, Y, C):
    N = X
    M = Y
    recommendations = C

    graph = defaultdict(list)
    for recommendation in recommendations:
        A, B = map(int, recommendation.split())
        graph[A].append(B)

    # now we can use DFS to find all nodes
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

    # to get the set of all students they recommend for each student
    recommended_sets = []
    for student in range(1, N + 1):
        visited = set()
        dfs(student, visited)
        recommended_sets.append(visited)

    recommended_by_everyone = set(range(1, N + 1))
    for recommended_set in recommended_sets:
        recommended_by_everyone &= recommended_set

    return len(recommended_by_everyone)


X = 3
Y = 3
C = ["1 2", "2 1", "2 3"]

X = 4
Y = 4
C = ["1 2", "2 3", "3 4", "4 1"]

# X = 6
# Y = 5
# C = ["1 2", "2 4", "4 5", "5 6", "3 1"]

print(solution(X, Y, C))
