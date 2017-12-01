An implementation of the Ford-Fulkerson and Edmonds-Karp algorithms for finding the maximum flow of a flow network. Includes 3 different implementations of a graph.

MatrixGraph implements graphs using an adjacency matrix method, G[i][j] is the capacity of the i-j edge in the graph. 

ArrayGraph implements graphs as an array of association lists. G[i] is a list of all the (node, cost) pairs of the neighbors of i and the capacities of the edges between them. This tends to yield the fastest running times on all but the densest graphs. 

NaiveGraph implements graphs as an association lists of association lists. Each node is associated with a list of (node, cost) pairs as in the implementation of ArrayGraph.

Use the compile.sh file to compile, and run the ./flow <FILENAME> binary created. Documentation on the format of the graph files accepted can be found in main.ml, and examples can be found in the tests folder. 

The -g option accepts one of {matrix, array, naive} to select the graph type.
The -s option accepts one of {dfs, bfs} and chooses whether the Ford-Fulkerson algorithm uses a breadth-first or depth-first search to find an augmenting path at each iteration. Using a breadth-first search makes the algorithm equivalent to Edmonds-Karp. The traditional Ford-Fulkerson using a depth-first search performs better on graphs that have low edge capacity to size ratios, while Edmonds-Karp performs better on graphs with very high edge capacities. 



