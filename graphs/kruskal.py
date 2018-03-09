#!/bin/python

import sys

TO, WEIGHT = 0, 1

# =============================================================================
def find_partition(partitions, v):
    for idx, partition in enumerate(partitions):
        if v in partition:
            return idx

# =============================================================================
def min_span_tree(n, edges):
    # Complete this function
    graph = [[(0, -1)]] + [[] for _ in range(n)]
    
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))
    # print graph

    partitions = [{v} for v in range(1, n+1)]

    mst = []
    for edge in sorted(edges, key=lambda v: v[2]):
        # print 'from %i to %i w=%i' % (edge[0], edge[1], edge[2])
        partition1 = find_partition(partitions, edge[0])
        partition2 = find_partition(partitions, edge[1])
        # print partition1, partition2
        if partition1 is not None and partition1 != partition2:
            # print 'appending', edge
            mst.append(edge)
            partitions[partition1] = partitions[partition1].union(partitions[partition2])
            partitions[partition2] = {}
            # print partitions
    
    # print mst
    return sum(map(lambda x: x[2], mst))


# =============================================================================
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    edges = []
    for edges_i in xrange(m):
        edges_temp = map(int,raw_input().strip().split(' '))
        edges.append(edges_temp)
    result = min_span_tree(n, edges)
    print result
