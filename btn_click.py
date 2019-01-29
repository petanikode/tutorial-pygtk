import gtk

class App(gtk.Window):

    def __init__(self):
        super(App, self).__init__()

        self.set_title("Latihan Button Click")
        self.set_size_request(400, 200)
        self.set_position(gtk.WIN_POS_CENTER)

        # membuat button dan label
        button = gtk.Button("Klik Saya!")
        self.label = gtk.Label("...")

        # membuat container untuk button
        container = gtk.Fixed()

        # menambahkan button ke container
        container.put(button, 20, 30)
        container.put(self.label, 20, 100)

        # connect singnal dan fungsi
        self.connect("destroy", gtk.main_quit)
        button.connect("clicked", self.on_button_click)

        # menambahkan container ke jendela
        self.add(container)
        self.show_all()
    
    def on_button_click(self, button):
        print("Tombol diklik!")
        self.label.set_text("Hello World")


App()
gtk.main()