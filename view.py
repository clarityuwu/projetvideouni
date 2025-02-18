import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class View:
    def __init__(self):
        self.window = Gtk.Window(title="MVC Example")
        self.label = Gtk.Label(label="")
        self.button = Gtk.Button(label="Click Me")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

        self.window.add(self.box)
        self.window.connect("destroy", Gtk.main_quit)

    def show(self):
        self.window.show_all()