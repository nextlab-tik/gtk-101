import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        # creation d'un container de type Grid (layout de type tableau)
        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        # ajoute du button 1
        grid.add(button1)

        # ajoute button 2 en 2eme colonne et premier ligne avec hauteur d'une
        # seule ligne et largeur de 2 colonnes
        grid.attach(button2, left=1, top=0, width=2, height=1)

        # ajoute button3 à dessous du button1 avec hauteur de 1 et largeur de 2
        grid.attach_next_to(
            button3, sibling=button1, side=Gtk.PositionType.BOTTOM, width=1, height=2)

        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)

        grid.attach(button5, 1, 2, 1, 1)

        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
