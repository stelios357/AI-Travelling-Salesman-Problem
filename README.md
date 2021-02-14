
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

4.	Current state of the art methods which show (significant) improvement over MST heuristic. Genetic Algorithm (GA)
A.	Genetic Algorithm (GA)
Genetic programming [6-8] is an automated method for solving problems. Specifically, genetic programming progressively breeds a population of computer programs over a series of generations. Genetic programming is a probabilistic algorithm that searches the space of compositions of the available functions and terminals under the guidance of a fitness measure. Genetic programming starts with a primordial ooze of thousands of randomly created computer programs and uses the Darwinian principle of natural selection, recombination (crossover), mutation, gene duplication, gene deletion, and certain mechanisms of developmental biology to breed an improved population over a series of many generations.
Genetic programming breeds computer programs to solve problems by executing the following three steps:
1)	Generate an initial population of compositions of the functions and terminals of the problem.
2)	Iteratively perform the following substeps (referred to herein as a generation) on the population of programs until the termination criterion has been satisfied:
a)	Execute each program in the population and assign a fitness value using the fitness measure.
b)	Create a new population of programs by applying the following operations. The operations are applied to program selected from the population with a probability based on fitness (with reselection allowed).

Reproduction: Copy the selected program to the new population. The reproduction process can be subdi-vided into two subprocesses: Fitness Evaluation and Selection. The fitness function is what drives the evolutionary process and its purpose is to determine how well a string (individual) solves the problem, al-lowing for the assessment of the relative performance of each population member.
Crossover: Create a new offspring program for the new population by recombining randomly chosen parts of two selected programs. Reproduction may proceed in three steps as follows: 1) two newly re-produced strings are randomly selected from a Mating Pool; 2) a number of crossover positions along each string are uniformly selected at random and 3) two new strings are created and copied to the next generation by swapping string characters between the crossover positions defined before.
Mutation: Create one new offspring program for the new population by randomly mutating a randomly chosen part of the selected program.
Architecture-altering operations: Select an architecture-altering operation from the available repertoire of such operations and create one new offspring pro-gram for the new population by applying the selected architecture-altering operation to the selected program.
3)	Designate the individual program that is identified by result designation (e.g., the best-so far individual) as the result of the run of genetic programming. This result may be a solution (or an approximate solution) to the problem. The specification of the designed GA technique depends on used database; population size will selected from 100 and increasing monotonically while find solution, crossover rate around 0.5 – 0.7, Mutation rate in range 0.05 – 0.09, Chromosome Length depends on number of cities in database.
Figure 1 shows the flowchart of the parameter optimizing procedure using GA. For details of genetic operators and each block in the flowchart, one may consult literature [9].

	
 






Fig.1. The optimization flowchart of GA technique.

B.	Ant Colony Optimization
Ant colony optimization (ACO) is one of the most popular meta-heuristics used for combinatorial optimization (CO) in which an optimal solution is sought over a discrete search space. The well-known CO's example is the traveling salesman problem (TSP) [10] where the search-space of candidate solutions grows more than exponentially as the size of the problem increase, which makes an exhaustive search for optimal solution infeasible.
The first ACO algorithm, Ant System (AS), has been introduced by Marco Dorigo in the early 1990‟s [11-13], and since then several improvement of the AS have been devised (Gambardella & Dorigo, 1995[14]; Stützle & Hoos, 1997[15]). The ACO algorithm is based on a computational paradigm inspired by real ant colonies and the way they function. The underlying idea was to use several constructive computational agents (simulating real ants) [16]. Ant's behavior is governed by the goal of colony survival rather than being focused on  the  survival  of  individuals.  The behavior that provided the inspiration for ACO is the ants‟ foraging behavior (see figure 2), and in particular, how ants  can find shortest paths between food sources and their nest. When searching for food, ants initially explore the area surrounding their nest in a random manner. While moving, ants leave a chemical pheromone  trail on the ground.  Ants  can smell pheromone.
 
Fig. 2 Ants use pheromone as indirect communication to build best tour
















Fig. 3. The optimization flowchart of ACO
 
