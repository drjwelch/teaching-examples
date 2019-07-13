class DataSource:

    # Defines how to 'make' a datasource object
    # A datasource has properties: flag, id and ptr
    # Flag is True if the datasource is a file
    # id is the file handle or list name
    # ptr is the position we're up to in the list (ignored for a file)
    def __init__(self,name,flag):
        self.flag = flag
        if flag:
            self.id = open(name,'r')
        else:
            self.id = name
        self.ptr = 0

    # Define how to do FOR i IN DataSource:
    # __next__ gets the next line/item from the datasource
    def __iter__(self):
        if self.flag:
            self.id.seek(0)
        else:
            self.ptr = 0
        return self

    def __next__(self):
        if self.flag: # it's a file
            d = self.id.readline().strip()
            if d == "": # end of file (EOF)
                raise StopIteration()
            else:
                return d
        else: # it's a list
            if self.ptr > len(self.id)-1:
                raise StopIteration()
            else:
                d = self.id[self.ptr] 	# keep track of where we're up
                self.ptr += 1	    	# to by using self.ptr
                return d

    # Linear search in a DataSource
    def find(self,target):
        for d in self: # this only works because of the code above
            print("checking",d)
            if d == target:
                return True
        return False

mylist = [1,2,3]
filename = 'data.txt'
a = DataSource(mylist,False)
b = DataSource(filename,True)

while True:
    target = input("Enter data: ")
    try:
        target = int(target)
    except:
        pass
    
    if a.find(target): print("Found in list")
    if b.find(target): print("Found in file")
