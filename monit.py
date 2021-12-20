from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QScreen, QFont, QPixmap, QMovie
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
        
    #self.setGeometry(0,0,frmX,frmY)
    self.setGeometry(100,100,600,500)
    self.setWindowTitle("Powiadomienie")
    
    layout = QVBoxLayout()
    
    
    label = QLabel("Hello World", self)
    label.setText("Uwaga pożar: udaj się na miejsce alarmu")
    label.move(100,100)
    label.setFont(QFont("Arial", 22))
    
    '''
    label2 = QLabel(self)
    mapa = QPixmap("media/narzedziownia.bmp")
    label2.setPixmap(mapa)
    '''
    layout.addWidget(label)
    #layout.addWidget(label2)
    label3 = QLabel(self)
    movie = QMovie('R.gif')
    label3.setMovie(movie)
    movie.start()
    layout.addWidget(label3)
    layout.addWidget(QPushButton('right'))
    self.setLayout(layout)
    
    
window = Window()
window.show()
sys.exit(app.exec_())