When choosing their way, they tend to choose, in probability, paths marked by  strong  pheromone concentrations. As soon as an ant finds a food source, it evaluates the quantity and the quality of the food and carries some of it back to the nest. During the return trip, the quantity of pheromone that an ant leaves on the ground  may  depend on the quantity and quality of the food. The pheromone trails will guide other ants to the food source. It has been shown in [17] that the indirect communication between the ants via pheromone trails enables them to find shortest paths between their nest and food sources. The flowchart of ACO is shown in figure (3)

C.	Particle Swarm Optimization
PSO is a population based optimization method first proposed by Eberhart and Colleagues [18-20]. Some of the attractive features of PSO include the ease of implementation and the fact that no gradient information is required. It can be used to solve a wide array of different optimization problems. Like evolutionary algorithms, PSO technique conducts search using a population of particles, corresponding to individuals. Each particle represents a candidate solution to the problem at hand. In a PSO system, particles change their positions by flying around in a multidimensional search space until computational limitations are exceeded. Concept of modification of a searching point by PSO is shown in Figure 4.

 
Fig. 4 Concept of modification of a searching point by PSO

The PSO technique is an evolutionary computation technique, but it differs from other well-known evolutionary computation algorithms such as the genetic algorithms. Although a population is used for searching the search space, there are no operators inspired by the human DNA procedures applied on the population. Instead, in PSO, the population dynamics simulates a „bird flock‟s‟ behaviour, where social sharing of information takes place and individuals can profit from the discoveries and previous experience of all the other companions during the search for food. Thus, each companion, called particle, in the population, which is called swarm, is assumed to „fly‟ over the search space in order to find promising regions of the landscape. For example, in the minimization case, such regions possess lower function values than other, visited previously. In this context, each particle is treated as a point in a d-dimensional space, which adjusts its own „flying‟ according to its flying experience as well as the flying experience of other particles (companions). In PSO, a particle is defined as a moving point in hyperspace. For each particle, at the current time step, a record is kept of the position, velocity, and the best position found in the search space so far.
The assumption is a basic concept of PSO. In the PSO algorithm, instead of using evolutionary operators such as mutation and crossover, to manipulate algorithms, for a variable optimization problem, a flock of particles are put into the d-dimensional search space with randomly chosen velocities and positions knowing their best values so far (Pbest) and the position in the d-dimensional space.
The velocity of each particle, adjusted according to its own flying experience and the other particle‟s flying experience. For example, the i-th particle is represented as xi = (xi,1 ,xi,2 ,…, xi,d) in the d-dimensional space. The best previous position of the i-th particle is recorded and represented as:
Pbesti = (Pbesti,1, Pbesti,2 ,..., Pbest i,d) (1)
The index of best particle among all of the particles in the group is gbestd. The velocity for particle i is represented as vi = (vi,1 ,vi,2 ,…, vi,d). The modified velocity and position of each particle can be calculated using the current velocity and the distance from Pbesti, d to gbestd as shown in the following formulas [16-18]:
 

D.	Bacterial Foraging Algorithm (BFA)
Recently, bacterial foraging algorithm (BFA) has emerged as a powerful technique for the solving optimization problems. BFA mimics the foraging strategy of E. coli bacteria which try to maximize the energy intake per unit time.
 
From the very early days it has drawn attention of researchers due to its effectiveness in the optimization domain. So as  to improve its performance, a large number of modifications have already been undertaken. The  bacterial foraging system consists of four principal mechanisms, namely chemotaxis, swarming, reproduction and elimination-dispersal. A brief description of each of these processes along with the pseudo-code of the complete algorithm is described below.
Chemotaxis: This process simulates the movement of an E.coli cell through swimming and tumbling via flagella. Biologically an E.coli bacterium can move in two different  ways. It can swim for a period of time in the same direction  or it may tumble, and alternate between these two modes of operation for the entire lifetime. Suppose  
represents ith bacterium at jth chemotactic, kth reproductive and lth elimination-dispersal step. C(i) is the size of  the step
taken in the random direction specified by the tumble (run length unit). Then in computational chemotaxis the movement of the bacterium may be represented by.


 

Where Δ indicates a vector in the random direction whose elements lie in [-1, 1].
 
(3)
 
