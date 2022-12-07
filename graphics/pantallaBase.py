from PySide6.QtWidgets import *


class PantallaBase(QWidget):

	def __init__(self, graphics):
		super().__init__(graphics.window)
		self.btn_volver = QPushButton(self)
		self.btn_volver.setText("Volver")
		self.btn_volver.setGeometry(10, 10, 100, 40)

		self.btn_volver.clicked.connect(lambda: graphics.cambiarPantalla(graphics.pantallaInicial))

		self.setFixedSize(500,500)