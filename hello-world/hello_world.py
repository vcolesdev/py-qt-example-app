import sys
import random

from PySide6 import QtCore, QtWidgets


class HelloWorldWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.label = QtWidgets.QLabel
        self.button = QtWidgets.QPushButton
        self.layout = QtWidgets.QVBoxLayout(self)

        self.widgets_layout = self.add_widgets_to_layout()
        self.widget_button = self.widgets_layout["widget_button"]
        self.widget_button.clicked.connect(self.magic)

    def create_qt_label(self, text="Hello World!"):
        """
        Create a Qt label widget
        :param text:
        :return:
        """
        label = self.label(text)
        return label

    def create_qt_push_button(self, text="Click me!"):
        """
        Create a Qt push button widget
        :param text:
        :return:
        """
        button = self.button(text)
        return button

    def create_qt_layout(self):
        """
        Create a Qt layout widget
        :return:
        """
        layout = self.layout
        return layout

    def add_layout_widget(self, layout_widget: QtWidgets.QWidget):
        """
        Add a widget to a Qt layout
        :param layout_widget:
        :return:
        """
        layout = self.create_qt_layout()
        layout.addWidget(layout_widget)
        return layout

    def add_widgets_to_layout(self):
        """
        Add created widgets to a Qt layout
        :return:
        """
        widget_text = self.create_qt_label("Hello World!")
        widget_button = self.create_qt_push_button("Click me!")

        self.add_layout_widget(widget_text)
        self.add_layout_widget(widget_button)

        widget_layout = {
            "widget_text": widget_text,
            "widget_button": widget_button
        }

        return widget_layout

    @QtCore.Slot()
    def magic(self):
        """
        Slot to change the text of the label
        :return:
        """
        text = random.choice(self.hello)
        layout = self.add_widgets_to_layout()
        layout["widget_text"].setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = HelloWorldWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