Swarming: An interesting group behavior has been observed where a group of E.coli cells arrange themselves in a traveling ring by moving up the nutrient gradient when placed amidst a semisolid matrix with a single nutrient chemoeffecter. The cells, when stimulated by a high level of succinate, release an attractant aspertate, which helps them to aggregate into groups and thus move as concentric patterns of swarms with high bacterial density. The cell-to-cell signaling in E. coli swarm may be represented by the following function.
where	is the objective function value to be added to the actual objective function (to be minimized) to present a time varying objective function, S is the total number of bacteria, p is the number of variables to be optimized, which are present in each bacterium and   is a point in the p dimensional search domain.
Reproduction: The least healthy bacteria eventually die while each of the healthier bacteria (those yielding lower
value of the objective function) asexually split into two bacteria, which are then placed in the same location. This keeps the swarm size constant.
Elimination and Dispersal: Gradual or sudden changes in the local environment where a bacterium population lives may occur due to various reasons e.g. a significant local rise of temperature may kill a group of bacteria that are currently in a region with a high concentration of nutrient gradients. Events can take place in such a fashion that all the bacteria in a region are killed or a group is dispersed into a new location.
Size of population „S‟: Increasing S can significantly increase the computational complexity of the algorithm. However, for larger values of S, it is more likely at least some bacteria near an optimum point should be started, and over time, it is then more likely that many bacterium will be in that region, due to either chemotaxis or reproduction.
Length of chemotactic step „C(i)‟: If C(i) are too large, then if the optimum value lies in a valley with steep edges, the search will tend to jump out of the valley, or it may simply miss possible local minima by swimming through them without stopping. On the other hand, if C(i) are too small, convergence can be slow, but if the search finds a local minimum it will typically not deviate too far from it. c(i) is a sort of a “step size” for the algorithm.
Chemotactic step „Nc‟: If the size of Nc is chosen to be too short, the algorithm will generally rely more on luck and reproduction, and in some cases, it could more easily get trapped in a local minimum (premature convergence). Ns creates a bias in the random walk (which would not occur if Ns = 0), with large values tending to bias the walk more in the direction of climbing down the hill.
Reproduction number „Nre‟: If Nre is too small, the algorithm may converge prematurely; however, larger values of Nre clearly increase computational complexity.
Elimination and dispersal number „Ned‟: A low value for Ned dictates that the algorithm will not rely on random elimination-dispersal events to try to find favorable regions. A high value increases computational complexity but allows the bacteria to look in more regions to find good nutrient concentrations. Clearly, if ped is large, the algorithm can degrade to random exhaustive search. If, however, it is chosen appropriately, it can help the algorithm jump out of local optima and into a global optimum.
Parameters defining cell-to-cell attractant functions „Jcc‟: If the attractant width is high and very deep, the cells will have a strong tendency to swarm (they may even avoid going after nutrients and favor swarming). On the other hand, if the attractant width is small and the depth shallow, there will be little tendency to swarm and each cell will search on its own. Social versus independent foraging is then dictated by the balance between the strengths of the cell-to-cell attractant signals and nutrient concentrations. [21]
 
 
 
Fig. 5: BFA flow chart

E.	Artificial Bee Colony Algorithm
The artificial bee colony (ABC) consists of three groups of bees: employed bees, onlooker bees and scout bees and three actions: searching food source, recruiting bees for the food source and abandoning the food source. Employed bees exploit food source and share the information about the food source with onlookers. Onlooker bees wait in the hive for the information employed bees provided. Scout bees search for the new food source. Employed bees share information about food sources by dancing in the dance area and the nature of dance is proportional to the nectar content of food source just exploited by the dancing bees. Onlooker bees watch the dance and choose a food source according to the probability proportional to the quality of that food source. Therefore, good food sources attract more onlooker bees. Whenever a bee, whether it is scout or onlooker, finds a food source it becomes employed. Whenever a food source is exploited fully, all the employed bees associated with it abandon it, and may become scouts or onlookers. In the ABC algorithm, a food source position represents a possible solution of the problem to be optimized which is represented by a d-dimension real-valued vector. The nectar amount of a food source corresponds to the quality (fitness) of the associated solution. The number of employed bees or the onlookers is equal to the number of the food sources (solutions) in the population. In other words, for every food source, there is only one employed bee [22 ].
Algorithm:
At the first step, the artificial bees colony generates a randomly distributed initial population P(G = 0) of pn solutions (food source positions), where pn denotes the size of population. Each solution xi (i = 1, 2, ..., pn) is a d- dimensional vector. Here, d is the number of optimization parameters. After initialization, the population of the positions (solutions) is subjected to repeated cycles, C = 1, 2, ...,MCN (maximum cycle number), of the search processes of the employed bees, the onlooker bees and scout bees. An employed bee produces a modification on the position (solution) in her memory depending on the local information (visual information) and tests the nectar amount (fitness value) of the new source (new solution). Provided that the nectar amount of the new one is higher than that of the previous one, the
 
