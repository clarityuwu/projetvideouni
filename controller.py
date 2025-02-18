class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button.connect("clicked", self.on_button_clicked)
        self.update_view()

    def on_button_clicked(self, widget):
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        self.view.label.set_text(data)