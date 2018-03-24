import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="window class")

        # creer le container
        self.box = Gtk.Box(spacing=100)

        # ajouter le container à window
        self.add(self.box)

        self.salutBut = Gtk.Button(label="salut")
        self.salutBut.connect("clicked", self.salut)

        # ajouter le boutton au container
        self.box.pack_start(self.salutBut, expand=True, fill=True, padding=0)

        self.byeBut = Gtk.Button(label="bye")
        self.byeBut.connect("clicked", self.bye)
        self.box.pack_start(self.byeBut, expand=True, fill=True, padding=0)

    def salut(self, widget):
        print("salut!")

    def bye(self, widget):
        print("bye!")


window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
