import random


#helper function to copy each vertex and its neighbors into the copy of the adjacency list
def copy_adj(G, adj_cp):
    for vertex in G.adj:
        neighbors = G.adj[vertex]
        adj_cp[vertex] = list(neighbors)


#helper function to check if there are any edges left in a graph
def has_edges(adj):
    for neighbor in adj.values():
        if len(neighbor) > 0:
            return True
    return False


def approx1(G): 
    C = set() #start with empty set to store the vertex cover
    adj_cp = {} #create an empty copy of the adjacency list to modify
    copy_adj(G, adj_cp) #copy the adjacency list into adj_cp
    
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


def approx2(G):
    C = set() #start with empty set to store the vertex cover
    adj_cp = {} #create an empty copy of the adjacency list to modify
    copy_adj(G, adj_cp) #copy the adjacency list into adj_cp

    #while there are still edges in the graph
    while has_edges(adj_cp):
        vertices = [] #list of vertices not in the vertex cover
        
        for v in adj_cp:
            if v not in C:
                vertices.append(v)
        
        v = random.choice(vertices) #choose a random vertex from the list of vertices not in the vertex cover
        C.add(v) #add the random vertex to the vertex cover
    
    return C
    

def approx3(G):
    C = set() #start with empty set to store the vertex cover
    adj_cp = {} #create an empty copy of the adjacency list to modify
    copy_adj(G, adj_cp) #copy the adjacency list into adj_cp

    #while there are still edges in the graph
    while has_edges(adj_cp):
        edges = [] #list of edges not in the vertex cover
        u = None #first vertex of the selected edge
        v = None #second vertex of the selected edge

        for (u, v) in adj_cp.items():
            for neighbor in v:
                edges.append((u, neighbor))
        
        (u, v) = random.choice(edges) #choose a random edge from the list of edges not in the vertex cover
        C.add(u) #add the first vertex of the random edge to the vertex cover
        C.add(v) #add the second vertex of the random edge to the vertex cover

        #remove all edges incident to the first vertex of the random edge
        for neighbor in adj_cp[u]: 
            adj_cp[neighbor].remove(u)
        adj_cp[u] = []

        #remove all edges incident to the second vertex of the random edge
        for neighbor in adj_cp[v]: 
            adj_cp[neighbor].remove(v)
        adj_cp[v] = []
        
    return C