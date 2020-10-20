#!/usr/bin/python 

import gtk

class App:
    
    def __init__(self):
        self._initUI()
        
    def _initUI(self):
        # membuat object builder untuk load ui glade
        builder = gtk.Builder()
        builder.add_from_file("main_window.glade")
        self.window = builder.get_object("window1")
        
        self.button = builder.get_object("button1")
        self.button.connect("clicked", self.on_button_click)
        
        self.window.connect("destroy", gtk.main_quit)
        self.window.show_all()
    
    def on_button_click(self, button):
        print("Button diklik!")

App()
gtk.main()
 