bee  memorizes the new position and  forgets the old one. Otherwise she keeps the position of the previous one  in        her memory. After all employed bees complete the search process; they share the nectar information of the food sources and their position information with the onlooker bees on the dance area. An onlooker bee evaluates the nectar  information taken from all employed bees and chooses a food source with a probability related to its nectar amount. As in the case of the employed bee, she produces a modification on the position in her  memory  and  checks  the  nectar amount of the candidate source. Providing that its nectar is higher than that of the previous one, the bee memorizes the new position and forgets the old on. An artificial onlooker bee chooses a food source  depending  on the  probability value associated with that food source, pi calculated by the equation:

 
pi 
 
fit i SN
fit n
n1	(5)
 
where fiti is the fitness value of the solution i which is proportional to the nectar amount of the food source in the position i and pn is the number of food sources which is equal to the number of employed bees (pn ).
In order to produce a candidate food position from the old one in memory, the artificial BA uses the following expression in eq. (6).
 
vi j  xi j  ij (xij  xkj )
 

(6)
 
where k ∈ { 1, 2,..., pn} and j ∈ { 1,  2,...,d} are randomly chosen indexes.  Although k  is  determined  randomly, it has to be different from i. Øij is a random number between [-1, 1]. It controls the production of neighbor food sources around xij and represents the comparison of two food positions visually by a bee. As can be seen from eq. (6), as the difference between the parameters of the xij and xkj decreases, the perturbation on the position xij gets decrease, too. Thus, as the search approaches to the optimum solution in the search space, the step length is adaptively reduced. If a parameter value produced by this operation exceeds its predetermined limit, the parameter can be set to an acceptable value. In this work, the value of the parameter exceeding its limit is set to its limit value. The food source of which the nectar is abandoned by the bees is replaced with a new food source by the scouts. In ABC, this is simulated by producing a position randomly and replacing it with the abandoned one. Hence that providing that a position cannot be improved further through a predetermined number of cycles, then that food source is assumed to be abandoned. The value of predetermined number of cycles is an important control parameter of the artificial BA, which is called “limit” for abandonment. Assume that the abandoned source is xij and j ∈ {1, 2,..., d}, then the scout discovers a new food source to be replaced with xi .This operation can be defined as in eq. (7).
 
xi      xi	 rand(0,1)(xi      xi	)
 

(7)
 

 


Fig. 6 Artificial Bee Colony flow chart
 
After each candidate source position vij is produced and then evaluated by the artificial bee, its performance is compared with that of its old one. If the new food has equal or better nectar than the old source, it is replaced with the old one in the memory. Otherwise, the old one is retained in the memory. In other words, a greedy selection mechanism is employed as the selection operation between the old and the candidate one. It is clear from the above explanation that there are four control parameters used in the ABC: The number of food sources (pn) which is equal to the number of employed and onlooker bees, the value of limit, the maximum cycle number (mcn).

F.	Simulated Annealing (SA)
Simulated Annealing is a generic probabilistic meta-algorithm used to find an approximate solution to global optimization problems. It is inspired by annealing in metallurgy which is a technique of controlled cooling of material to reduce defects [23][24][25]. The Simulated Annealing algorithm starts with a random solution. A random nearby  solution is formed by every iteration. If this solution is a better solution, it will replace the current solution. If it is a  worse solution, it may be chosen to replace the current solution with a probability that depends on the temperature parameter. As the algorithm progresses, the temperature parameter decreases, giving worse solutions a lesser chance of replacing the current solution.
We allow worst solutions at the beginning to avoid solution converging to a local minimum rather than the global minimum. We will use the simulated annealing algorithm to solve Random Travelling Salesman Problem. The salesman must visit each city only once and return to the same city in which he began. The constraints that affect the outcome of the algorithm are the initial temperature, the rate at which the temperature decreases and the stopping condition of the algorithm. By adjusting these values, we run the SA and to see that how algorithm responds.
The SA algorithm is described as in flow chart in figure 7.



