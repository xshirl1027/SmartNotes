from tkinter import *

def make_circle(event):
    global make_circle_switch
    global make_line_switch
    global line_pos
    
    if make_circle_switch == 1: 
        arc = main_window.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, fill="red")
        circ_list.append([arc, (event.x, event.y)])
        make_circle_switch = 0

    elif make_line_switch != 0:
        for cir in circ_list:
            if event.x > cir[1][0] - 50 and cir[1][1] + 50 > event.x and event.y > cir[1][1] - 50 and cir[1][1] + 50 > event.y:
                line_pos.append(cir)
                make_line_switch = make_line_switch + 1
                print(make_line_switch)

                if make_line_switch == 3:
                    main_window.create_line(line_pos[0][1][0], line_pos[0][1][1], line_pos[1][1][0], line_pos[1][1][1], width=7)
                    main_window.tag_raise(line_pos[0][0])
                    main_window.tag_raise(line_pos[1][0])
                    make_line_switch = 0
                    line_pos = []
                    print(line_pos)

def remove_circle():
    if (len(circ_list) == 0):
        pass
    else:
        main_window.delete(circ_list.pop())

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

    print(make_line_switch)

    

if __name__ == "__main__":
    top = Tk()
    top.wm_title("SmartNotes")
    circ_list = []
    make_circle_switch = 0
    make_line_switch = 0
    line_pos = []

    main_window = Canvas(top, bg="#FFFFFF", height=700, width=1300)

    line_photo = PhotoImage(file="arrow.png")
    plus_photo = PhotoImage(file="plus.png")
    minus_photo = PhotoImage(file="minus.png")
    circle_photo = PhotoImage(file="circle.png")

    node_button = Button(main_window, command=switch_on_make_circle)
    node_button.place(x=0, y=0)
    node_button.config(image=circle_photo, width="75", height="75")

    line_button = Button(main_window, command=switch_on_make_line)
    line_button.place(x=100, y=0)
    line_button.config(image=line_photo, width="75", height="75")

    plus_button = Button(main_window)
    plus_button.place(x=200, y=0)
    plus_button.config(image=plus_photo, width="75", height="75")

    minus_button = Button(main_window, command=remove_circle)
    minus_button.place(x=300,y=0)
    minus_button.config(image=minus_photo, width="75", height="75")

    main_window.create_line(0, 0, 200, 200, width=7)

    main_window.bind("<Button-1>", make_circle)
    main_window.pack()

    top.mainloop()
