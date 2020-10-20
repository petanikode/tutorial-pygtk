#!/usr/bin/python

import gtk

class App(gtk.Window):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.set_title("HBox Layout App")
        self.set_size_request(640, 360)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # membuat kontainer hbox
        hbox = gtk.HBox(homogeneous=False, spacing=5)
                
        # membuat button
        btn_ok = gtk.Button("OK")
        btn_ok.set_size_request(70, 30)
        btn_close = gtk.Button("Close")
        
        hbox.add(btn_ok)
        hbox.add(btn_close)
        
        # tambahkan layout hbox ke window
        self.add(hbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main()
