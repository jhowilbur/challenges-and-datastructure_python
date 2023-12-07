from collections import defaultdict


def solution(X, Y, C):
    N = X
    recommendations = C

    graph = defaultdict(list)
    for recommendation in recommendations:
        A, B = map(int, recommendation.split())
        graph[A].append(B)

    def dfs(node):
        visited = set()
        stack = [node]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            stack.extend(neighbor for neighbor in graph[current] if neighbor not in visited)
        return visited

    common_students = set(range(1, N + 1))
    for student in range(1, N + 1):
        common_students.intersection_update(dfs(student))
        if not common_students:
            break

    return len(common_students)


X = 3
Y = 3
C = ["1 2", "2 1", "2 3"]

X = 4
Y = 4
C = ["1 2", "2 3", "3 4", "4 1"]

X = 6
Y = 5
C = ["1 2", "2 4", "4 5", "5 6", "3 1"]

print(solution(X, Y, C))
