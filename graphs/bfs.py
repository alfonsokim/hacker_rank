#!/bin/python

import sys
from collections import deque


# =============================================================================
def bfs(n, m, graph_edges, s):
    # Complete this function
    EDGE_LEN = 6
    graph = [None] + [[] for _ in range(n)]
    colors = [None] + ['W' for _ in range(n)]
    for vertex, edge in graph_edges:
        graph[vertex].append(edge)
        graph[edge].append(vertex)
    distances = [None] + [0] * n
    queue = deque([s])
    colors[s] = 'G'
    while len(queue) > 0:
        u = queue.popleft()
        edges = graph[u]
        for v in edges:
            if colors[v] == 'W':
                colors[v] = 'G'
                distances[v] = distances[u] + EDGE_LEN
                queue.append(v)
        colors[u] = 'B'
    return [distances[v] if colors[v] == 'B' else -1 for v in range(1, n+1) if v != s]


# =============================================================================
if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, m = raw_input().strip().split(' ')
        n, m = [int(n), int(m)]
        edges = []
        for edges_i in xrange(m):
            edges_temp = map(int,raw_input().strip().split(' '))
            edges.append(edges_temp)
        s = int(raw_input().strip())
        result = bfs(n, m, edges, s)
        print " ".join(map(str, result))
