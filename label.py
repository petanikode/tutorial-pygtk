import gtk

class App(gtk.Window):
    def __init__(self):
        super(App, self).__init__()

        self.set_title("Latihan Label")
        self.set_size_request(640,320)
        self.set_position(gtk.WIN_POS_CENTER)

        label = gtk.Label("Selamat datang di Petani Kode")
        self.add(label)
        self.connect("destroy", gtk.main_quit)
        self.show_all()


App()
gtk.main()