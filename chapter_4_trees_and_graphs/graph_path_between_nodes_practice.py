def is_path(graph, start, end, visited=None):
    if not visited:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end:
                return True
            if is_path(graph, node, end, visited):
                return True
    return False
