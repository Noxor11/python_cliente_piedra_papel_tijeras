from graphics.pantallaBase import PantallaBase
from graphics.pantallaConexion import PantallaConexion
from graphics.pantallaLobby import PantallaLobby
from graphics.pantallaEnfrentamiento import PantallaEnfrentamiento
from graphics.pantallaCreacionTorneo import PantallaCreacionTorneo
from graphics.pantallaInicial import PantallaInicial
from graphics.pantallaGanador import PantallaGanador
from graphics.pantallaPerdedor import PantallaPerdedor
from graphics.pantallaUnirseTorneo import PantallaUnirseTorneo

from PySide6.QtWidgets import *
from GameFunctionality import GameFunctionality

import threading



class Graphics(QApplication):



	def __init__(self, functionality: GameFunctionality):
		super().__init__()

		self.functionality = functionality

		self.window = QMainWindow()
		self.window.setFixedSize(500,500)

		self.functionality: GameFunctionality

		self.pantallaPerdedorTorneo = PantallaPerdedor(self)
		self.pantallaPerdedorTorneo.hide()

		self.pantallaGanadorTorneo = PantallaGanador(self)
		self.pantallaGanadorTorneo.hide()

		self.pantallaEnfrentamiento = PantallaEnfrentamiento(self)
		self.pantallaEnfrentamiento.hide()

		self.pantallaConexion = PantallaConexion(self)
		self.pantallaConexion.hide()

		self.pantallaLobby = PantallaLobby(self)
		self.pantallaLobby.hide()

		self.pantallaCreacionTorneo = PantallaCreacionTorneo(self)
		self.pantallaCreacionTorneo.hide()

		self.pantallaUnirseTorneo = PantallaUnirseTorneo(self)
		self.pantallaUnirseTorneo.hide()

		self.pantallaInicial = PantallaInicial(self)
		self.pantallaInicial.hide()

		self.pantallaActual = self.pantallaInicial
		self.pantallaActual.show()

		self.initGraphics()
		"""
		self.setContentPane(pantallaInicial)
		self.setSize(pantallaInicial.getSize())
		self.setLocationRelativeTo(null)
		self.setDefaultCloseOperation(EXIT_ON_CLOSE)
		self.setVisible(true)
		"""

	def initGraphics(self):
		self.pantallaActual = self.pantallaInicial
		self.window.show()

	def onConectando(self):
		self.cambiarPantalla(self.pantallaConexion)

	def onConexionExitosa(self):
		print("GRAPHICS dice: Conectado!")
		self.pantallaConexion.onConexionExitosa()

	def getFunctionality(self) -> GameFunctionality:
		return self.functionality

	def onEnviarSeleccion(self) :
		self.cambiarPantalla(self.pantallaEnfrentamiento)

	def onEnviarNombre(self) :
		print("GRAPHICS dice: Esperando a que el usuario escriba su nombre.")
		self.cambiarPantalla(self.pantallaConexion)

	def onConexionExitosaTorneo(self):
		self.cambiarPantalla(self.pantallaLobby)

	def onJugadoresEnLobby(self, jugadores: str):
		self.pantallaLobby.onJugadoresEnLobby(jugadores)

	def getPantallaInicial(self):
		return self.pantallaInicial

	def setPantallaInicial(self, pantallaInicial: PantallaInicial) :
		self.pantallaInicial = pantallaInicial

	def getPantallaConexion(self):
		return self.pantallaConexion

	def setPantallaConexion(self, pantallaConexion: PantallaConexion) :
		self.pantallaConexion = pantallaConexion


	def getPantallaEnfrentamiento(self):
		return self.pantallaEnfrentamiento

	def setPantallaEnfrentamiento(self, pantallaEnfrentamiento: PantallaEnfrentamiento):
		self.pantallaEnfrentamiento = pantallaEnfrentamiento

	def getPantallaLobby(self):
		return self.pantallaLobby

	def setPantallaLobby(self, pantallaLobby: PantallaLobby):
		self.pantallaLobby = pantallaLobby

	def getPantallaCreacionTorneo(self) :
		return self.pantallaCreacionTorneo

	def getPantallaUnirseTorneo(self) :
		return self.pantallaUnirseTorneo

	def onClaveTorneo(self, clave: str):
		self.functionality.setClaveTorneo(clave)
		self.pantallaLobby.onClaveTorneo(clave)


	def setNombreTorneo(self, nombreTorneo: str) :
		self.pantallaLobby.setNombreTorneo(nombreTorneo)

	def cambiarPantalla(self, pantallaSiguiente: PantallaBase):
		self.pantallaActual.hide()
		self.pantallaActual = pantallaSiguiente
		pantallaSiguiente.show()

		"""
		if(pantallaActual instanceof PantallaCreacionTorneo):
			self.pantallaCreacionTorneo = PantallaCreacionTorneo(self)
		elif (pantallaActual instanceof PantallaLobby) :
			pantallaLobby = PantallaLobby(self)
		elif (pantallaActual instanceof PantallaUnirseTorneo) :
			pantallaUnirseTorneo = PantallaUnirseTorneo(self)
		elif (pantallaActual instanceof PantallaEnfrentamiento) :
			pantallaEnfrentamiento = PantallaEnfrentamiento(self)


		self.setContentPane(pantallaSiguiente)
		"""

	def getPantallaGanadorTorneo(self):
		return self.pantallaGanadorTorneo

	def setPantallaGanadorTorneo(self, pantallaGanadorTorneo: PantallaGanador) :
		self.pantallaGanadorTorneo = pantallaGanadorTorneo

	def volver(self) :
		# self.setContentPane(pantallaInicial)
		print("placeholder")

	def getPantallaPerdedorTorneo(self):
		return self.pantallaPerdedorTorneo
