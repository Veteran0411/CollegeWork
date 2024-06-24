#TW 1

from collections import defaultdict 
graph=defaultdict(list)


def addEdge(u,v):
      graph[u].append(v)

def dfid(start,goal,max_depth):
      print("Start node us: ",start," Goal node is :",goal)
      for i in range(max_depth):
            print("At level :",i+1)
            print("Path taken is: ",end=" ")
            isfound=dfs(start,goal,i)
            if isfound:
                  print("\nNode found !\n")
                  return
            else:
                  print("\nNode not found!\n")
                  

def dfs(start,goal,depth):
      print(start,end=" ")
      if start==goal:
            return True
      if depth<=0:
            return
      for i in graph[start]:
            if dfs(i,goal,depth-1):
                  return True
      return False

goal=defaultdict(list)
addEdge('A','B')
addEdge('A','C')
addEdge('A','D')
addEdge('C','E')
addEdge('C','F')
addEdge('D','G')
addEdge('D','H')
addEdge('G','I')
addEdge('H','K')
addEdge('H','L')
addEdge('I','J')
addEdge('K','O')
addEdge('L','M')
addEdge('M','N')
dfid('A','O',4)