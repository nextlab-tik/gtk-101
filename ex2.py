import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title="Gtk window 2")
window.connect('delete-event', Gtk.main_quit)

# creation du botton evec "click" comme contenu
but = Gtk.Button(label="click")

# ajouter le bouton à la fenetre
window.add(but)

window.show_all()
Gtk.main()
