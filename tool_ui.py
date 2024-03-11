import sys
from configparser import ConfigParser

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

from tool_funcs import start_btn_callback
from tool_widget import Ui_Form


## Incase you get the "source code string cannot contain null bytes" error from trying to import the Ui_Form
## Open the ui.py file in notepad and change the encoding to UTF-8 then save the file
## This comment applies to PyQt6 for reference

def run():
    print("running!")
    config = ConfigParser()
    config.read('app_settings.ini')
    label_color = config['app_settings']['answer_label_color']
    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
            self.ui = Ui_Form()
            self.ui.setupUi(self)
            # access designer elements after setupUi call
            button_start = self.ui.buttonStart
            self.ui.buttonStart.clicked.connect(self.on_start_button_clicked)
        def mousePressEvent(self, a0):
            self.dragPos = a0.globalPosition().toPoint()

            if a0.button() == Qt.MouseButton.LeftButton:
                print("left click")
        def mouseMoveEvent(self, a0):
            self.move(self.pos() + a0.globalPosition().toPoint() - self.dragPos)
            self.dragPos = a0.globalPosition().toPoint()
            a0.accept()
        def on_start_button_clicked(self, a0):
            self.ui.buttonStart.hide()
            self.ui.frameTool.setStyleSheet("background-color: transparent;")
            self.ui.labelAnswer.setStyleSheet(" " + label_color + "")
            self.ui.labelAnswer.setText(start_btn_callback())
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())