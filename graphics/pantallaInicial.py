from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit)

import Senal
from graphics import pantallaBase


class PantallaInicial(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla inicial")

        self.graphics = graphics


        self.titulo = QLabel("Piedra, Papel, o Tijera!", self)
        self.titulo.setGeometry(57,58,371, 147)

        self.joinServer = QPushButton('Unirse a un torneo', self)
        self.joinServer.setGeometry(262, 228, 144,27)

        self.joinServer.clicked.connect(self.manejarUnirseTorneo)

        self.createServer = QPushButton('Crear torneo', self)
        self.createServer.setGeometry(63, 228, 108,27)

        self.createServer.clicked.connect(self.cambiarPantallaACreacionTorneo)

    def manejarUnirseTorneo(self):
        self.graphics.getFunctionality().getSignalManager().enviarSenal(Senal.SOLICITAR_LISTA_TORNEOS)
        print("Enviada senal de solicitar lista torneos")
        self.graphics.cambiarPantalla(self.graphics.getPantallaUnirseTorneo())

    def cambiarPantallaACreacionTorneo(self):
        self.graphics.cambiarPantalla(self.graphics.getPantallaCreacionTorneo())