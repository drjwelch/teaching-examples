# Define a Node object

class ListNode:
        
    def __init__(self, value, weight=0): # the special init method creates a new Node
        self.data = value # set the data to parameter value
        self.weight = weight # set the weight (used for graph adjacency list)
        self.pointer = None # set the pointer to the next node to be Null
        
# Define a LinkedList object

class LinkedList:
        
    def __init__(self,firstvalue,weight=0): # create a linked list
        self.firstnode = ListNode(firstvalue,weight) # create a single node
        
    def addNode(self,value,weight=0):
        newnode = ListNode(value,weight) # make a new node
        nxt = self.firstnode
        while nxt.pointer != None:  # traverse the list
            nxt = nxt.pointer
        nxt.pointer = newnode # link new node onto end of list
    
    def getNodebyWeight(self,target): # find a node that has a given weight
        nxt = self.firstnode
        while nxt.weight!=target: # traverse list
            if nxt.pointer==None: # at the end? => not found
                return None # return a null pointer
            else:
                nxt = nxt.pointer
        return nxt.data # found it - return the data value of this node

    def printout(self):
        nxt = self.firstnode
        while nxt.pointer != None: # traverse list printing each item
            print(nxt.data,", ",end='',sep='')
            nxt = nxt.pointer
        print(nxt.data,end='')
        print()

        
# Define a GraphNode object - a GraphNode comprises an ID and a (linked) list of adjacent nodes

class GraphNode:
    def __init__(self, txt): # graph nodes have an i.d. and linked list of adjacent nodes
        self.id = txt
        self.adjacent = None # adjacent list is none to start with
        self.whatshere = None
        
# Define a Graph object - a graph is a list of GraphNodes

class Graph:
    def __init__(self,node_desc):
        self.nodes = [GraphNode(node_desc)] # a graph is a list of nodes

    def add_node(self, txt):
        new_node = GraphNode(txt)
        self.nodes.append(new_node) # add a new node to the list for this graph
        
    def get_node_by_id(self,nodeid):
        for node in self.nodes: # find the node with this given nodeid
            if node.id == nodeid:
                return node # returns a pointer to the node
        return None

    def add_edge(self, id1,id2,d1,d2): # we are using the linked list / edge weight to store the direction (d1,d2)
        node1 = self.get_node_by_id(id1) # get a pointer to the node with the given id
        node2 = self.get_node_by_id(id2)
        if node1 == None or node2 == None: return None # if those id's are not real nodes, return null
        if node1.adjacent == None:
            node1.adjacent = LinkedList(node2,d1) # if there're no adjacent nodes yet, start the linked list
        else:
            node1.adjacent.addNode(node2,d1) # but if there are, add a new linked list node
        if node2.adjacent == None:
            node2.adjacent = LinkedList(node1,d2) # make the link work both ways
        else:
            node2.adjacent.addNode(node1,d2)

    def get_new_node(self,current_node,direction):
        edges = current_node.adjacent
        return edges.getNodebyWeight(direction)


# Initialise the game map
		
game_map = Graph("forest")

# Add more nodes (places)

game_map.add_node("clearing")
game_map.add_node("house")
game_map.add_node("hillbottom")
game_map.add_node("entrycave")
game_map.add_node("hilltop")

# Add routes from one node to another (and back)

game_map.add_edge("forest","clearing","n","s")
game_map.add_edge("forest","house","e","w")
game_map.add_edge("forest","hillbottom","s","n")
game_map.add_edge("forest","entrycave","w","e")
game_map.add_edge("house","clearing","n","e")
game_map.add_edge("hilltop","hillbottom","d","u")

# Create descriptions of each location

descriptions = {} # dict:  the node id is the key; the value is the description of that node
descriptions["forest"] = "You are in a forest.  There are paths in all directions."
descriptions["clearing"] = "You are in a clearing in the forest.  Paths lead south and east."
descriptions["house"] = "You are outside a small house.  Paths lead west and north."
descriptions["hillbottom"] = "You are at the bottom of a tall hill.  It looks too tall to climb.  A path leads north."
descriptions["entrycave"] = "You are at the entrance to a cave.  It is too small to fit through.  A path leads east."
descriptions["hilltop"] = "You maverick.  You can see for miles.  The only way is down, baby."

# Start the game in the forest

current_node = game_map.get_node_by_id("forest")
current_node.whatshere = LinkedList("sword")

while True:
    print(descriptions[current_node.id]) # say where you are
    if current_node.whatshere!=None:
        print("Here there is a: ",end='')
        current_node.whatshere.printout()
    command = input(">> ")
    if command == 'die': break
    new_node = game_map.get_new_node(current_node,command[0]) # traverse graph in the direction asked for
    if new_node == None:
        print("You can't go that way") # if no edge in that direction
    else:
        current_node = new_node # go to new node along the chosen edge

print("You are dead.")
