import gtk

class App(gtk.Window):
    def __init__(self):
        super(App, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Jendela dengan Ikon")
        self.set_icon_from_file("icon.png")
        self.show()

App()
gtk.main()