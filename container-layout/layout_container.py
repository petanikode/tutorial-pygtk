#!/usr/bin/python

import gtk

class App(gtk.Window):
    
    def __init__(self):
        super(App, self).__init__()
        
        self.set_title("Layout Container App")
        self.set_size_request(640, 360)
        self.set_position(gtk.WIN_POS_CENTER)
        
        # membuat object scrolled_window
        scrolled_window = gtk.ScrolledWindow()
        
        # membuat layout container dengan ukuran 400x400
        layout_container = gtk.Layout()
        layout_container.set_size(400,400)
        
        btn = gtk.Button("Klik saya")
        
        # tambahkan button ke dalam layout pada posisi 125,200
        layout_container.put(btn, 125, 200)
        
        # tambahkan layout ke dalam scrolled_window
        scrolled_window.add(layout_container)
        
        # tambahkan scrolled_window ke dalam window utama
        self.add(scrolled_window)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        

App()
gtk.main()
        
        
