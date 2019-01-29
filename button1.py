import gtk

class App(gtk.Window):
    def __init__(self):
        super(App, self).__init__()

        self.set_title("Latihan Button")
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)

        # membuat button
        button = gtk.Button("Sebuah Tombol")

        # membuat container untuk button
        container = gtk.Fixed()

        # menambahkan button ke container
        container.put(button, 20, 30)

        # menambahkan container ke jendela
        self.add(container)
        self.connect("destroy", gtk.main_quit)
        self.show_all()




App()
gtk.main()