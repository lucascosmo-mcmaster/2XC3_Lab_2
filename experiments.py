from graph import create_random_graph, has_cycle
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


def plot_graph(n, max_edges, trials, filename):
    e, p = cycle_experiment(n, max_edges, trials)
    plt.plot(e, p)
    plt.xlabel("Number of Edges")
    plt.ylabel("Probability of Cycle")
    plt.savefig("graphs/" + filename + ".png", dpi=300, bbox_inches="tight")
    save_results(e, p, filename)
    plt.show()

#saves the results of an experiment
def save_results(num_edges, prob, filename):
    with open("csv/" + filename + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["edges", "probability"])
        for e, p in zip(num_edges, prob):
            writer.writerow([e, p])