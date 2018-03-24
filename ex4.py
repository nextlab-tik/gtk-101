import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title="Gtk window 1")
window.connect('delete-event', Gtk.main_quit)


label = Gtk.Label()
label.set_text("votre nom et prenon")  # inserer une text a la label
label.set_angle(30)  # regle l affichage avec une angle de 30 degre
label.set_halign(Gtk.Align.END)  # allginé notre label à la droite
window.add(label)  # ajouter label au window


window.show_all()

Gtk.main()
