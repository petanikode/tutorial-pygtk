import gtk

class App(gtk.Window):
  def __init__(self):
    super(App, self).__init__()
   
    self.set_title("Latihan Tombol")
    self.set_size_request(250,150)
    self.set_position(gtk.WIN_POS_CENTER)
   
    btn1 = gtk.Button("Tombol 1")
    btn1.set_sensitive(False) # non-aktifkan tombol
    btn2 = gtk.Button("Tombol 2")
    btn3 = gtk.Button(stock=gtk.STOCK_CLOSE) 
    btn4 = gtk.Button("Tombol 4")
    btn4.set_size_request(80,40) # set ukuran tombol
   
    container = gtk.Fixed() # membuat kontainer
   
    container.put(btn1, 20, 30)
    container.put(btn2, 100, 30)
    container.put(btn3, 20, 80)
    container.put(btn4, 100, 80)
   
    self.connect("destroy", gtk.main_quit)
   
    self.add(container)
    self.show_all()

App()
gtk.main()