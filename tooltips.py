import gtk

class App(gtk.Window):

  def __init__(self):
    super(App, self).__init__()
   
    self.set_title("Latihan Tooltips")
    self.set_size_request(250,200)
    self.set_position(gtk.WIN_POS_CENTER)
   
    self.connect("destroy", gtk.main_quit)
   
    self.container = gtk.Fixed()
    self.add(self.container)
   
    button = gtk.Button("Sebuah Tombol")
    button.set_size_request(100,35)
   
    self.container.put(button,50,50)
   
    self.set_tooltip_text("Ini jendela")
    button.set_tooltip_text("Ini adalah sebuah tombol")
   
    self.show_all()
   
App()
gtk.main()