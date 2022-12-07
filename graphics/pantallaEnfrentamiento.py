from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont, QPixmap

import Senal
from graphics import pantallaBase
import sys


class PantallaEnfrentamiento(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.opcionSeleccionada = False

        self.setWindowTitle("Pantalla Enfrentamiento")

        self.graphics = graphics

        self.puntaje = QLabel(self)
        self.puntaje.setText("0 | 0")
        self.puntaje.setGeometry(250, 40, 100, 60)

        self.nombreRival = QLabel(self)
        self.nombreRival.setGeometry(200, 0, 500, 100)

        self.mensaje = QLabel(self)
        self.mensaje.setGeometry(120, 100, 250, 50)
        self.mensaje.setFont(QFont("Arial", 19))
        #self.mensaje(0,50, 500,100)

        self.piedra_img = QLabel(self)
        self.piedra_img.setGeometry(50, 150, 100, 100)
        self.piedra_img.setPixmap(QPixmap("graphics/img/piedra.png"))
        self.lbl_piedra = QLabel("Piedra", self)
        self.lbl_piedra.setGeometry(70, 280, 50, 50)

        self.papel_img = QLabel(self)
        self.papel_img.setGeometry(180, 150, 100, 100)
        self.papel_img.setPixmap(QPixmap('graphics/img/papel.png'))
        self.lbl_papel = QLabel("Papel", self)
        self.lbl_papel.setGeometry(200, 280, 50, 50)

        self.tijeras_img = QLabel(self)
        self.tijeras_img.setGeometry(310, 150, 100, 100)
        self.tijeras_img.setPixmap(QPixmap("graphics/img/tijeras.png"))
        self.lbl_tijeras = QLabel(self)
        self.lbl_tijeras.setText("Tijeras")
        self.lbl_tijeras.setGeometry(330, 280, 50, 50)

        self.piedra_img.mouseReleaseEvent = lambda x: self.enviarSeleccion(senal=Senal.PIEDRA)
        self.papel_img.mouseReleaseEvent = lambda x: self.enviarSeleccion(senal=Senal.PAPEL)
        self.tijeras_img.mouseReleaseEvent = lambda x: self.enviarSeleccion(senal=Senal.TIJERA)


    def enviarSeleccion(self, senal):
        self.graphics.getFunctionality().getSignalManager().enviarSenal(senal)
        self.mensaje.setText("Selección enviada!")
        self.mensaje.show()

        self.opcionSeleccionada = True

        print("Clicked", senal)

    def onNombreDelRival(self, nombre):
        self.nombreRival.setText("Rival: " + nombre)

    def onRondaGanada(self):
        self.mensaje.setText("¡Has ganado la ronda!")
        self.opcionSeleccionada = False

    def onRondaPerdida(self):
        self.mensaje.setText("Has perdido la ronda :(")
        self.opcionSeleccionada = False

    def onEmpate(self):
        self.mensaje.setText("Empate!!!")
        self.opcionSeleccionada = False

    def onEnfrentamientoGanado(self):
        self.mensaje.setText("¡Has ganado el enfrentamiento!")
        self.opcionSeleccionada = True

    def onEnfrentamientoPerdido(self):
        self.mensaje.setText("Has perdido el enfrentamiento :(")
        self.opcionSeleccionada = True

    def onEmpezarFinal(self):
        self.mensaje.setText("¡Empieza la final!")
        self.opcionSeleccionada = False

    def onObtenerPuntaje(self, puntajes) :
        self.puntaje.setText(str(puntajes[0]) + " | " + str(puntajes[1]))
    
