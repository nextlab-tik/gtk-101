import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="List Box")

        # set le border du window à 10 pixels
        self.set_border_width(10)

        # creation du container de type ListBox
        listbox = Gtk.ListBox()

        # désactiver la selection des élements du listbox
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        # creer un container Box d'orientation vertical
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(listbox)

        # creer la 1er ligne du list qui va continer les elements
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row1.add(box1)
        label = Gtk.Label("je suis etudiant: ")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)

        # ajouter la ligne à la box
        listbox.add(row1)

        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row2.add(box2)
        label = Gtk.Label("je suis connecte: ")
        switch = Gtk.Switch()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(switch, True, True, 0)
        listbox.add(row2)

        row3 = Gtk.ListBoxRow()
        box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row3.add(box3)
        label = Gtk.Label("je fumme: ")
        check2 = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check2, True, True, 0)
        listbox.add(row3)


window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
