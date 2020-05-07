
'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

'''





import collections
class Solution(object):
    def criticalConnections(self, n, connections):
        
#         make adjacency graph
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph
        
        graph = makeGraph(connections)
#         sort connections and make tuples 
        for x in connections:
            x = x.sort()
        connections.sort(key = lambda x : x[0])
        connections = set([tuple(x) for x in connections])
#         create rank array
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue 
                back_depth = dfs(neighbor, depth + 1)
#                 if rank is less than or equal to depth you're at a cycle, discard edge
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
            
        dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)
                
                    
            