from PySide6.QtWidgets import (QApplication, QToolBar, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit)
from graphics import pantallaBase


    
class PantallaEnfrentamiento(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        opcionSeleccionada = False

        self.setWindowTitle("Pantalla Enfrentamiento")

        self.graphics = graphics


        self.puntaje = QLabel("0 | 0", self)
        self.puntaje.setGeometry(250,130, 100,60)


        self.nombreRival = QLabel("", self)
        self.nombreRival.setGeometry(200,0, 500,100)

        self.mensaje = QLabel("", self)
        self.mensaje(0,50, 500,100)

        self.panel_piedra = QToolBar("panel piedra")
        self.panel_piedra.setGeometry(54, 250, 100, 130)

        self.piedra = QLabel("", self)
        self.piedra.setStyleSheet("border-image:url(:/juego/cliente/graphics/img/piedra.png)")

        self.lblPiedra = QLabel("Piedra", self)
        
        self.panel_piedra.addWidget(self.lblPiedra)

        self.panel_papel = QToolBar("panel papel")
        self.panel_papel.setGeometry(200, 250, 100, 130)

        self.papel_img = QLabel("", self)
        self.papel_img.setStyleSheet("border-image:url(:/juego/cliente/graphics/img/papel.png)")

        self.papel = QLabel("Papel", self)

        self.panel_papel.addWidget(self.papel)

        self.panel_tijeras = QToolBar("panel tijeras")
        self.panel_tijeras.setGeometry(357, 250, 100, 130)

        self.tijeras_img = QLabel("", self)
        self.tijeras_img.setStyleSheet("border-image:url(:/juego/cliente/graphics/img/tijeras.png)")

        self.tijeras = QLabel("Tijeras", self)
        
        self.panel_papel.addWidget(self.papel)

        



        

        def onJugadoresEnLobby(j):
            self.jugadores.setText(j)
           

        def onClaveTorneo(clave):
            self.lbl_MostrarClaveTorneo = QLabel("Clave del torneo:", self)
            self.lbl_MostrarClaveTorneo.setGeometry(40, 130, 200, 30)

            self.lbl_claveTorneo  = QTextEdit()
            self.lbl_claveTorneo.isEnabled(False) 
            self.lbl_claveTorneo.setGeometry(40, 170, 150, 30)
            self.lbl_claveTorneo.setText(clave)

            self.revalidate()
            self.repaint()

            

        def setNombreTorneo(nombreTorneo): 
            self.lbl_nombreTorneo.setText(nombreTorneo)
