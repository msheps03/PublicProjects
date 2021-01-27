from Graph import *

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class PriorityQueue:
        def __init__(self):
            self.heapArray = [(0, 0)]
            self.currentSize = 0

        def buildHeap(self, alist):
            self.currentSize = len(alist)
            self.heapArray = [(0, 0)]
            for i in alist:
                self.heapArray.append(i)
            i = len(alist) // 2
            while (i > 0):
                self.percDown(i)
                i = i - 1

        def percDown(self, i):
            while (i * 2) <= self.currentSize:
                mc = self.minChild(i)
                if self.heapArray[i][0] > self.heapArray[mc][0]:
                    tmp = self.heapArray[i]
                    self.heapArray[i] = self.heapArray[mc]
                    self.heapArray[mc] = tmp
                i = mc

        def minChild(self, i):
            if i * 2 > self.currentSize:
                return -1
            else:
                if i * 2 + 1 > self.currentSize:
                    return i * 2
                else:
                    if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                        return i * 2
                    else:
                        return i * 2 + 1

        def percUp(self, i):
            while i // 2 > 0:
                if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                    tmp = self.heapArray[i // 2]
                    self.heapArray[i // 2] = self.heapArray[i]
                    self.heapArray[i] = tmp
                i = i // 2

        def add(self, k):
            self.heapArray.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)

        def delMin(self):
            retval = self.heapArray[1][1]
            self.heapArray[1] = self.heapArray[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapArray.pop()
            self.percDown(1)
            return retval

        def isEmpty(self):
            if self.currentSize == 0:
                return True
            else:
                return False

        def decreaseKey(self, val, amt):
            # this is a little wierd, but we need to find the heap thing to decrease by
            # looking at its value
            done = False
            i = 1
            myKey = 0
            while not done and i <= self.currentSize:
                if self.heapArray[i][1] == val:
                    done = True
                    myKey = i
                else:
                    i = i + 1
            if myKey > 0:
                self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
                self.percUp(myKey)

        def __contains__(self, vtx):
            for pair in self.heapArray:
                if pair[1] == vtx:
                    return True
            return False

def prim(G,start):
    pq = PriorityQueue() # Call priority Queue
    for v in G: # For vertex in the passed graph, reset values for distance and precessor
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0) # Distance from root node to start is 0
    pq.buildHeap([(v.getDistance(),v) for v in G]) # Create a heap, essentially doubleQueue
    while not pq.isEmpty():
        currentVert = pq.delMin() # CurrentVertex is popped from the heap, then analyzed for connections
        for nextVert in currentVert.getConnections(): # NextVert is the current connection being analyzed
            newCost = currentVert.getWeight(nextVert) # Self-explanatory
            if nextVert in pq and newCost<nextVert.getDistance(): #
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert,newCost)

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def bfsWeighted(g,start,end):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0: # unchanged
        currentVert = vertQueue.dequeue() # unchanged
        for nbr in currentVert.getConnections(): # where nbr is each connection, store vertices with a path weight check
            closeness = currentVert.getWeight(nbr) + currentVert.getPathWeight()
            newWeight = nbr.getPathWeight()+nbr.getWeight(currentVert)
            if nbr.getDistance() == sys.maxsize: # If distance is maxsize connection hasn't been visited
                nbr.setPred(currentVert)
                nbr.setPathWeight(closeness)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(nbr)

            # Checks if new pathweight would be less than current pathweight
            elif newWeight > currentVert.getPathWeight() and nbr.getDistance() < currentVert.getDistance():
                currentVert.setPathWeight(newWeight)
                currentVert.setPred(nbr)
