from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
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
        self.puntaje.setGeometry(250, 130, 100, 60)

        self.nombreRival = QLabel(self)
        self.nombreRival.setGeometry(200, 0, 500, 100)

        self.mensaje = QLabel(self)
        #self.mensaje(0,50, 500,100)


        self.papel_img = QLabel("", self)
        self.papel_img.setStyleSheet("image:url(:/graphics/img/papel.png)")
        self.papel_img.setGeometry(170, 150, 50, 50)
        self.lbl_papel = QLabel("Papel", self)
        self.lbl_papel.setGeometry(170, 230, 50, 50)

        self.tijeras_img = QLabel(self)
        self.tijeras_img.setStyleSheet("border-image:url(:/graphics/img/tijeras.png)")
        self.papel_img.setGeometry(240, 150, 50, 50)
        self.lbl_tijeras = QLabel(self)
        self.lbl_tijeras.setText("Tijeras")
        self.lbl_tijeras.setGeometry(240, 230, 50, 50)

        

    def onNombreDelRival(self, nombre):
        self.nombreRival.setText("Rival: " + nombre)

    def onRondaGanada(self) :
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
        self.puntaje.setText(puntajes[0] + " | " + puntajes[1])
    
