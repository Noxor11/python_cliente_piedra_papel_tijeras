from PySide6.QtWidgets import (QApplication,QToolBar, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit)
from graphics import pantallaBase

    
class PantallaCreacionTorneo(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla creacion del torneo")

        self.graphics = graphics

        senalEnviada = False

        self.pnl_partidaPublica = QToolBar("")
        self.pnl_partidaPublica.setGeometry(125, 230, 250, 250)   

        self.img_torneoPublico = QLabel("toolbar partida publica", self)       
        self.img_torneoPublico.setStyleSheet("border-image:url(:/juego/cliente/graphics/img/partida_publica.png)")

        self.lblTorneoPublico = QLabel("Torneo Público", self) 

        self.pnl_partidaPrivada = QToolBar("toolbar partida privada")
        self.pnl_partidaPrivada.setGeometry(125, 0, 250, 250)

        self.lblTorneoPublico = QLabel("Torneo Privado", self) 


        

        self.pnl_partidaPublica.clicked.connect(self.graphics.cambiarPantalla(Senal.CREAR_TORNEO_PUBLICO))
        self.pnl_partidaPrivada.clicked.connect(self.graphics.cambiarPantalla(Senal.CREAR_TORNEO_PRIVADO))

        

        def pedirNombreDelTorneo(senal):
            self.pnl_partidaPrivada.setVisible(False)
            self.pnl_partidaPublica.setVisible(False)

            self.lbl_nombreTorneo = QLabel("Introduzca el nombre del torneo.", self) 
            self.lbl_nombreTorneo.setGeometry(50, 50, 200,30)

