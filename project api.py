import heapq

class Node: 
    '''super class for main data structure'''
    ID = 0
    name = ''
    text = ''
    priority = 0
    connections = []
    
    def __init__(self, text, con): #by default, Node is init as a comment node without name
        self.ID = id
        self.text = text
        self.connections.insert(0, con)
        
    def get_id():
        return ID
    
    def set_name(self,name): #name will only be set if concept_node class is invoked
        self.name = name
    
    def set_text(self,text): #update text
        self.text = text
    
    def get_string(self): #return the entire node in string
        return self.name+" "+self.text
        
    def add_con(self, new_con): #add a connection to another node
        self.connections.insert(0,new_con)
    
    def set_priority(self,priority):
        self.priority = priority
    
    def get_priority(self):
        return self.priority

        
class Concept_Node(Node): 
    '''node specialized for storing major concepts'''
    priority = 0
    
    def __init__(self, name, text):
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
    
    def incre_ref(self, num): #increase number of references
        self.reference += num
        
    def decre_ref(self, num):
        self.reference -= num
        
    def get_ref(self):
        return self.reference
    
    def get_term(self):
        return self.term
    
    def get_def(self):
        return self.definition
    
    def get_string(self):
        return self.term + ": "+ self.definition
    
    def __lt__(self,other):
        return self.reference > other.reference
    def __eq__(self,other): 
        return self.reference == other.reference
    def __str__(self):
        return str(self.reference)    
    
    
class Graph:
    '''store and maintain network of nodes'''
    #update definition list whenever a new node is added
    
    
    
    
class Definition_List:
    '''self-organizing priority queue that acts as an observer for Graph'''
    dictionary = []
    
    observing = None
    def add_term(self,definition):
        self.dictionary.insert(0,definition)
        heapq.heapify(self.dictionary)
        
    def parse_node(self,node): #increment reference of definition based on number of occurrence in this node
        node_str = node.get_string()
        for term in self.dictionary:
            term.incre_ref(node_str.count(term.get_term()))
        heapq.heapify(self.dictionary)
    
    def print_list(self):
        for term in self.dictionary:
            print(term.get_string())

  
         
def test_defintion_heap():
    newnode = Node("hi", None)
    newdef = Definition("Asia", "An eastern continent")
    newdef2 = Definition("America", "A country on fire")
    newdef.incre_ref(4)
    newdef2.incre_ref(2)
    dictionary.add_term(newdef2)
    dictionary.add_term(newdef)
    dictionary.print_list()
    dictionary = None
    #dictionary.print_list()

def test_parse_node():
    dictionary = Definition_List()
    graph = Graph()    
    testnode = Node("China is a country in Asia that has been occupied by America America America Military in the 1940s. It is also the largest country in Asia", None)
    newdef = Definition("Asia", "An eastern continent")
    newdef2 = Definition("America", "A country on fire")    

    dictionary.add_term(newdef)
    dictionary.add_term(newdef2)
    dictionary.parse_node(testnode)
    dictionary.print_list()
    dictionary  = None
    

test_parse_node()

    