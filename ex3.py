import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title="Gtk window 3")
window.connect('delete-event', Gtk.main_quit)
but = Gtk.Button(label="clik")


# la fonction à executer en click boutton
def on_clik(widget):
    print("hello!")

# relier la fonction à l'évenement de click du bouttton
but.connect("clicked", on_clik)

window.add(but)
window.show_all()
Gtk.main()
