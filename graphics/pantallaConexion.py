from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit)
from graphics import pantallaBase


class PantallaConexion(pantallaBase.PantallaBase):
    def __init__(self, graphics):
        super().__init__(graphics)

        self.setWindowTitle("pantalla conexion")

        self.graphics = graphics


        self.lbl_nombre = QLabel("Nombre de usuario: ", self)
        self.conexion = QLabel("Conectando...", self)
        self.conexion.resize(200,200)

        self.nombreDeUsuario = QLineEdit(self)
        
        
        ##layout_padre = QHBoxLayout()
        #layout_hijo = QVBoxLayout()
        #layout_padre.addLayout(layout_hijo)
        #layout_hijo.addWidget(QPushButton('V1'))
        #layout_hijo.addWidget(QPushButton('V2'))
        #layout_hijo.addWidget(QPushButton('V4'))
        self.enviar = QPushButton('Enviar', self)
        self.enviar.move(20, 20)
        ##layout_padre.addWidget(QPushButton('Volver'))
        #layout_padre.addWidget(QPushButton('H2'))
        #layout_padre.addWidget(QPushButton('H3'))
        #layout_padre.addWidget(QPushButton('H4'))
        #componente_principal = QWidget()
        #componente_principal.setLayout(layout_padre)
        #self.setCentralWidget(componente_principal)

        

        #def cambiarPantalla(self):
        #graphics.cambiarPantalla(graphics.getPantallaInicial())

        def onConectando():
            self.conexion.setText("Conectando...")

            

            self.lbl_nombre.setVisible(False)
            self.nombreDeUsuario.setVisible(False)
            self.enviar.setVisible(False)

        def onConexionExitosa():
            self.lbl_nombre.setGeometry(100,154,194,40)
            
            self.nombreDeUsuario.setGeometry(216,155,217,40)

            self.enviar.setGeometry(200, 300,100,50)

            self.lbl_nombre.setVisible(True)
            self.nombreDeUsuario.setVisible(True)
            self.enviar.setVisible(True)

            self.enviar.clicked.connect(self.hola)

        def hola():
            graphics.getFunctionality()
            graphics.getSignalManager()
            graphics.enviarPaquete(self.nombreDeUsuario.getText())
            onConectando()