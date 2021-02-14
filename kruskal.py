class Kruskal:
    def __init__(self,vertices):
        #initializing number of vertices and empty list for graph edges
        self.V=vertices
        self.adj_list=[]
        self.adj_mat_mst=[[0 for i in range(vertices)] for j in range(vertices)]
        self.vis={}


    def dfs(self,start):                                      # perform dfs 
        self.vis[start]=True
        print(start,end=" ")
        for i,w in enumerate(self.adj_mat_mst[start]):
            if(w!=0 and i not in self.vis):
                self.vis[i]=True
                self.dfs(i)

    def makeMST(self):
        rank=[]
        self.adj_list=sorted(self.adj_list,key=lambda item: item[2]) #sorting edges based on their weight
        par=[]

        for node in range(self.V):
            rank.append(0)
            par.append(node)            #initially, each vertex has its own set        
        
        i=0
        mst=[]
        cov_edges=0     # number of edges in MST

        while cov_edges<self.V-1:               #iterate until there are V-1 edges in the mst
            u,v,w=self.adj_list[i]
            set1=self.belongs_to(par,u)          #FIND-SET operation on vertex u
            set2=self.belongs_to(par,v)          #FIND-SET operation on vertex v
            i+=1
            #if u and v belong to different sets then we can combine them 
            #to the same set as there are no cycles
            if set1!=set2:
                self.combine(par,rank,set1,set2)                                   
                cov_edges+=1
                mst.append([u,v,w])
        for u,v,wt in mst:          #making the adjacency matrix of the mst
            print("MST Edge between vertices %d and %d has weight: %d" % (u,v,wt))
            self.adj_mat_mst[u][v]=wt
            self.adj_mat_mst[v][u]=wt
        print("The path to be followed is:")
        self.dfs(0)                 #performing dfs
        print(0,end=" ")

    def belongs_to(self,par,i):
        #finds the set which contains vertex i
        if par[i]==i:
            return i
        return self.belongs_to(par,par[i])


    def combine(self,par,rank,set1,set2):
        #used to combine the set of vertices x and y 
        x_set=self.belongs_to(par,set1)
        y_set=self.belongs_to(par,set2)
        #if x's set has lesser rank, combine it into y's set 
        if rank[x_set]<rank[y_set]:
            par[x_set]=y_set
        #if y's set has lesser rank, combine it into x's set
        elif rank[x_set]>rank[y_set]:
            par[y_set]=x_set
        #if they have the same rank, combine y'set to x's set and raise it's rank by 1
        else:
            par[y_set]=x_set
            rank[x_set]+=1


    def addedge(self,u,v,wt):
        #adding an edge between vertices u and v having weight wt
        self.adj_list.append([u,v,wt])
        self.adj_list.append([v,u,wt])



if __name__ == "__main__":

    num_ver=int(input("Enter the number of vertices:"))
    g=Kruskal(num_ver)    #making an object of class Kruskal with num_ver vertices
    num_edge=int(input("Enter the number of edges:"))

    for i in range(num_edge):
        u=int(input("Enter 1st vertex:"))
        v=int(input("Enter 2nd vertex:"))
        wt=int(input("Enter edge weight:"))
        g.addedge(u,v,wt)

    g.makeMST()         #calling the method that implements kruskal algorithm to make the MST
