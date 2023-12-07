from collections import defaultdict


def recommended_by_all(N, M, recommendations):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for recommendation in recommendations:
        A, B = map(int, recommendation.split())
        graph[A].append(B)

    # Use DFS to find all nodes reachable from the current node
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

    # For each student, get the set of all students they recommend
    recommended_sets = []
    for student in range(1, N + 1):
        visited = set()
        dfs(student, visited)
        recommended_sets.append(visited)

    # Find the intersection of all the recommended sets
    # to get the students who are recommended by everyone
    recommended_by_everyone = set(range(1, N + 1))
    for recommended_set in recommended_sets:
        recommended_by_everyone &= recommended_set

    return len(recommended_by_everyone)


# print(recommended_by_all(3, 3, ["1 2", "2 1", "2 3"]))  # Expected output: 1
print(recommended_by_all(2, 2, ["1 2", "2 1"]))            # Expected output: 2
# print(recommended_by_all(4, 3, ["1 2", "2 3", "3 4"]))    # Expected output: 1
# print(recommended_by_all(4, 4, ["1 2", "2 3", "3 4", "4 1"]))  # Expected output: 4
# print(recommended_by_all(6, 4, ["1 2", "2 1", "3 4", "4 3"]))  # Expected output: 0
# print(recommended_by_all(100, 99, ["1 " + str(i) for i in range(2, 101)]))  # Expected output: 1
