class Node: 
    '''super class for main data structure'''
    ID = 0
    text = ''
    priority = 0
    connections = []
    
    def __init__(text):
        this.ID = id
        this.text = text
        
    def get_id():
        return ID
    
    def set_text(text):
        this.text = text
    
    def get_text():
        return this.text
        
    def set_con(new_con):
        connections.add(new_con)
    
    def set_priority(priority):
        this.priority = priority
    
    def get_priority():
        return this.priority

        
class Concept_Node: 
    '''node specialized for storing major concepts'''
    concept = ''
    priority = 0
    
    def __init__(name, text):
        Node.__init__(text)
        concept = name
        
    def print_str():
        return this.concept + ": " + Node.get_text
    
    def print_concept():
        return concept
    
    def print_text():
        return Node.get_text
           

class Definiton():
    term = ''
    definition = ''
    reference = 0
    
    def __init__(term, definition):
        this.term = term
        this.definition = definition
    
    def incre_ref(num):
        this.reference += num
        
    def decre_ref(num):
        this.reference -= num
        
    def get_reference():
        return reference
    
    def get_term():
        return term
    
    def get_definition():
        return definition
    
    
class Graph():
    '''store and maintain network of nodes'''
    
    
    
class Definition_List():
    '''self-organizing priority queue that acts as an observer for Graph'''
    dictionary = {} #ordered in desc by reference
    observing = Object()
    def add_term(defintion):
        dictionary.add(defintion);
    
    
        