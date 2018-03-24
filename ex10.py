import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

w = Gtk.Window(title="Gtk Window")
w.connect("delete-event", Gtk.main_quit)

# create a label with content as Pango Markup language
# https://developer.gnome.org/pango/stable/PangoMarkupFormat.html
label = Gtk.Label(label="""<i>Je</i>
<span background='red' foreground='white'>suis</span>
<u>Moez</u>
<a href='http://google.com'>lien</a>""")
label.set_use_markup(True)

w.add(label)
w.show_all()
Gtk.main()
