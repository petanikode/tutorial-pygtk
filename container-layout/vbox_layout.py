#!/usr/bin/python

import gtk

class App(gtk.Window):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.set_title("VBox Layout App")
        self.set_size_request(640, 360)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # membuat kontainer vbox
        vbox = gtk.VBox(homogeneous=False, spacing=5)
                
        # membuat button
        btn_ok = gtk.Button("OK")
        btn_ok.set_size_request(70, 30)
        btn_close = gtk.Button("Close")
        
        vbox.add(btn_ok)
        vbox.add(btn_close)
        
        # tambahkan layout vbox ke window
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main()
        
        
