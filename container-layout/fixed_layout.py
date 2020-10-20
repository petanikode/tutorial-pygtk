#!/usr/bin/python

import gtk

class App(gtk.Window):

    def __init__(self):
        super(App, self).__init__()

        self.set_title("Container Fixed")
        self.set_size_request(300, 280)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(000, 6400, 6400))
        self.set_position(gtk.WIN_POS_CENTER)
        
        button1 = gtk.Button("Tombol 1")
        button2 = gtk.Button("Tombol 2")
        button3 = gtk.Button("Tombol 3")
                       
        container = gtk.Fixed()
           
        container.put(button1, 20, 20)
        container.put(button2, 40, 160)
        container.put(button3, 170, 50)

        self.add(container)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main() 
