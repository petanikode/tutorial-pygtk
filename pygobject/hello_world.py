import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_title("Hello World App")
window.set_size_request(640, 360)
window.connect('destroy', Gtk.main_quit)
window.show_all()

Gtk.main()
