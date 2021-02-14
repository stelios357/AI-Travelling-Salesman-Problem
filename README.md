
Traveling Salesman Problem
Link For Demo:
https://drive.google.com/drive/u/1/folders/19NOrc1q_jbhVSkb352mVFxE88GFzWkNt 


1.	Introduction

Traveling salesman problem is a combinatorial optimization task of finding a tour of n cities where the objective is to find a tour that visits each vertex exactly once and returns to the starting point and whose total length is as small as possible.TSP belongs to the class of N-P hard problems in combinatorial optimization.
Traveling Salesman Problem can be viewed as an undirected weighted graph problem, where the cities can be viewed as the graph's vertices, paths as the graph's edges, and the path's distance is the edge's weight.
Mathematically it can be explained as follows:
Let G=(V, E) be a complete undirected graph with vertices V, |V|= n , and the edges E and let
𝑑𝑖𝑗be the length of edge (i, j).
The most straightforward approach to solve this problem is by using brute force search to find all the possible permutations and then selecting the shortest tour. It is impractical as the number of
permutations is (n−1)! Which means that in terms of time complexity, we will be looking at O(𝑛!) which is highly undesirable.
TSP can also be solved by using Dynamic programming by having a recursive relation in terms of sub-problems and even though this method is slightly better in terms of time complexity than brute force, its time complexity is still exponential in nature.
In fact, TSP is a famous NP hard problem and thus there is no polynomial time solution for this problem. Thus all the research on this problem has been made by making efforts on finding approximating algorithms. Approximation algorithms are hardly any longer than an optimal solution and their time complexity is a lower order polynomial function.
The other caveat in using approximation algorithms is that they only work if the problem satisfies triangle inequality.

TRIANGLE INEQUALITY: The triangle inequality states that the sum of the lengths of any two sides of a triangle is greater than the length of the remaining side.
When the cost function satisfies the triangle inequality, we can make sure that the approximate algorithm for TSP will return a tour whose cost is never more than twice the cost of an optimal tour.

2.	Minimum Spanning Tree

Given an undirected graph G=(V, E) with arc lengths 𝑑𝑖𝑗,a spanning tree is a subgraph of G such that it is a tree and it touches all the nodes of the graph G. A minimum spanning tree does not contain any cycles which means that for n nodes it contains n-1 arcs.The minimum
spanning tree problem is to find a spanning tree with the minimum possible total edge weight.
The algorithms for finding the Minimum Spanning Tree use the concept of greedy algorithm to implement the minimum spanning tree:

2.1	Kruskal’s Algorithm

Kruskal’s Algorithm builds the spanning tree by adding edges having the least weight one by one into the growing spanning tree iteratively.
Steps:
1.	Sort all the edges in increasing order of their weight.
2.	Pick the smallest edge and include it if it does not form a cycle with the currently formed spanning tree. If it forms a cycle, then discard it.
3.	Repeat step 2 until there are (V-1) edges in the spanning tree.


Algorithm:
KRUSKAL(G):
A = ∅

For each vertex v ∈ V:

 MAKE-SET(v)
 
For each edge (u, v) ∈ E ordered by increasing order by weight(u, v):

 if FIND-SET(u) ≠ FIND-SET(v):
 
 A = A ∪ {(u, v)}
 
 UNION(u, v)
 
return A


Graph Depiction: Suppose we have the following graph:
![image](https://user-images.githubusercontent.com/48243821/107869697-ca2d4600-6eb6-11eb-93e2-6b9e98dceaa3.png)
 
Then according to Kruskal’s algorithm, the steps followed will be:
![image](https://user-images.githubusercontent.com/48243821/107869698-cdc0cd00-6eb6-11eb-9b53-43a9008e50e3.png)


Time Complexity: The overall time complexity to implement Kruskal’s algorithm is O(ElogE) as sorting of edges takes O(ELogE) time and after sorting, we iterate through all edges and check whether a cycle is being formed or not which also takes O(ElogV) time.


2.2	Prim’s Algorithm

Prim’s algorithm starts with an empty spanning tree. Here we grow the spanning tree from an arbitrary starting vertex. Then we keep on adding vertices to the growing spanning tree.
Steps:

1.	Keep 2 separate sets of vertices. One contains the vertices that are present in the growing spanning tree called the fringe and the other contains the vertices that are not covered yet.
 
2.	Select that vertex that is connected to the fringe but is not in the set containing vertices of the spanning tree and has the cheapest cost and add it to the set containing the vertices of the spanning tree.
3.	Check for cycles. To do that, mark the nodes which have been already selected and insert only those nodes that are not in the fringe.

Algorithm:
#Suppose we have 2 sets of vertices, U and V-U where U contains the visited #vertices. T is the
set of edges in the MST. We move the vertices from V-U to U #one by one
PRIMS(V)
T = ∅;

U = { 1 };

while (U ≠ V)

 let (u, v) be the least cost edge such that u ∈ U and v ∈ V - U;
 
 T = T ∪ {(u, v)}
 
 U = U ∪ {v}
 


Graph Depiction: Suppose we have the following graph: -

![image](https://user-images.githubusercontent.com/48243821/107869700-d2858100-6eb6-11eb-92b8-432786e9f401.png)
![image](https://user-images.githubusercontent.com/48243821/107869701-d74a3500-6eb6-11eb-8210-48b0252da67a.png)


Time Complexity: The time complexity of the Prim’s Algorithm is O(ElogV) as well
Thus, any of the above two algorithms can be used to implement MST as both the algorithms have the same time complexity.

Now that we have made the MST, we need to figure out how to get the solution of TSP from it. One method is to apply DFS or Preorder traversal on the obtained MST, note down the nodes that we obtain from DFS and append the source node at the end. This will give us the path that should be taken to solve TSP. However, through this method, we only get the path and not the minimum weight path. This method is simply an estimation for solving this problem and as such, does not give us the correct output in every case. To get better results we can make use of the A* algorithm as stated in the next section.

3.	MST based heuristic to solve Traveling Salesman Problem
Steps:
1.	Choose a vertex to be the starting and ending point for the salesman.
2.	Construct a minimum spanning tree for the given graph.
3.	Traverse all the vertices by a tree traversal algo(A* in our problem) of your choice, record the sequence of vertices(both visited and unvisited) and in the end, add the starting vertex as well..

Time Complexity: The time complexity of the solution of travelling salesman problem with help of MST heuristic using A* Algorithm is O(E*(V^2))
Complexity of graph matrix method = V^2 Complexity of prim’s algorithm = E*(V^2) Complexity of A* algorithm = E*(V^2) E*(V^2) + V^2 + E*log(V) = O(V^2)


