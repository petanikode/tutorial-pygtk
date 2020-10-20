import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self._initUI()
    
    def _initUI(self):
        self.set_title("App Hello World dengan OOP")
        self.set_size_request(640, 360)
        self.set_icon_from_file("icon.png")
        self.connect('destroy', Gtk.main_quit)

        self.label = Gtk.Label("Aplikasi GTK dengan Python")
        self.add(self.label)

        self.show_all()


# main
if __name__ == "__main__":
    MainWindow()
    Gtk.main()