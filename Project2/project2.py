import csv
import sys
from Graph import *
from QueueX import *

class OSN:
    def __init__(self):
        self.network = Graph()
        self.negNetwork = Graph()
        self.MST = Graph()

    def buildGraph(self, filename):
        with open(filename, 'r') as data: # open the file that is passed with the function
            sheet = csv.reader(data,delimiter=',') # Separate values in the csv file by commas
            for column in sheet:
                firstName = column[0]
                secondName = column[1]
                weight = int(column[2])
                self.network.addEdge(firstName, secondName, weight)
                self.network.addEdge(secondName, firstName, weight)
                # Same network but negative, useful for building a Max spanning tree
                self.negNetwork.addEdge(firstName, secondName, -weight)
                self.negNetwork.addEdge(secondName, firstName, -weight)


    def findDistance(self, user1, user2):
        distance = 0 # initialize distance

        vertex1 = self.network.getVertex(user1) # Vertex of user 1
        vertex2 = self.network.getVertex(user2) # Vertex of user 2
        # Modified Djinkstra method
        pq = PriorityQueue() # Initialize Priority Queue
        vertex1.setDistance(0) # Distance on initial vertex is 0

        pq.buildHeap([(v.getDistance(), v) for v in self.network])
        while not pq.isEmpty():
            currentVert = pq.delMin() # Take smallest value and pop it
            for nextVert in currentVert.getConnections(): # For each connection to the current vertex
                newDist = currentVert.getDistance() + 1 # Distance is each node it passes through, therefore past nodes
                # +1 for the current node
                if newDist < nextVert.getDistance(): # If new path is shorter than the current path, change path
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)
        # End of Djinkstra method
        # Would vertex1.getDistance() work? alternatively vertex2.getDistance()?
        while vertex2.getPred(): # Vertex 2 tracks back until it reaches vertex 1, vertex 1 does not have a
            # predecessor node therefore when the vertex is none, vertex1 == vertex2
            distance += 1 # Distance + 1 for each node that is passed through
            vertex2 = vertex2.getPred()

        for v in self.network: # Reset dist and pred of nodes in the graph, necessary for gradescope
            v.dist = sys.maxsize
            v.pred = None

        return distance


    def buildMST(self):
        start = self.network.getVertex("Lynch") # Initialize starting vertex
        prim(self.negNetwork,start) # Define predecessor nodes using the prim function
        for vertex in self.negNetwork:
            for connections in vertex.getConnections():
                if connections == vertex.getPred(): # If the connection is the predessor, all the work was done by prim
                    # algorithm to create the maximum spanning tree
                    self.MST.addEdge(connections.id, vertex.id, -vertex.getWeight(connections))
                    self.MST.addEdge(vertex.id, connections.id, -vertex.getWeight(connections))

    def findPath(self, user1, user2):
        # Find user1 as current vertex, span one way, if it isn't there than span the other way.
        vertex1 = self.MST.getVertex(user1) # Vertex that corresponds to the id given for user 1
        vertex2 = self.MST.getVertex(user2)
        bfs(self.MST, vertex1) # Define the predecessors/the path to follow for the tree

        list = [] # Initialize Empty list, will be the path from user 1 to user 2

        while vertex2:
            list.append(vertex2.id)
            vertex2 = vertex2.getPred()

        list.reverse() # Reverse the list
        for v in self.MST: # Reset the vertices in the self.MST graph
            v.dist = sys.maxsize
            v.pred = None
            v.color = "white"

        return " -> ".join(list)

    def findClosePath(self, user1, user2):
        vertex1 = self.network.getVertex(user1)  # Vertex that corresponds to the id given for user 1
        vertex2 = self.network.getVertex(user2)
        bfsWeighted(self.network, vertex1, vertex2)  # Parse the MaxST
        list = [] # Initialize empty list, this will be the order from user1 to user2
        weight = 0 # Initialize weight as 0
        v2Original = vertex2 # vertex2 Hold in order to add to the weight to end of the list
        while vertex2.getPred(): # Add elements to the list that are predecessors (bfsWeighted did all work)
            list.append(vertex2.getPred().id)
            weight += vertex2.getPred().getWeight(vertex2)
            vertex2 = vertex2.getPred()

        weight = " (" + str(weight) + ")" # Proper output for the weight
        list.reverse()
        list.append(v2Original.id + weight) # Last list index adds the weight to the end

        for v in self.network: # Reset function, could make a function inside OSN class
            v.setDistance(0)
            v.dist = sys.maxsize
            v.pred = None
            v.color = "white"

        return " -> ".join(list)



if __name__ == "__main__":
    O = OSN()
    O.buildGraph("facebook_network (1).csv")
    # print(O.findDistance("Lynch", "Murray"))
    # print(O.findDistance("Murray", "Clark"))
    O.buildMST()
    print(O.findClosePath("Lynch", "Clark"))
