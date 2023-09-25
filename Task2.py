#importing libraries for use
import json
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import queue
import heapq


#importing json files as dictionaries for use
with open(r"C:\Users\draco\OneDrive - Nanyang Technological University\NTU Y3\SC3000 Artifical Intelligence\Lab Assignment\Data Files\G.json") as a:
  G = json.load(a)
with open(r"C:\Users\draco\OneDrive - Nanyang Technological University\NTU Y3\SC3000 Artifical Intelligence\Lab Assignment\Data Files\Dist.json") as b:
  Dist = json.load(b)
with open(r"C:\Users\draco\OneDrive - Nanyang Technological University\NTU Y3\SC3000 Artifical Intelligence\Lab Assignment\Data Files\Cost.json") as c:
  EC = json.load(c)
with open(r"C:\Users\draco\OneDrive - Nanyang Technological University\NTU Y3\SC3000 Artifical Intelligence\Lab Assignment\Data Files\Coord.json") as d:
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

shortestPath, shortestDistance, totalEC, curEC, nodeVisitedCount = UCS1(G, source, terminateState, energyBudget, EC, Coord, Dist)
#print(shortestPath)

if (shortestPath is not None):
    print(f"Shortest Path: {shortestPath}")
    print(f"Shortest Distance: {shortestDistance}")
    print(f"Total Energy Cost: {totalEC}")
    print(f"Number of Nodes Visted: {nodeVisitedCount}")
else:
    print("No path found")