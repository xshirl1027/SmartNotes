import heapq

class Node: 
    '''super class for main data structure'''
    ID = 0
    name = ''
    text = ''
    priority = 0
    connections = []
    
    def __init__(self, text):
        self.ID = id
        self.text = text
        
    def get_id():
        return ID
    
    def set_name(self,name):
        self.name = name
    
    def set_text(self,text):
        self.text = text
    
    def get_text(self):
        return self.name+" "+self.text
        
    def set_con(self, new_con):
        self.connections.add(new_con)
    
    def set_priority(self,priority):
        self.priority = priority
    
    def get_priority(self):
        return self.priority

        
class Concept_Node(Node): 
    '''node specialized for storing major concepts'''
    priority = 0
    
    def __init__(self, ame, text):
        Node.__init__(text)
        Node.set_name(name)

    def get_name():
        Node.get_name()
        


class Definition():
    term = ''
    definition = ''
    reference = 0
    
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
    
    def incre_ref(self, num):
        self.reference += num
        
    def decre_ref(self, num):
        self.reference -= num
        
    def get_ref(self):
        return self.reference
    
    def get_term(self):
        return self.term
    
    def get_def(self):
        return self.definition
    
    def get_text(self):
        return self.term + ": "+ self.definition
    
    def __lt__(self,other):
        return self.reference > other.reference
    def __eq__(self,other): 
        return self.reference == other.reference
    def __str__(self):
        return str(self.reference)    
    
    
class Graphs:
    '''store and maintain network of nodes'''
    #update definition list whenever a new node is added
    
    
    
    
class Definition_List:
    '''self-organizing priority queue that acts as an observer for Graph'''
    dictionary = []
    
    observing = None
    def add_term(self,definition):
        self.dictionary.insert(0,definition)
        heapq.heapify(self.dictionary)
        
    def parse_node(self,node):
        #increment occurrence of word
        node_str = node.get_text()
        for term in self.dictionary:
            term.incre_ref(node_str.count(term.get_term()))
        heapq.heapify(self.dictionary)
    
    def print_list(self):
        for term in self.dictionary:
            print(term.get_text())

newlist = Definition_List()
newnode = Node("hi")
newdef = Definition("asia", "a eastern continent")
newlist.add_term(newdef)
newlist.print_list()
#newlist.print_list()