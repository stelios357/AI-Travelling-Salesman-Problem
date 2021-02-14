# TSP

# problem statement :
'''
given a list of cities. all cities are connected with each other with some weights (weights can be
either distances or time). what is the shortest possible route that visits each city  
and return to original city.it also has many variants like "can not travel one edge twice" or "can not 
move one edge in same direction twice" 

'''

'''

A* algorithm 

-> f(n) = g(n) + h(n)

'''







#import array
from sys import maxsize 
INT_MAX = maxsize 


class Link:
    def __init__(self,x):
        self.data = x
        self.next = None


class Graph:
    def __init__(self, x):
        self.n = x              # number of vertices
        self.adjmatrix = []     # adjacency matrix representation of actual distances g(n)
        self.MSTmatrix = []     # heuristics matrix (MST edges low weight & non MST edge original weight)
        self.flag = []          # utility flag array 
        self.final_cost = []    # it is final cost f(n) = g(n) + h(n)
        self.final_cost_flag = []   # utility flag
     #    self.visit = []*self.n
        self.adjlist = [None]*self.n   # initialization of adjlist size
        
        # adjacency matrix initialization with max value of integer
        for i in range(self.n):
            for j in range(self.n):
                self.adjmatrix.append([INT_MAX for i in range(self.n)])

        # MST heuristic matrix initialization with -1 value
        for i in range(self.n):
            for j in range(self.n):
                self.MSTmatrix.append([-1 for i in range(self.n)])

        # flag initialization with 0 value
        for i in range(self.n):
            for j in range(self.n):
                self.flag.append([0 for i in range(self.n)])

        # final cost f(n) initialization with -1 value
        for i in range(self.n):
            for j in range(self.n):
                self.final_cost.append([-1 for i in range(self.n)])

        # flag initialization with 0 value 
        for i in range(self.n):
            for j in range(self.n):
                self.final_cost_flag.append([0 for i in range(self.n)])

    ''' utitlity function to make adjacency list and matrix with (u,v) vertices and w weight '''
    def graphical(self, u, v, w):
        self.graphlist(u, v)
        self.graphmatrix(u, v, w)

    ''' it will make adj list with help of (u,v) vertices '''
    def graphlist(self, u, v):
        newnode = Link(v)
        if self.adjlist[u] is None:
            self.adjlist[u] = newnode
        else:
            temp1 = self.adjlist[u]
            while temp1.next is not None:
                temp1 = temp1.next
            temp1.next = newnode
        newnode = Link(u)
        if self.adjlist[v] is  None:
            self.adjlist[v] = newnode
        else:
            temp2 = self.adjlist[v]
            while temp2.next is not None:
                temp2 = temp2.next
            temp2.next = newnode


    ''' it will make adjacenecy matrix with help of (u,v) vertices '''
    def graphmatrix(self, u, v, w):
        self.adjmatrix[u][v] = w
        self.adjmatrix[v][u] = w
        
    ''' it will call the function to visualize the matrix '''
    def graphic(self,V):
#        self.list()
        self.matrix(V)

    def list(self):
        for i in range(self.n):
            temp = self.adjlist[i]
            print(i)
            while temp is not None:
                print(temp.data)
                temp = temp.next
            print("\n")

    ''' 
    it will print the adjacency matrix and call the prim method that will make MST with 
    help of prim's algorithm
    
    '''
    
    def matrix(self, V):
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.adjmatrix[i][j] = INT_MAX
        # calling prim's method to apply prims algorithm
        self.prim(self.adjmatrix,V)
  
    
    
    
    
    ''' utility function for checking the validity of edge '''
    def edge_validity(self,u, v, edge_inside_mst): 
        if edge_inside_mst[u] == False and edge_inside_mst[v] == False: 
            return False
        if u == v: 
            return False
        elif edge_inside_mst[u] == True and edge_inside_mst[v] == True: 
            return False
        return True
      
    ''' prim's algorithm : it will make MST matrix that is also huristics matrix'''
    def prim(self,cost,V): 
        edge_inside_mst = [False] * V 
      
        # include first vertex in MST 
        edge_inside_mst[0] = True
        
        # initilization of MST array that will take count of all edge value in MST
        MST = [0]*(V-1)
      
        edge_count = 0
        mincost = 0
        while edge_count < V - 1: 
      
            minn = INT_MAX 
            a = -1
            b = -1
            for i in range(V): 
                for j in range(V): 
                    if cost[i][j] < minn: 
                        if self.edge_validity(i, j, edge_inside_mst): 
                            minn = cost[i][j] 
                            a = i 
                            b = j 
      
            if a != -1 and b != -1: 
                print("(%d, %d) cost: %d" % (a, b, minn)) 
                MST[edge_count] = minn
                edge_count += 1
                mincost += minn 
                edge_inside_mst[b] = edge_inside_mst[a] = True
      
        print("Minimum cost = %d" % mincost) 
        for i in range(edge_count):
            print(MST[i])
            
        # it will make a MST matrix (heurisitcs matrix) 
        ''' 
        it will traverse all edge value and collate with MST edge and assign weight 
        according them
        
        '''
        
        for k in range(0,edge_count): 
            for i in range(V): 
                for j in range(V): 
                    if self.adjmatrix[i][j] == MST[k] and self.flag[i][j] == 0:
                        self.MSTmatrix[i][j] = 0;
                        self.flag[i][j] = 1;
                    elif self.flag[i][j] == 0:
                        self.MSTmatrix[i][j] = self.adjmatrix[i][j];
    
        # it will make the final cost matrix f(n) = g(n) + h(n) (adjacency matrix + MST_heuristics matrix)
        for i in range(V): 
            for j in range(V): 
                if i is not j:
                    self.final_cost[i][j] = self.adjmatrix[i][j] + self.MSTmatrix[i][j]                
                else:
                    self.final_cost[i][j] = -1
        
        # applying a* algorithm
        self.a_star_algorithm(V)

    def a_star_algorithm(self, V):
        
        count = 0 # it will count if all edges are visited
        i = 0 # start with 0th edge
        j = 0 
        minimum = 0 # total cost
        mini_index = 0 
        flag_variable = [0]*V # utility flag variable to count if vertex visited or not  
        flag_variable[i] = 1 # 0th vertex is visited intially

        '''
        it will find the min cost and traverse to that vertex and so on.the visited vertex will be set to 1
        
        '''
        
        while count < V:
            count = 0       # it will count number of edges visited
            mini = INT_MAX 
            for j in range(0,V): 
                if mini > self.final_cost[i][j] and self.final_cost[i][j] != -1 and self.final_cost_flag[i][j] == 0:
                    mini = self.final_cost[i][j]
                    mini_index = j
                    
            print("%d -> %d" % (i,mini_index))    

                
            self.final_cost_flag[i][mini_index] = 1
 #           self.final_cost_flag[mini_index][i] = 1 # (restriction that it can not travel back same edge)

            minimum = minimum + self.adjmatrix[i][mini_index]
            i = mini_index;
            flag_variable[i] = 1
            print("cost of travel " , minimum)
            for k in range(0,V):
                if flag_variable[k] == 1:
                    count = count + 1
                    
            print("number od edges visited " , count)

        mini = INT_MAX
        for j in range(0,V):
            if mini > self.final_cost[i][j] and self.final_cost[i][j] != -1:
                mini = self.final_cost[i][j]
                mini_index = j
        print("%d -> %d" % (i,mini_index))        
        minimum = minimum + self.adjmatrix[i][mini_index] 
        print("number od edges visited " , count)
        print("cost of travel " , minimum)              
           


