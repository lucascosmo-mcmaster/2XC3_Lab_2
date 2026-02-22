from experiments import plot_graph, cycle_experiment

N = 100
MAX_EDGES = 200
TRIALS = 50

plot_graph(N, MAX_EDGES, TRIALS, "experiment1", cycle_experiment, "Probability of Cycle")