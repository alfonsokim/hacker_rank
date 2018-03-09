#!/bin/python

import sys
import heapq

# =============================================================================
def prims(n, graph_edges, start):
    # Complete this function
    path_weight = 0
    heap, connected = [], set([start])
    graph = [None] + [{} for _ in range(n)]

    for edge in edges:
        graph[edge[0]][edge[1]] = min(edge[2], graph[edge[0]].get(edge[1], float('inf')))
        graph[edge[1]][edge[0]] = min(edge[2], graph[edge[1]].get(edge[0], float('inf')))
    print graph

    for edge, weight in graph[start].iteritems():
        heapq.heappush(heap, (edge, weight))
    # print heap

    while len(connected) < n:
        edge, weight = heapq.heappop(heap)
        if edge not in connected:
            connected.add(edge)
            path_weight += weight
            for next_edge, next_weight in graph[edge].iteritems():
                heapq.heappush(heap, (next_edge, next_weight))

    return path_weight


# =============================================================================
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    edges = []
    for edges_i in xrange(m):
        edges_temp = map(int,raw_input().strip().split(' '))
        edges.append(edges_temp)
    start = int(raw_input().strip())
    result = prims(n, edges, start)
    print result
