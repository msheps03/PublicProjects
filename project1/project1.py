import csv
import time
import random


class City:
    def __init__(self,cid,cname,cstate,pop,cities):
        self.cid = str(cid) # City id
        self.cname = cname # city name
        self.cstate = cstate # city's state
        self.pop = pop # City's Population
        self.cities = cities # Array thjat contains confirmed cases for 2 months

        self.leftChild, self.rightChild, self.key = None, None, None # Replaces need for node class

    def __str__(self): # returns formatted list of cid,cname,cstate,pop, and most recent number of cases
        return "cid: " + self.cid + "; cname: " + self.cname + "; cstate: " + self.cstate + \
               "; cases:" + str(self.cities[-1])


class COV19Library:
    def __init__(self):
        self.cityArray = [] # initialize array
        self.size = len(self.cityArray) # size is len of city array
        self.isSorted = False # list is not initially sorted

        self.root = None

    def LoadData(self, filename):
        with open(filename, 'r') as data: # open the file that is passed with the function
            sheet = csv.reader(data,delimiter = ',') # Seperate values from csv file by commas
            firstRow = True # set to true because first row is the column headers
            for column in sheet: # for each column in the sheet
                if not firstRow: # is ignored if firstRow is True
                    cid = column[0]
                    name = column[1].split() # split the city and state name by spaces

                    if len(name) != 1:
                        state = name[-1]  # call the last instance of list name, which will be the state
                        cname = " ".join(name[:-1]) # joining city names together, index is all elements except last
                    else:
                        cname = name[-1] # call the last instance of list name, which will be the state
                        state = "None"
                    pop = column[2] # population
                    infections = [] # initialize empty list for infections
                    for i in range(4,65): # from row 4 to row 65
                        infections.append(int(column[i]))
                    city = City(cid, cname, state, pop, infections)
                    self.cityArray.append(city)
                firstRow = False
                self.size = len(self.cityArray)

    def linearSearch(self, city, attribute): # for 100 Trials:2.1298 s, avg of 0.021298
        if attribute == "id":  # check if attribute is "id"
            for i in range(self.size):
                if self.cityArray[i].cid == city: # if city id is equal to passed id print info then return
                    return self.cityArray[i] # calling the __str__ function in city class
        elif attribute == "name":  # check is attribute is "name"
            for i in range(self.size):
                if self.cityArray[i].cname == city: # if city name is same as the passed name print info then return
                    return self.cityArray[i] # calling the __str__ function in city class
        return "City not found" # if city isn't found

    def quickSort(self): # code from class appended with setting sorted to true
        alist = self.cityArray
        self.quickSortHelper(alist,0, self.size - 1) # calls helper function
        self.isSorted = True
        self.cityArray = alist

    def quickSortHelper(self,alist,first, last): # code from class
        if first < last:
            splitpoint = self.partition(alist,first, last)

            self.quickSortHelper(alist,first, splitpoint - 1) # recursively run for first "half" of list
            self.quickSortHelper(alist,splitpoint + 1, last)  # recursively run for second "half" of list

    def partition(self, alist,first, last): # code from class changed alist to self.cityarray[].cname, to compare names
        pivotValue = alist[first].cname
        leftMark = first + 1
        rightMark = last
        done = False
        while not done:
            while leftMark <= rightMark and alist[leftMark].cname <= pivotValue:
                leftMark = leftMark + 1
            while alist[rightMark].cname >= pivotValue and rightMark >= leftMark:
                rightMark = rightMark - 1
            if rightMark < leftMark:
                done = True
            else:
                temp = alist[leftMark]
                alist[leftMark] = alist[rightMark]
                alist[rightMark] = temp
        temp = alist[first]
        alist[first] = alist[rightMark]
        alist[rightMark] = temp
        return rightMark

    def buildBST(self): # total time of 0.00050044, avg time of 0.0000050044
        # t0 = time.time()
        self.quickSort()
        self._buildBST(self.cityArray)
        mid = self.size // 2
        self.root = self.cityArray[mid] # Selects root node to be the middle of the sorted list
        # print(time.time()-t0)

    def _buildBST(self,arr):
        if len(arr) == 0: # if list is empty return none
            return None
        mid = len(arr)//2 # mid point of passed cityArray
        arr[mid].leftChild = self._buildBST(arr[:mid]) # recursively call _buildBST for the left half of the list
        arr[mid].rightChild = self._buildBST(arr[mid+1:]) # recursively call _buildBST for the right half of the list
        return arr[mid] # 

    def searchBST(self,cid):
        city = self._searchBST(cid,self.root)
        if self.root and city: # if root is not none
            return city
        return "City not found"

    def _searchBST(self,cid,root): # helper function for searchBST
        if root is None:
            return "City not found"
        elif cid < root.cid: # check if cid is in left half of tree
            return self._searchBST(cid,root.leftChild)
        elif cid > root.cid: # check if cid is in the right half of tree
            return self._searchBST(cid,root.rightChild)
        else: # cid does not exist in list
            return root

    def timing(self): # used to complete the rest of tasks
        list =[] # intiailize empty list to hold the ids that the functions check for
        for i in range(100):
            x = random.randint(0,941)
            list.append(self.cityArray[x])
        t0 = time.time() # initial time for linear search
        for i in list: # run linear search 100 times for values in list
            self.linearSearch(i.cid,"id")
        tfLinear = time.time() - t0 # final time for linear search
        t0 =time.time() # initial time for binary search tree
        for i in list: # run binary search 100 times for values in list
            self.searchBST(i.cid)
        tfBST = time.time() - t0
        return tfLinear, tfBST # return the time for linear and binary respectively

if __name__ == "__main__":
    c = COV19Library()
    c.LoadData("cov19_city.csv")
    c.buildBST()