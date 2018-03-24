import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# greation du class MyWindow


class MyWindow(Gtk.Window):  # herité la class GTk.Window

    def __init__(self):  # constructeur du class Mywindow
        # appel au constructeur du class parent
        Gtk.Window.__init__(self, title="window class")


window = MyWindow()  # generation d un objet du class Mywindow
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
