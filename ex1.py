# Specifier la version API de Gtk à utilisé (3.0)
import gi
gi.require_version('Gtk', '3.0')

# importer la lib Gtk
from gi.repository import Gtk

# creation object fenetre avec titre "Gtk window 1"
window = Gtk.Window(title="Gtk window 1")

# connecter l'evenement de fermuture de fenetre à fonction predefinie
# "Gtk.main_quit" qui termine notre application
window.connect('delete-event', Gtk.main_quit)

# afficher le fenetre et ses contenus
window.show_all()

# entrer à la lopp principale qui gere les evenements
Gtk.main()
