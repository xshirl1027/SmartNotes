"""
Functionality that is currently working:

Press the circle button once: click anywhere to create a node there.
Press the circle button before clicking anywhere else: turn off node creation.

Press the line button: click one node and then another node and will create a line between the two nodes.
Press the line button before clicking the second node (or the first node): turn off line creation. 
"""

from tkinter import *

class FrontEndNode:

    def __init__(self, x, y, i):
        self.i = i
        self.x = x
        self.y = y
        self.connection_list = {}

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_i(self):
        return self.i

def is_in_node(x, y, cir_x, cir_y):
    if x > cir_x - 50:
        if cir_x + 50 > x:
            if y > cir_y - 50:
                if cir_y + 50 > y:
                    return True

    return False

def switch_on_make_circle():
    global make_circle_switch
    
    if make_circle_switch == 1:
        make_circle_switch = 0
    else:
        make_circle_switch = 1

def switch_on_make_line():
    global make_line_switch

    if make_line_switch == 0:
        make_line_switch = 1
    else:
        make_line_switch = 0

def make_circle(event):
    global make_circle_switch
    global make_line_switch
    global line_pos
    
    if make_circle_switch == 1: 
        arc = main_window.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill="red")
        fnode = FrontEndNode(event.x, event.y, arc)
        circ_list.append(fnode)
        make_circle_switch = 0

    elif make_line_switch != 0:
        for cir in circ_list:
            if is_in_node(event.x, event.y, cir.get_x(), cir.get_y()):
                line_pos.append(cir)
                make_line_switch = make_line_switch + 1
                break

        if make_line_switch == 3:
            main_window.create_line(line_pos[0].get_x(), line_pos[0].get_y(), line_pos[1].get_x(), line_pos[1].get_y(), width=7)
            main_window.tag_raise(line_pos[0].get_i())
            main_window.tag_raise(line_pos[1].get_i())
            make_line_switch = 0
            line_pos = []

def remove_circle():
    """
    if (len(circ_list) == 0):
        pass
    else:
        main_window.delete(circ_list.pop())
    """
    pass

if __name__ == "__main__":

    #Initialize Window
    top = Tk()
    top.wm_title("SmartNotes")
    main_window = Canvas(top, bg="#FFFFFF", height=700, width=1300)

    #Global Variables
    circ_list = []
    make_circle_switch = 0
    make_line_switch = 0
    line_pos = []

    #Initalize Button Images
    line_photo = PhotoImage(file="arrow.png")
    plus_photo = PhotoImage(file="plus.png")
    minus_photo = PhotoImage(file="minus.png")
    circle_photo = PhotoImage(file="circle.png")
    cross_photo = PhotoImage(file="cross.png")

    #Create Node Button
    node_button = Button(main_window, command=switch_on_make_circle)
    node_button.place(x=0, y=0)
    node_button.config(image=circle_photo, width="75", height="75")

    #Create Line Button
    line_button = Button(main_window, command=switch_on_make_line)
    line_button.place(x=100, y=0)
    line_button.config(image=line_photo, width="75", height="75")

    #Create Display Layer Button
    plus_button = Button(main_window)
    plus_button.place(x=200, y=0)
    plus_button.config(image=plus_photo, width="75", height="75")

    #Create Hide Layer Button
    minus_button = Button(main_window)
    minus_button.place(x=300,y=0)
    minus_button.config(image=minus_photo, width="75", height="75")

    #Create Delete Button
    cross_button = Button(main_window, command=remove_circle)
    cross_button.place(x=400, y=0)
    cross_button.config(image=cross_photo, width="75", height="75")
    
    #Run Program
    main_window.bind("<Button-1>", make_circle)
    main_window.pack()
    top.mainloop()
