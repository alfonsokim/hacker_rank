#!/bin/python

import sys
import heapq

INFINITE = float('inf')

# =============================================================================
def dijkstra(graph_edges, s):
    # print graph_edges, s
    graph = [None] + [[] for _ in range(len(graph_edges))]
    queue = []
    distances = [None] + [INFINITE] * len(graph_edges)
    visited = set()
    for g_edge in graph_edges:
        graph[g_edge[0]].append((g_edge[1], g_edge[2]))
        graph[g_edge[1]].append((g_edge[0], g_edge[2]))
        heapq.heappush(queue, (g_edge[2], (g_edge[0], g_edge[1])))
        heapq.heappush(queue, (g_edge[2], (g_edge[1], g_edge[0])))
    distances[s] = 0
    # print graph
    # print queue
    # print distances
    while len(queue) > 0:
        w, (u, uu) = heapq.heappop(queue)
        # print u, w
        # path.append(u)
        # if u in visited:
        #     continue
        # visited.add(u)
        for v, w_v in graph[u]:
            # print 'u:%i, v:%s' % (u, v)
            if distances[v] > (distances[u] + w_v):
                distances[v] = (distances[u] + w_v)
    # print range(1, len(graph) + 1)
    return [
        distances[e]
        for e in range(1, len(graph_edges) + 1) 
        if e != s and distances[e] < INFINITE
    ]


# =============================================================================
t = int(raw_input().strip())
line = 1
line_str = ''
for a0 in xrange(t):
    line_str = raw_input()
    n, m = line_str.strip().split(' ')
    line += 1
    n, m = [int(n),int(m)]
    edges = []
    for a1 in xrange(m):
        line_str = raw_input()
        x, y, r = line_str.strip().split(' ')
        line += 1
        x, y, r = int(x), int(y), int(r)
        edges.append((x, y, r))
    line_str = raw_input()
    s = int(line_str.strip())
    line += 1
    print ' '.join(map(str, dijkstra(edges, s)))
