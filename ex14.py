import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class GridWindow(Gtk.ApplicationWindow):

    def __init__(self):
        # set window position to the center of current mouse position and to
        # not be resizable
        super().__init__(title="Demo 2",
                         icon_name="gtk-about",
                         resizable=False,
                         gravity=Gdk.Gravity.NORTH_WEST,
                         window_position=Gtk.WindowPosition.MOUSE,
                         )

        # change window size to 500x500 pixels
        self.set_size_request(500, 500)
        g = Gtk.Grid(column_homogeneous=True)
        self.add(g)

        # create switch button
        e1 = Gtk.Switch()

        # create label with selection support and with content written on pango
        # markup language:
        # https://developer.gnome.org/pango/stable/PangoMarkupFormat.html
        e2 = Gtk.Label("<i>Hi</i> <b>there</b> <u>go</u> <span background='#FFaa00' foreground='#00FFFF'>to</span> <a href='https://google.com'>google</a>",
                       use_markup=True,
                       selectable=True,
                       )

        # create entry with text no visible (for passwords) and max 50 chars
        e3 = Gtk.Entry(text="initial value",
                       editable=True,
                       max_length=50,
                       visibility=False,
                       )
        # add icon to the entry widget
        e3.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "gtk-info")

        # create check button that's actived
        e4 = Gtk.CheckButton("Select me",
                             active=True,
                             )

        # create toggle button (same as check button but with different look
        e5 = Gtk.ToggleButton("toggle")

        # create radio button
        e6 = Gtk.RadioButton("choice1")

        # create 2nd radio button and add it to the same group as 1st radio btn
        e7 = Gtk.RadioButton("choise2")
        e7.join_group(e6)

        students = ["firas", "sahar", "ali", "imen", "slim"]

        # create a comboBox (selection list) and add students content to it
        e8 = Gtk.ComboBoxText()
        for s in students:
            e8.append_text(s)

        # a more general ComboBox that can accept more than just a text
        # 1st: create a store model add add data to it (a store of one str)
        students_store = Gtk.ListStore(str)
        for s in students:
            students_store.append([s])
        # 2nd: create ComboBox using the store and with 2nd elemet selected
        e9 = Gtk.ComboBox(
            model=students_store,
            active=2,
        )
        # 3rd: specify the comboBox item rendering (Text cell)
        renderer_text = Gtk.CellRendererText()
        e9.pack_start(renderer_text, True)
        e9.add_attribute(renderer_text, "text", 0)

        # append the widget to the Grid container
        g.attach(e1, left=0, top=0, width=1, height=1)
        g.attach(e2, left=1, top=0, width=1, height=1)
        g.attach(e3, left=0, top=1, width=1, height=1)
        g.attach(e4, left=1, top=1, width=1, height=1)
        g.attach(e5, left=0, top=2, width=2, height=1)
        g.attach(e6, left=0, top=3, width=1, height=1)
        g.attach(e7, left=1, top=3, width=1, height=1)
        g.attach(e8, left=0, top=4, width=1, height=1)
        g.attach(e9, left=1, top=4, width=1, height=1)

w = GridWindow()
w.connect("delete-event", Gtk.main_quit)
w.show_all()
Gtk.main()
