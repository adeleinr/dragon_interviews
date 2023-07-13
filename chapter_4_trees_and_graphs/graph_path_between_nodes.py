import unittest


def is_route(graph, start, end, visited=None):
    if not visited:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end:
                return True
            if is_route(graph, node, end, visited):
                return True
    return False


class TestGraph(unittest.TestCase):
    graph = {
        "A": ["B", "C"],
        "B": [],
        "C": ["D", "E"],
        "D": [],
        "E": [],
        "F": ["G"],
    }
    find_route_testcases = [
        ("A", "B", True),
        ("A", "G", False),
    ]

    def test_find_route(self):
        for start, end, expected in self.find_route_testcases:
            assert (is_route(self.graph, start, end) == expected)


unittest.main()