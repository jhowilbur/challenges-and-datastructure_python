
class Graph:
    @staticmethod
    def depth_first_print(graph):
        for key, value in graph.items():
            print(f'key: {key} - value: {value}')


# example of use
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }
    Graph.depth_first_print(graph)
