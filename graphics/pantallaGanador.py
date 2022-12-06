from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit)
from graphics import pantallaBase


    
class PantallaGanador(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla ganador")

        self.graphics = graphics


        self.perdedor = QLabel("Felicitaciones!!! eres el ganador del gran torneo ", self)
        self.perdedor.setVisible(True)
        self.perdedor.setGeometry(57, 58, 371, 147)

