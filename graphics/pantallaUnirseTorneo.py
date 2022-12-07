from PySide6.QtCore import *
from PySide6.QtWidgets import *

import Senal
from graphics import pantallaBase


class PantallaUnirseTorneo(pantallaBase.PantallaBase):
	def __init__(self, graphics):
		super().__init__(graphics)

		self.graphics = graphics

		if not self.objectName():
			self.setObjectName(u"PantallaBase")
		self.resize(500, 500)
		self.tableWidget = QTableWidget(self)
		if (self.tableWidget.columnCount() < 3):
			self.tableWidget.setColumnCount(3)
		__qtablewidgetitem = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
		self.tableWidget.setObjectName(u"tableWidget")
		self.tableWidget.setGeometry(QRect(0, 60, 511, 381))
		self.tableWidget.setLineWidth(1)

		self.tableWidget.setColumnWidth(0, 350)
		self.tableWidget.setColumnWidth(1, 150)
		self.tableWidget.setColumnWidth(2, 0)

		self.retranslateUi(self)

		QMetaObject.connectSlotsByName(self)
		self.tableWidget.setSortingEnabled(False)

		self.titulo = QLabel("Lista de torneos disponibles", self)
		self.titulo.setGeometry(140, 0, 400, 60)

		self.btn_actualizar = QPushButton("actualizar", self)
		self.btn_actualizar.setGeometry(390, 10, 100, 40)
		self.btn_actualizar.clicked.connect(lambda: graphics.getFunctionality().getSignalManager().enviarSenal(Senal.SOLICITAR_LISTA_TORNEOS))

		self.btn_unirseTorneo = QPushButton("Unirse al Torneo", self)
		self.btn_unirseTorneo.setGeometry(10, 460, 150, 30)

		self.btn_torneoPrivado = QPushButton("Torneo Privado", self)
		self.btn_torneoPrivado.setGeometry(340, 460, 150, 30)
		self.btn_torneoPrivado.clicked.connect(self.cambiarAUnirseTorneoPrivado)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
		___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
		___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nombre", None));
		___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
		___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Cantidad de jugadores", None));
		___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
		___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Clave", None));

	def onListaTorneoRecibida(self, datos):
		self.tableWidget.model().removeRows(0, self.tableWidget.rowCount())

		for row in range(0, len(datos)):
			nombre, c_jugadores, clave = datos[row].split("|")
			self.tableWidget.insertRow(row)
			self.tableWidget.setItem(row, 0, QTableWidgetItem(nombre))
			self.tableWidget.setItem(row, 1, QTableWidgetItem(c_jugadores))
			self.tableWidget.setItem(row, 2, QTableWidgetItem(clave))

		self.btn_unirseTorneo.clicked.connect(self.setListenerBotonUnirseTorneo)

	def setListenerBotonUnirseTorneo(self):
		selected_rows = self.tableWidget.selectionModel().selectedIndexes()
		if len(selected_rows) == 0:
			return

		selected_row = selected_rows[0]

		clave = self.tableWidget.item(selected_row.row(), 2).text()
		self.graphics.getFunctionality().getSignalManager().enviarSenal(Senal.UNIRSE_TORNEO_PUBLICO)
		self.graphics.getFunctionality().getSignalManager().enviarPaquete(clave)

	def cambiarAUnirseTorneoPrivado(self):
		self.btn_torneoPrivado.setVisible(False)
		self.tableWidget.setVisible(False)
		self.titulo.setVisible(False)
		self.btn_unirseTorneo.setVisible(False)

		self.lbl_ingreseElCodigo = QLabel("Ingrese el código del torneo.", self)
		self.lbl_ingreseElCodigo.setGeometry(30, 50, 300, 40)
		self.lbl_ingreseElCodigo.show()

		self.codigo = QTextEdit(self)
		self.codigo.setGeometry(150, 200, 200, 30)
		self.codigo.show()

		self.btn_unirseAlTorneo = QPushButton("Unirse al torneo", self)
		self.btn_unirseAlTorneo.setGeometry(70, 420, 200, 30)
		self.btn_unirseAlTorneo.clicked.connect(self.enviarUnirseTorneoPrivado)
		self.btn_unirseAlTorneo.show()

	def enviarUnirseTorneoPrivado(self):
		print("Enviado codigo " + self.codigo.toPlainText())
		self.graphics.getFunctionality().getSignalManager().enviarSenal(Senal.UNIRSE_TORNEO_PRIVADO)
		self.graphics.getFunctionality().getSignalManager().enviarPaquete(self.codigo.toPlainText())

