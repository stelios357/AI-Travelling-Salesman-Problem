import sys


def dfs(start,vis,adj_mat):                 # code for dfs
    vis[start]=True
    print(start,end=" ")
    for i,w in enumerate(adj_mat[start]):
        if(w!=0 and i not in vis):
            vis[i]=True
            dfs(i,vis,adj_mat)

p=sys.maxsize   #a very large positive number
num_ver=int(input("Enter number of vertices:"))
adj_mat=[[0 for i in range(num_ver)] for j in range(num_ver)]   #initializing adjacency matrix of graph with 0s
fringe=[False for i in range(num_ver)] #denotes the vertices on the fringe
num_edge=int(input("Enter number of edges:"))
adj_mat_mst=[[0 for i in range(num_ver)] for j in range(num_ver)]   #initializing adjacency matrix of MST with 0s
for i in range(num_edge):           # making the adjacency matrix
    u=int(input("Enter 1st vertex:"))
    v=int(input("Enter 2nd vertex:"))
    wt=int(input("Enter edge weight:"))
    adj_mat[u][v]=wt
    adj_mat[v][u]=wt
cov_edges=0
fringe[0]=True #initializing fringe with source 
while(cov_edges<num_ver-1): #for MST to be fully connected we must have num_ver-1 edges in it
    min=p           # initialize min as a large number
    start=0         # vertex from which the newly added edge will originate
    end=0           # vertex from which the newly added edge will terminate
    for i in range(num_ver):
        if fringe[i]==True:    #if vertex is on the fringe, we will explore its outgoing edges to add to MST 
            for j in range(num_ver):
                if (fringe[j]==False and adj_mat[i][j]!=0):  #if vertex is not on the fringe and connected to explored vertex then check if it is a minimum cut-edge
                    if min>adj_mat[i][j]:
                        min=adj_mat[i][j]
                        start=i                             # if edge weight is minimum then store the starting and ending vertex
                        end=j
    cov_edges+=1    #increment the number of edges in MST
    fringe[end]=True   #adding the new terminal node to the fringe
    print("Edge between vertex ",start," and vertex ",end," has weight:",adj_mat[start][end])   #adjacency matrix for MST
    adj_mat_mst[start][end]=adj_mat[start][end]
    adj_mat_mst[end][start]=adj_mat[start][end]

vis={}
print("Path to be followed is: ")
dfs(0,vis,adj_mat_mst)  #performing dfs on MST
print(0,end=" ")
