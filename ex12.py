import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Events:
    def affiche(self, widget):
        print("affiche")

    def reset(self, widget):
        print("reset")

# build the widgets element using the glade template file
builder = Gtk.Builder()
builder.add_from_file(r"template.glade")

# assign the events handlers defined to the Events class isntance to the
# builder widgets
builder.connect_signals(Events())

# get the window element instance from the builder and show_all its elements
w = builder.get_object("window")
w.connect("delete-event", Gtk.main_quit)
w.show_all()

Gtk.main()
