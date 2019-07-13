import pickle

# Define a queue object - needed for printing out but interesting in itself!

class Queue:
    def __init__(self):
        self.items = [] # uses a list as the queue

    def enqueue(self, item):
        self.items.insert(0,item) # enqueue adds new item at start (tail) of list

    def dequeue(self):
        return self.items.pop() # dequeue removes from the end (head)

    def count(self):
        return len(self.items)

    def countdata(self):
        return len(self.items) - self.items.count(None)
        
# Define a Node object

class Node:
        
    def __init__(self,value): # the special init method creates a new Node
        self.data = value # set the data to parameter value
        self.leftpointer = None # set the pointer to Null
        self.rightpointer = None # set the pointer to Null
        
# Define a BinaryTree object

class BTree:
        
    def __init__(self,firstvalue): # create a linked list
        self.firstnode = Node(firstvalue) # create a single node
        
    def addNode(self,value):
        newnode = Node(value) # make a new node
        nxt = self.firstnode
        while True:
            if value < nxt.data:
                if nxt.leftpointer == None:
                    nxt.leftpointer = newnode
                    break
                else:
                    nxt = nxt.leftpointer
            else:
                if nxt.rightpointer == None:
                    nxt.rightpointer = newnode
                    break
                else:
                    nxt = nxt.rightpointer
    
    def contains(self,value):
        nxt = self.firstnode
        return BTree.ncontains(value,nxt)
    
    def ncontains(value,nodepointer):
        if nodepointer == None:
            return False
        elif nodepointer.data == value:
            return True
        else:
            return BTree.ncontains(value,nodepointer.leftpointer) or \
                   BTree.ncontains(value,nodepointer.rightpointer)
    MAXSP = 60
    
    def printout(self):    
        q = Queue()
        sp = int(BTree.MAXSP/2)
        q.enqueue(self.firstnode)
        while q.count() > 0:
            if q.count() in [2,4,8,16,32,64,128]: # max 8 levels of tree
                if q.countdata()==0: break # if this row is all nulls, exit
                print("\n")
                sp = int(BTree.MAXSP / (q.count()+1))
            n = q.dequeue()
            if n == None:
                print(" "*sp+"@",end='') # show @ for nulls
                q.enqueue(None)
                q.enqueue(None)
            else:
                print(" "*sp+str(n.data),end='')
                q.enqueue(n.leftpointer)
                q.enqueue(n.rightpointer)
        print("\n\n---------------END OF TREE---------------\n")
        
# Guess the animal game

try:
    with open('data.pickle', 'rb') as f:
        mytree = pickle.load(f)
except:
    mytree = BTree("Does it have 4 legs?")
    yesnode = Node("Dog")
    nonode = Node("Snake")
    mytree.firstnode.leftpointer = yesnode
    mytree.firstnode.rightpointer = nonode

playing = True

print("Think of an animal ...")

while playing:
    current_node = mytree.firstnode
    while current_node != None:
        if current_node.data.endswith("?"): # if this node is a question ...
            print(current_node.data)
            ans = input()
            if ans.lower()[0]=='y':
                current_node = current_node.leftpointer
            else:
                current_node = current_node.rightpointer
        else: # this node is not a question, so it's an animal guess
            print("Is it a",current_node.data,"?")
            ans = input()
            if ans.lower()[0]=='y':
                print("Thought so!")
                current_node = None # to end the game: computer wins
            else:
                print("Oh. What is it?")
                ans = input()
                print("Give me a question to distinguish a",ans,"from a",current_node.data)
                qn = input()
                if qn[-1]!='?': qn+='?'
                newanimal = Node(ans)
                thisanimal = Node(current_node.data)
                current_node.data = qn
                current_node.leftpointer = newanimal
                current_node.rightpointer = thisanimal
                current_node = None # to end the game: player wins
    print("Game over!")
    print("Play again?")
    ans = input()
    if ans.lower()[0]!='y':
        playing = False

with open('data.pickle', 'wb') as f:
    pickle.dump(mytree, f)

