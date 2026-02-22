from graph import create_random_graph, has_cycle, is_connected, MVC
from approx_algs import approx1, approx2, approx3
import matplotlib.pyplot as plt
import csv


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


#experiment for number of edges vs. connected probability
def connected_experiment(n, max_edges, trials):
    num_edges = [] #list to store each tested number of edges
    prob = [] #list to store the probability of a connected graph for each number of edges

    for e in range(max_edges):
        num_connected = 0 #counts how many graphs are connected

        #generate a random graph with n nodes and e edges
        for _ in range(trials):
            G = create_random_graph(n, e)
        
            #check whether or not the graph is connected
            if is_connected(G):
                num_connected += 1
    
        p = num_connected / trials #probability of a graph being connected
        num_edges.append(e)
        prob.append(p)

    return num_edges, prob


#experiment to compare how close each approximation algorithm is to outputting the minimum vertex cover compared to the number of edges
def approx_experiment1(n, max_edges, trials):
    num_edges = list(range(1, max_edges, 5)) #list of edges from 1 to max_edges, stepping by 5
    approx1_ratios = []
    approx2_ratios = []
    approx3_ratios = []

    #loop over each number of edges to generate random graphs
    for m in num_edges:
        mvc_total = 0
        a1_total = 0
        a2_total = 0
        a3_total = 0

        for _ in range(trials):
            G = create_random_graph(n, m)
            mvc_size = len(MVC(G))
            mvc_total += mvc_size

            #run all three approximation algorithms multiple times and take the average
            a1_total += sum(len(approx1(G)) for _ in range(5)) / 5
            a2_total += sum(len(approx2(G)) for _ in range(5)) / 5
            a3_total += sum(len(approx3(G)) for _ in range(5)) / 5

        #compute the average ratio of the approximation size to the MVC size
        approx1_ratios.append(a1_total / mvc_total)
        approx2_ratios.append(a2_total / mvc_total)
        approx3_ratios.append(a3_total / mvc_total)

    return num_edges, approx1_ratios, approx2_ratios, approx3_ratios


#experiment to compare how close each approximation algorithm is to outputting the minimum vertex cover compared to the number of nodes
def approx_experiment2(max_nodes, e, trials):
    num_nodes = list(range(5, max_nodes, 5)) #list of nodes from 1 to max_nodes, stepping by 5
    approx1_ratios = []
    approx2_ratios = []
    approx3_ratios = []

    #loop over each number of nodes to generate random graphs
    for n in num_nodes:
        mvc_total = 0
        a1_total = 0
        a2_total = 0
        a3_total = 0

        for _ in range(trials):
            G = create_random_graph(n, e)
            mvc_size = len(MVC(G))
            mvc_total += mvc_size

            #run all three approximation algorithms multiple times and take the average
            a1_total += sum(len(approx1(G)) for _ in range(5)) / 5
            a2_total += sum(len(approx2(G)) for _ in range(5)) / 5
            a3_total += sum(len(approx3(G)) for _ in range(5)) / 5

        #compute the average ratio of the approximation size to the MVC size
        approx1_ratios.append(a1_total / mvc_total)
        approx2_ratios.append(a2_total / mvc_total)
        approx3_ratios.append(a3_total / mvc_total)

    return num_nodes, approx1_ratios, approx2_ratios, approx3_ratios


#plots the graph of an experiment versus nodes and saves it
def plot_node_graph(max_nodes, e, trials, filename):
    e, p1, p2, p3 = approx_experiment2(max_nodes, e, trials)
    plt.plot(e, p1, label="approx1")
    plt.plot(e, p2, label="approx2")
    plt.plot(e, p3, label="approx3")
    save_results(e, p1, filename + "_approx1")
    save_results(e, p2, filename + "_approx2")
    save_results(e, p3, filename + "_approx3")
    plt.legend()
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Ratio to MVC")
    plt.savefig("graphs/" + filename + ".png", dpi=300, bbox_inches="tight")
    plt.show()


#plots the graph of an experiment versus edges and saves it
def plot_edge_graph(n, max_edges, trials, filename, func, yla):
    if func == approx_experiment1: 
        e, p1, p2, p3 = func(n, max_edges, trials)
        plt.plot(e, p1, label="approx1")
        plt.plot(e, p2, label="approx2")
        plt.plot(e, p3, label="approx3")
        save_results(e, p1, filename + "_approx1")
        save_results(e, p2, filename + "_approx2")
        save_results(e, p3, filename + "_approx3")
        plt.legend()
    else:
        e, p = func(n, max_edges, trials)
        plt.plot(e, p)
        save_results(e, p, filename)

    plt.xlabel("Number of Edges")
    plt.ylabel(yla)
    plt.savefig("graphs/" + filename + ".png", dpi=300, bbox_inches="tight")
    plt.show()


#saves the results of an experiment
def save_results(num_edges, prob, filename):
    with open("csv/" + filename + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["edges", "probability"])
        for e, p in zip(num_edges, prob):
            writer.writerow([e, p])