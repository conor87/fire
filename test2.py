from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QScreen, QFont, QPixmap, QMovie, QImage
import sys

app = QApplication([])
SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
#Get Screen Width
frmX=SrcSize.width()
#Get Screen Height
frmY=SrcSize.height()

class Window(QWidget):
  def __init__(self):
    super().__init__()
        
    self.setGeometry(0,0,frmX,frmY)
    self.setWindowTitle("Powiadomienie")
    
    layout = QVBoxLayout()

    label4 = QLabel("zdjecie", self)
    #zdj = QImage("media/narzedziownia.bmp")
    pix = QPixmap("media/narzedziownia.bmp").scaledToWidth(1200)
    label4.setPixmap(pix)
    
    label3 = QLabel(self)
    movie = QMovie("red_dot.gif")
    movie.setSpeed(500)
    label3.setMovie(movie)
    movie.start()
    layout.addWidget(label3)
    layout.addWidget(label4)
    layout.addWidget(QPushButton('right'))
    self.setLayout(layout)
    
    
window = Window()
window.show()
sys.exit(app.exec_())
