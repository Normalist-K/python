import bisect

import sys
sys.setrecursionlimit(1000000)

# sys.stdin = open("05.txt", "r")

def DFS(graph, visited, root):
    visited.append(root)
    for node in graph[root]:
        if node not in visited:
            DFS(graph, visited, node)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        bisect.insort_left(graph[u], v)
        bisect.insort_left(graph[v], u)

    visited = []
    DFS(graph, visited, 0)
    print(*visited)
    
        

    