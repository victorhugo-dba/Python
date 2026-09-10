# Pyqt5 introduction
import sys
from PyQt5.QtWidgets import  QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500 )
        self.setWindowIcon(QIcon("GUI_profile_pic.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 11))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #332d2d;"
                            "background-color: #2fbceb;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) #vertically top
        #label.setAlignment(Qt.AlignBottom) #vertically bottom
        #label.setAlignment(Qt.AlignVCenter) #vertically center

        # label.setAlignment(Qt.AlignRight) #horizontally right
        #label.setAlignment(Qt.AlignHCenter) #horizontally center
        #label.setAlignment(Qt.AlignLeft) #horizontally left

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 

def main():
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()