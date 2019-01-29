#impor pustaka GTK
import gtk

# membuat objek jendela
window = gtk.Window()

# konfigurasi jendela
window.set_size_request(600,200)
window.set_position(gtk.WIN_POS_CENTER)
window.set_title("Pemrograman PyGTK - Petani Kode")
window.connect("destroy", gtk.main_quit)

# tampilkan jendela
window.show()
gtk.main()
