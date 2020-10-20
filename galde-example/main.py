#!/usr/bin/python 

import gtk

# membuat object builder untuk load ui glade
builder = gtk.Builder()
builder.add_from_file("main_window.glade")

# membuat objek window dari ui glade
window = builder.get_object("window1")

# event saat close button diklik
window.connect("destroy", gtk.main_quit)

window.show_all()
gtk.main()
