from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from graphics import pantallaBase


class PantallaLobby(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla Lobby")

        self.graphics = graphics

        self.lbl_jugadores = QLabel("Jugadores en el lobby: ", self)
        self.lbl_jugadores.setGeometry(50, 250, 200,30)

        self.jugadores = QLabel(self)
        self.jugadores.setGeometry(210, 255, 500, 40)

        self.lbl_nombreTorneo = QLabel(self)
        self.lbl_nombreTorneo.setFont(QFont('Arial', 20))
        self.lbl_nombreTorneo.setGeometry(0, 80, 500, 60)
        self.lbl_nombreTorneo.show()

        self.lbl_MostrarClaveTorneo = QLabel(self)
        self.lbl_MostrarClaveTorneo.setText("Clave del torneo:")
        self.lbl_MostrarClaveTorneo.setGeometry(40, 130, 200, 30)
        self.lbl_MostrarClaveTorneo.hide()

        self.lbl_claveTorneo = QLabel(self)
        self.lbl_claveTorneo.setGeometry(40, 170, 150, 30)



    def onJugadoresEnLobby(self, jugadores):
        self.jugadores.setText(jugadores)

    def onClaveTorneo(self, clave):
        self.lbl_MostrarClaveTorneo.show()
        self.lbl_claveTorneo.setText(clave)

    def setNombreTorneo(self, nombreTorneo):
        self.lbl_nombreTorneo.setText(nombreTorneo)

