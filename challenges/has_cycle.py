def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = set()

    def dfs(node: str, parent: str) -> bool:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True

    return False