Fig. 7 Simulated Annealing flow chart

IV.	IMPLEMENTATION
The experimental results are produced and tested by MatLab software. To encode the inputs (coordinates of cities, or distance between cities), each dataset stored in excel file and read it by MatLab as a matrix.
In this paper we use six datasets of cities with different sizes:
1.	Arabic24.tsp : 24 capital cities in Arabic world
2.	berlin52.tsp: 52 locations in Berlin
3.	ch150.tsp: 150 cities (churritz)
4.	lin318.tsp: 318 cities (Lin/Kernighan)
5.	fl1400.tsp: 1400 Drilling (Reinelt)
6.	brd14051.tsp : 14051 BR Deutschland in den Grenzen von 1989 (Bachem/Wottawa)

The Machine Specification that used to implement the experimental results is:- HP-Z420 Workstation Desktop
Available Processors : 4 Available Cores	: i7 Available Memory	: 4 G
Available Windows	: WIN-7, 64-bit
As shown table 1, all techniques work well with suitable running time for dataset with small size up to tens of cities. But for datasets with hundreds cities some techniques converge to local minimum solution, is not the best one. On other hand, for thousands cities all techniques suffer to converge the solution and we cannot guarantee the best solution. Also the techniques show different results within different long running time.
For dataset with 14050 cities, GA, ABC and BFO cannot complete for different reasons: GA needs more memory, ABC faced cycling problem, while BFO do not converge at all running times.On the other side, three techniques ACO, PSO, and SA complete all dataset although they spent a lot of time (around 24 hours) to converge solution that is not guaranteed to be the best.
 
Table I Results Of All Techniques To Measure Best Value (Path), No. Of Iteration, And Running Time
Dataset		GA	ACO	PSO	BFO	BCO	SA

Arabic24	Best Value	229	229	229	229	229	229
	# of Iterations	131	155	104	98	110	97
	Run Time	1 s.	0 s.	0 s.	0 s.	0 s.	0 s.

berlin52	Best Value	7544	7544	7544	7544	7544	7544
	# of Iterations	129	128	116	91	114	101
	Run Time	6 s.	4	3	5	4	3

ch150	Best Value	6873	6873	6874	6877	6874	6872
	# of Iterations	248	192	207	237	209	176
	Run Time	70 s.	27	20	22	25	19

lin318	Best Value	47,940	47,941	47,941	47,946	47,943	47,936
	# of Iterations	615	582	568	602	593	571
	Run Time	848 s.	562	517	648	681	449

fl1400	Best Value	57,761	57,754	57,749	57,772	57,765	57,754
	# of Iterations	20,898	21,826	19,517	22,004	22,109	22,038
	Run Time	32,863 s.	26,352 s.	24,798	29,513	28,976	20,997

brd14051	Best Value	
Out of time	8,183,942	7,970,284	
Out of time	
Out of time	7,963,861
	# of Iterations		152,729	128,097			133,410
	Run Time		87,519	85,725			81,839

We can determine if the solution is wrong or may be the best solution from graph of tour. As in figures of datasets solutions, if there intersecting lines on path of solution, we can conclude that solution is not optimal (best), the best solution should be without intersecting lines, figure (8 a) shows the best tour for dataset (Arabic24), and figure (8 b) also gives the best tour for database (berlin52), while figure (8 c) illustrates some intersecting lines that indicate that the solution is not the best tour.
(a)	(b)	(c)
Fig. 8 Solution of some datasets: (a) Optimal solution of (Arabic 24), (b) optimal solution of (berlin52), (c) Solution of (ch150) (not optimal)

V.	CONCLUSION
This paper presents some optimization techniques for solving the Travelling Salesman Problem. All techniques produced good results for small dataset but may be not optimal if the size will increase. The running time and path distance increases with increasing number of cities. The quality of the results of any dataset increases with increasing population size but when increases the population size, the running time was increased. So we must to do the best to balance between runtime and the solution quality.
Finally, we noted that GA is good technique but needs more space memory to present its power for solving the problems, while SA does not need additional space because it saves the best solution as so far and ignore others.
In this work, SA, PSO, and then ACO proved their capability to solve TSP.

