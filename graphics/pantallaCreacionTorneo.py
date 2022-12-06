from PySide6.QtWidgets import *

import Senal
from graphics import pantallaBase

    
class PantallaCreacionTorneo(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla creacion del torneo")

        self.graphics = graphics

        self.senalEnviada = False

        self.pnl_partidaPublica = QPushButton(self)
        self.pnl_partidaPublica.setText("Partida Pública")
        self.pnl_partidaPublica.setGeometry(100, 230, 100, 50)

        #self.img_torneoPublico = QLabel(self)
        #self.img_torneoPublico.setText("toolbar partida publica")
        #self.img_torneoPublico.setGeometry(100,100, 50, 50)
        #self.img_torneoPublico.setStyleSheet("border-image:url(:/piedra-papel-tijeras/graphics/img/partida_publica.png)")

        #self.lblTorneoPublico = QLabel("Torneo Público", self)

        self.pnl_partidaPrivada = QPushButton(self)
        self.pnl_partidaPrivada.setGeometry(240, 230, 100, 50)
        self.pnl_partidaPrivada.setText("Partida Privada")

        #self.lblTorneoPublico = QLabel("Torneo Privado", self)

        self.pnl_partidaPublica.clicked.connect(lambda: self.pedirNombreDelTorneo(Senal.CREAR_TORNEO_PUBLICO))
        self.pnl_partidaPrivada.clicked.connect(lambda: self.pedirNombreDelTorneo(Senal.CREAR_TORNEO_PRIVADO))

        

    def pedirNombreDelTorneo(self, senal):
        self.pnl_partidaPrivada.setVisible(False)
        self.pnl_partidaPublica.setVisible(False)

        self.lbl_nombreTorneo = QLabel(self)
        self.lbl_nombreTorneo.setText("Introduzca el nombre del torneo.")
        self.lbl_nombreTorneo.setGeometry(50, 50, 200, 30)
        self.lbl_nombreTorneo.show()

        self.txt_nombreTorneo = QTextEdit(self)
        self.txt_nombreTorneo.setGeometry(50, 90, 200, 30)
        self.txt_nombreTorneo.show()

        self.btn_enviar = QPushButton(self)
        self.btn_enviar.setText("Enviar")
        self.btn_enviar.setGeometry(70, 320, 80, 30)
        self.btn_enviar.clicked.connect(lambda: self.cambiarPantallita(senal))
        self.btn_enviar.show()

        self.lbl_nombreTorneo = QLabel("Introduzca el nombre del torneo.", self)
        self.lbl_nombreTorneo.setGeometry(50, 50, 200,30)
        self.lbl_nombreTorneo.show()


    def cambiarPantallita(self, senal):
        self.graphics.setNombreTorneo(self.txt_nombreTorneo.toPlainText())
        self.graphics.getFunctionality().getSignalManager().enviarSenal(senal)
        self.graphics.getFunctionality().getSignalManager().enviarPaquete(self.txt_nombreTorneo.toPlainText())
        self.graphics.getFunctionality().getSignalManager().enviarPaquete("4")
        self.senalEnviada = True
        self.graphics.cambiarPantalla(self.graphics.getPantallaConexion())

