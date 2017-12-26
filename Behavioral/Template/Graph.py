"""
Template Pattern.
Aimed at Avoiding code duplication.
Use template pattern to organize common part of code in a function(The main situation, which would be the used in all situation),
and varying code in other small functions, to support specific situation.
The main func AS TEMPLATE use different small funcs to switch its operation.
"""

# coding: utf-8

# Breadth First Search
def bfs(graph, start, end):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return (True, path)
            # 两个顶点不相连，则跳过
            if current not in graph:
                continue
        visited = visited + graph[current]
    return (False, path)

# Deep First Search
def dfs(graph, start, end):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return (True, path)
            # 两个顶点不相连，则跳过
            if current not in graph:
                continue
        visited = graph[current] + visited
    return (False, path)


def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart', 'Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }

    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))

    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    print('bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found'))
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    print('dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found'))

if __name__ == '__main__':
    main()