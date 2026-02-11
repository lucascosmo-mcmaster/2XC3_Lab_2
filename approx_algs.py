def approx1(G): 
    C = set() #start with empty set to store the vertex cover
    adj_cp = {} #create an empty copy of the adjacency list to modify

    #copy each vertex and its neighbors into the copy of the adjacency list
    for vertex in G.adj:
        neighbors = G.adj[vertex]
        adj_cp[vertex] = list(neighbors)
    
    #helper function to check if there are any edges left in a graph
    def has_edges(adj):
        for neighbor in adj.values():
            if len(neighbor) > 0:
                return True
        return False
    
    #while there are still edges in the graph
    while has_edges(adj_cp):
        max_degree = -1 #highest degree seen so far
        v = None # vertex of the highest degree
        
        #find the vertex with the highest degree
        for vertex in adj_cp:
            degree = len(adj_cp[vertex])
            if degree > max_degree:
                max_degree = degree
                v = vertex

        #add the vertex with the highest degree to the vertex cover
        C.add(v)

        #remove all edges incident to the vertex with the highest degree
        for u in adj_cp[v]:
            adj_cp[u].remove(v)
        adj_cp[v] = []
    
    return C