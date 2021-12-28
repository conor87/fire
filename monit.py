from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QLabel, QWidget, QStackedLayout
from PySide6.QtGui import QMovie, QPixmap
import sys

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        layout = QStackedLayout()

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 1200, 600))
        self.label.setMinimumSize(QtCore.QSize(800, 500))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setObjectName("label")
        

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        pix = QPixmap("media/do_alarmu.bmp").scaledToWidth(1500)
        self.label.setPixmap(pix)
        self.label.move(0,100)
        
        # set qmovie as label
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.movie = QMovie("media/eee.gif")
        self.label2.setMovie(self.movie)
        
        size = QtCore.QSize(50,50)
        #śself.label2.setScaledSize(size)
        
        
        self.label2.move(1100,200)
        self.movie.start()
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setStyleSheet("color: red; font-size: 40px; background-color: yellow")
        self.label3.setText("Uwaga: alarm 1 stopnia - podejrzenie pożaru")
        self.label3.move(100,50)
        
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setStyleSheet("color: red; font-size: 40px; background-color: yellow")
        self.label4.setText("Sprawdź miejsce: Narzędziownia")
        self.label4.move(100,95)
        
        
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
