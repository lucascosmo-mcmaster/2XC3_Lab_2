import matplotlib.pyplot as plt
from graph import create_random_graph, has_cycle


#experiment for number of edges vs. cycle probability
def cycle_experiment(n, max_edges, trials):
    num_edges = [] #list to store each tested number of edges
    prob = [] #list to store the probability of a cycle for each number of edges

    for e in range(max_edges + 1):
        num_cycles = 0 #counts how many graphs contain a cycle

        #generate a random graph with n nodes and e edges
        for _ in range(trials):
            G = create_random_graph(n, e)
        
        #check whether or not the graph contains a cycle
        if has_cycle(G):
            num_cycles += 1
    
    p = num_cycles / trials #probability of a cycle occurring
    num_edges.append(e)
    prob.append(p)

    return num_edges, prob
