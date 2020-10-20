#!/usr/bin/python

import gtk

class App(gtk.Window):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.set_title("Alignment Layout App")
        self.set_size_request(640, 360)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # membuat kontainer vbox dan hbox
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)
        
        # membuat kontainer Alignment vertikal
        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)
        
        # membuat button
        btn_ok = gtk.Button("OK")
        btn_ok.set_size_request(70, 30)
        btn_close = gtk.Button("Close")
        
        #menambahkan button ke kontainer horizontal box
        hbox.add(btn_ok)
        hbox.add(btn_close)
        
        # membuat kontainer aligment horizontal
        halign = gtk.Alignment(0, 0, 0.5, 0)
        halign.add(hbox)
        
        # tambahkan halign layout ke valign
        vbox.pack_start(halign, False, False, 3)
        
        # tambahkan layout vbox ke window
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main()
        
        
