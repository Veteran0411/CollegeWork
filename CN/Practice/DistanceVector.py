import sys

class Network():
    def __init__(self,nodes):
        self.nodes=nodes
        self.graph={}
        self.distance_vector={}
    
    def add_link(self,n1,n2,cost):
        if n1 not in self.graph:
            self.graph[n1]={}
        self.graph[n1][n2]=cost

        if n2 not in self.graph:
            self.graph[n2]={}
        self.graph[n2][n1]=cost
    
    def initialize_distance_vector(self,node):
        self.distance_vector[node]={node:0}
        for n in self.nodes:
            if n!=node:
                self.distance_vector[node][n]=sys.maxsize

    def  update_distance_vector(self,node):
        for dest in self.nodes:
            if dest!=node:
                mincost=sys.maxsize
                for neighbor in self.graph[node]:
                    if dest in self.distance_vector[neighbor]:
                        cost=self.distance_vector[neighbor][dest]+self.graph[node][neighbor]
                        if cost<mincost:
                            mincost=cost
                self.distance_vector[node][dest]=mincost

    def print_distance_vector(self,node):
        print(f"printing routing table for {node}")
        print("destination\t\tcost")
        for dest,cost in self.distance_vector[node].items():
            if node!=dest:
                print(f"{dest}\t\t{cost}")
        print()
                
nodes=[1,2,3,4,5]
network=Network(nodes)
network.add_link(1,2,5)
network.add_link(1,3,15)
network.add_link(1,4,12)
network.add_link(1,5,1)
network.add_link(4,2,5)

for n in nodes:
    network.initialize_distance_vector(n)
    
num_iteration=6
for i in range(num_iteration):
    for n in nodes:
        network.update_distance_vector(n)
        
for n in nodes:
    network.print_distance_vector(n)