#importing libraries for use
import json
import heapq
from timeit import default_timer as timer

#importing json files as dictionaries for use
with open(r"dataFiles/G.json") as a:
  G = json.load(a)
with open(r"dataFiles/Dist.json") as b:
  Dist = json.load(b)
with open(r"dataFiles/Cost.json") as c:
  EC = json.load(c)
with open(r"dataFiles/Coord.json") as d:
  Coord = json.load(d)


def UCS1(Graph, start, end, EnergyBudget, EC, Coord, Dist):
    frontier = [(0, 0, start, 0, [start])] #(totalDist, totalCost, vertex, curEC, visitedNodes[])
    nodeVisitedCount =1
    #initialisation
    visitedNodes = set()
    totalCost=0
    totalDist =0
    while frontier:
        totalDist, totalCost, curNode, curEC, pathtaken = heapq.heappop(frontier)
        #When node 50 is reached, the search process terminates. 
        if (curNode == end):
            #break
            return '->'.join(pathtaken), newDist, newCost, curEC, nodeVisitedCount
        #Skip node if node has been visited with a lower energy cost
        if (curNode in visitedNodes):
            continue
        #print(curNode)
        #Mark the curNode as visitedNode with its corresponding curEC
        #visitedNodes[(int(curNode))] = curEC
        visitedNodes.add(curNode)
        #newG = json.dumps(Graph)
        
        #Explore neighbours of curNode
        for neighbour in Graph[curNode]:
            energyCost = EC[curNode + ',' + neighbour]
            newEC = curEC + energyCost
            if(newEC <= EnergyBudget):
                newPath = pathtaken + [neighbour]
                distance = Dist[curNode + ',' + neighbour]
                newDist = totalDist + distance
                newCost = newEC
                heapq.heappush(frontier, (newDist, newCost, neighbour, newEC, newPath))
                nodeVisitedCount +=1
        
    return None, None, None, None, None

source = '1'
terminateState = '50'
energyBudget = 287932

#track computational time for search algorithm
start_time = timer()
shortestPath, shortestDistance, totalEC, curEC, nodeVisitedCount = UCS1(G, source, terminateState, energyBudget, EC, Coord, Dist)
end_time = timer()

print("time taken for UCS algorithm: ", end_time- start_time)
shortestPath1 = "S" + shortestPath[(1):shortestPath.index("50")] + "T"
#print(shortestPath)

if (shortestPath is not None):
    print(f"Shortest Path: {shortestPath}")
    print(f"Shortest Path: {shortestPath1}") #to show source node as S and terminate state as T. 
    print(f"Shortest Distance: {shortestDistance}")
    print(f"Total Energy Cost: {totalEC}")
    print(f"Number of Nodes Visted: {nodeVisitedCount}")
else:
    print("No path found")
