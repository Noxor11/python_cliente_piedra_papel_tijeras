from PySide6.QtWidgets import (QApplication, QToolBar, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit)
from graphics import pantallaBase


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

        self.panel_piedra = QToolBar("panel piedra")
        self.panel_piedra.setGeometry(54, 250, 100, 130)

        self.piedra = QLabel("", self)
        self.piedra.setStyleSheet("border-image:url(:/graphics/img/piedra.png)")

        self.lblPiedra = QLabel("Piedra", self)
        
        self.panel_piedra.addWidget(self.lblPiedra)

        self.panel_papel = QToolBar("panel papel")
        self.panel_papel.setGeometry(200, 250, 100, 130)

        self.papel_img = QLabel("", self)
        self.papel_img.setStyleSheet("border-image:url(:/graphics/img/papel.png)")

        self.papel = QLabel("Papel", self)

        self.panel_papel.addWidget(self.papel)

        self.panel_tijeras = QToolBar("panel tijeras")
        self.panel_tijeras.setGeometry(357, 250, 100, 130)

        self.tijeras_img = QLabel(self)
        self.tijeras_img.setStyleSheet("border-image:url(:/graphics/img/tijeras.png)")

        self.tijeras = QLabel(self)
        self.tijeras.setText("Tijeras")
        
        self.panel_tijeras.addWidget(self.tijeras)

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
    
