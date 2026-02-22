from experiments import plot_edge_graph, connected_experiment

N = 100
MAX_EDGES = 500
TRIALS = 50

plot_edge_graph(N, MAX_EDGES, TRIALS, "experiment2", connected_experiment, "Probability of Connected Graph")