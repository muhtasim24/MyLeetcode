'''
we have to design an LRU Cache, Least Recently Used Cache 
We have a capacity,
We can put key,value pairs into the cache, and if the key already exists, update the value
If when putting a new key,val pair, and we are above the capacity, 
we need to remove the least recently used
And theres a function to get a key, if it exists just return the val
and when we call get on a key, that becomes the most recently used node

We will use a linked list to keep track of the order of least and most recently used 
and it would be easier to remove and add new nodes and change ordering

we can use a hashmap to map the key to the node itself 
Since we would need to change ordering, we will use a DOUBLY LINKED LIST
and to keep track of the least and most recently used nodes, we will have dummy nodes
LEFT AND RIGHT DUMMY NODES
the closer a node is to the left, it is less recently used
the closer a node is to the right, it is more recently used

we will create helper functions
When inserting we want to insert right BEFORE our RIGHT DUMMY NODE
Prev Node -><- self.right
        NEW Node
prev Node -><- New Node -><- self.right

when removing a node, we want to take the previous and next of that node 
and simply make the prev node.next == to the nodes next
and the next of that node.prev ==  becomes the prev node
just destroy the link

When called get, if key is in cache, remove and insert again so it automatically goes to right most
to make it most recently used node 

When called put, if key is in cache, remove and then craete the node
create key to node pariing in the cache
insert node to linked list

after inserting check if we are above the capacity
if we are remove the LRU, least recently used which is the .next of self.left
its not self.left itself because that is just a dummy node
remove from linkedlist
and remove from cache
'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None #initlaize prev and next to be NULL

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}

        #initilize the left and right pointers to tell use least and most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        #break the links of nodes'prev and next
        prev, nxt = node.prev, node.next
        #update prev next to nodes next
        #update nxt to nodes prev
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        #insert node right BEFORE self.right, so it is most recently used
        prev, nxt = self.right.prev, self.right
        #new node is in between prev and self.right, create the new links
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache: 
            #if its in the cache, remove and reinsert so it is near most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val #accessing the value of the key only gives us the node,
                                        #so we do .val to get the actual value of the node 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #if key in cache, remove from list so we can just create a new node with the updated
            #key,value pair and insert it at the rightmost
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) #put new node into the map
        self.insert(self.cache[key]) #insert in linked list
        
        if len(self.cache) > self.cap: #if we are above the capcity limit
            #remove the LRU, which is the .next of the self.left
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] #lru is a node, remove the key and 
                                # it will remove the pairing from the map


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
