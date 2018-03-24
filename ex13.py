import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Events:
    # add contructor to add the needed widgets to the instance

    def __init__(self, builder):
        self.builder = builder
        self.entry = builder.get_object("entry")

    def affiche(self, widget):
        # print the entry text and force flushing it to the terminal
        print(self.entry.get_text(), flush=True)

    def reset(self, widget):
        self.entry.set_text('')

builder = Gtk.Builder()

# get the absolute template path relative to the running python script
tmpl = os.path.join(os.path.dirname(__file__), "template.glade")

builder.add_from_file(tmpl)

builder.connect_signals(Events(builder))

w = builder.get_object("window")
w.connect("delete-event", Gtk.main_quit)
w.show_all()

Gtk.main()