def main():

    
    V = input("enter the number of vertices")
    V = int(V)
    graph = Graph(V)
    


    
    
    
    u = 0
    v = 1
    u = int(u)
    v = int (v)
    
    for i in range(V*(V-1)):
        if u < v: 
            w = input("enter the weight for (%d,%d) " %  (u,v)) 
            w = int(w)
            graph.graphical(u,v,w)
        if v == V-1:
            u = u+1
            v = 0
        else:
            v = v+1
    

    # test case 1

    '''
    graph.graphical(0,1,4)
    graph.graphical(0,2,7)
    graph.graphical(0,3,6)
    
    graph.graphical(1,2,2)
    graph.graphical(1,3,11)
    graph.graphical(2,3,8)
    
    '''

# test case 2    
    
    '''
    graph.graphical(0,1,4)
    graph.graphical(0,2,7)
    graph.graphical(0,3,2)
    
    graph.graphical(1,2,6)
    graph.graphical(1,3,11)
    graph.graphical(2,3,8)
    '''

            
# test case 3     
        
    '''
    
    
    graph.graphical(0,1,10)
    graph.graphical(0,2,15)
    graph.graphical(0,3,20)
    
    graph.graphical(1,2,35)
    graph.graphical(1,3,25)
    graph.graphical(2,3,30)
    '''

# test case 4

    '''
    
    
    graph.graphical(0,1,4)
    graph.graphical(0,2,100)
    graph.graphical(0,3,100)
    graph.graphical(0,4,8)
    graph.graphical(0,5,100)
    graph.graphical(0,6,100)
    graph.graphical(0,7,8)
    graph.graphical(0,8,100)

    
    graph.graphical(1,2,8)
    graph.graphical(1,3,100)
    graph.graphical(1,4,100)
    graph.graphical(1,5,100)
    graph.graphical(1,6,100)
    graph.graphical(1,7,11)
    graph.graphical(1,8,100)


    graph.graphical(2,3,7)
    graph.graphical(2,4,100)
    graph.graphical(2,5,4)
    graph.graphical(2,6,100)
    graph.graphical(2,7,100)
    graph.graphical(2,8,2)

    graph.graphical(3,4,9)
    graph.graphical(3,5,14)
    graph.graphical(3,6,100)
    graph.graphical(3,7,100)
    graph.graphical(3,8,100)

    graph.graphical(4,5,10)
    graph.graphical(4,6,100)
    graph.graphical(4,7,100)
    graph.graphical(4,8,100)

    graph.graphical(5,6,2)
    graph.graphical(5,7,100)
    graph.graphical(5,8,100)

    graph.graphical(6,7,1)
    graph.graphical(6,8,6)

    graph.graphical(7,8,7)
    
    '''

    # test case 5
    
    
    graph.graphical(0,1,4)
    graph.graphical(0,2,6)
    graph.graphical(0,3,15)
    graph.graphical(0,4,20)
    graph.graphical(0,5,9)

    
    graph.graphical(1,2,3)
    graph.graphical(1,3,8)
    graph.graphical(1,4,5)
    graph.graphical(1,5,12)


    graph.graphical(2,3,2)
    graph.graphical(2,4,18)
    graph.graphical(2,5,16)

    graph.graphical(3,4,14)
    graph.graphical(3,5,10)

    graph.graphical(4,5,11)
    

    graph.graphic(V)


if __name__ == "__main__": 
    main()



