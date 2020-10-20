#!/usr/bin/python

import gtk

class App(gtk.Window):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.set_title("VBox dan Hbox Layout App")
        self.set_size_request(640, 360)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # membuat kontainer vbox dan hbox
        vbox = gtk.VBox(homogeneous=False, spacing=5)
        hbox = gtk.HBox(homogeneous=False, spacing=10)
                
        # membuat button
        btn_ok = gtk.Button("OK")
        btn_ok.set_size_request(70, 30)
        btn_close = gtk.Button("Close")
        
        hbox.add(btn_ok)
        hbox.add(btn_close)
        
        vbox.add(gtk.Label("Aplikasi gabungan VBox dan HBox"))
        vbox.add(gtk.Label("Teks ini berada dalam VBox"))
        
        vbox.add(hbox)
        
        # tambahkan layout vbox ke window
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main()
        
        
