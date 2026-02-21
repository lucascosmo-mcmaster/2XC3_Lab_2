from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


def walk_back(path_back, start):
    path = deque()
    current = start
    path.appendleft(current)
    while path_back[current] != current:
        path.appendleft(path_back[current])
        current = path_back[current]
    return list(path)


#Breadth First Search variant that returns the list of nodes in the path from node1 to node2
def BFS2(G, node1, node2):
    #base case where node1 and node2 are the same
    if node1 == node2:
        return [node1]
    
    Q = deque([node1]) #initialize queue with starting node
    path = {} #dictionary to store each node's predecessor

    #initialize all nodes as unvisited
    for node in G.adj: 
        if node != node1:
            path[node] = None
    
    path[node1] = node1 #the path from node1 points to itself
    
    #perform BFS until all nodes have been visited
    while len(Q) != 0: 
        current_node = Q.popleft() #remove the next node from the queue
        for node in G.adj[current_node]: #visit all neighbors of the current node
            if path[node] == None: #if a neighbor hasn't been visited yet, add it to the queue
                Q.append(node) 
                path[node] = current_node #record the path
                if node == node2: #if the target node is found, walk back to find the path again
                    return walk_back(path, node)
    return {}


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


#Depth First Search variant that returns the list of nodes in the path from node1 to node2
def DFS2 (G, node1, node2):
    S = [node1] #initialize stack with starting node
    marked = {} #dictionary to track which nodes have been visited
    path = {} #dictionary to store each node's predecessor

    #initialize all nodes as unvisited/without a path
    for node in G.adj:
        marked[node] = False
        path[node] = None
    
    marked[node1] = True #the starting node is marked
    path[node1] = node1 #the path from node1 points to itself


    #perform DFS until all nodes have been visited
    while len(S) != 0:
        current_node = S.pop() #pop the current node from the stack
        for node in G.adj[current_node]: #visit all neighbors of the current node
            if not marked[node]: #if a node hasn't been marked yet, add it to the stack
                S.append(node)
                marked[node] = True #mark the node as visited
                path[node] = current_node #record the path
                if node == node2: #if the target node is found, walk back to find the path again
                    return walk_back(path, node)
    return {}


#Use the methods below to determine minimum vertex covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover