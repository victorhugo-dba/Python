# Pyqt5 introduction
import os
import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        
        pasta_do_script = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(pasta_do_script, "test_image.png")
        
        self.setWindowIcon(QIcon(image_path))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 11))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #332d2d; background-color: #2fbceb; font-weight: bold; font-style: italic; text-decoration: underline;")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #label.setAlignment(Qt.AlignTop) #vertically top
        #label.setAlignment(Qt.AlignBottom) #vertically bottom
        #label.setAlignment(Qt.AlignVCenter) #vertically center

        # label.setAlignment(Qt.AlignRight) #horizontally right
        #label.setAlignment(Qt.AlignHCenter) #horizontally center
        #label.setAlignment(Qt.AlignLeft) #horizontally left

def main():
    try:
        myappid = 'mygui.firstapp.v1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except:
        pass

    app = QApplication(sys.argv)
    
    pasta_do_script = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(pasta_do_script, "test_image.png")
    app.setWindowIcon(QIcon(image_path))

    window = main_window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
