from experiments import plot_graph, approx_experiment1

N = 8
MAX_EDGES = 30
TRIALS = 1000

plot_graph(N, MAX_EDGES, TRIALS, "approx_experiment1", approx_experiment1, "Average Ratio to MVC")