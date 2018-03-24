import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="window class")

        salutBut = Gtk.Button(label="salut")
        salutBut.connect("clicked", self.salut)
        self.add(salutBut)

    # definir la fonction handler d'evenement de click dans la classe
    def salut(self, widget):
        print("salut!")


window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
