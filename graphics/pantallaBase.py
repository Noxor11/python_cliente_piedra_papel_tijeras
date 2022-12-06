from PySide6.QtWidgets import *


class PantallaBase(QMainWindow):

	def __init__(self, graphics):
		super().__init__()
		self.btn_volver = QPushButton(self)
		self.btn_volver.setText("Volver")

		self.setFixedSize(500,500)