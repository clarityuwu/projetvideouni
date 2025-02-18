from model import Model
from view import View
from controller import Controller
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.show()
    Gtk.main()

if __name__ == "__main__":
    main()