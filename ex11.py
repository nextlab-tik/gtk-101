import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Gtk Window")
        box = Gtk.Box()

        # create entry element and add it to the instance for use later on
        # callback functions
        self.entry = Gtk.Entry()

        btn = Gtk.Button(label="affiche")
        btn2 = Gtk.Button(label='reset')
        box.add(self.entry)
        box.add(btn)
        box.add(btn2)

        # assign handler functions to the click signals
        btn.connect("clicked", self.btn_click)
        btn2.connect("clicked", self.reset_entry)

        self.add(box)
        self.connect("delete-event", Gtk.main_quit)

    # define the reset btn click event handler
    def reset_entry(self, widget):
        # set the entry content to '' (empty string)
        self.entry.set_text('')

    # define the affiche btn click event handler
    def btn_click(self, widget):
        # print the entry widget content
        print(self.entry.get_text())

w = MyWindow()
w.show_all()
Gtk.main()
