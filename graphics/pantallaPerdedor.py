from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit)
from graphics import pantallaBase


class PantallaPerdedor(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla perdedor")

        self.graphics = graphics

        self.perdedor = QLabel("Felicitaciones!!! eres un tremendo perdedor!!! ", self)
        self.perdedor.setVisible(True)
        self.perdedor.setGeometry(57, 58, 371, 147)
